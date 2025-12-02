import pytest
from unittest.mock import MagicMock
import paramiko
import stop_services_oops as s

class DummyChannel:
    def __init__(self, status=0):
        self._status = status
    def recv_exit_status(self):
        return self._status

class DummyStream:
    def __init__(self, data: bytes, channel_status=0):
        self._data = data
        self.channel = DummyChannel(channel_status)
    def read(self):
        return self._data

def make_mock_client(stdout_bytes: bytes, stderr_bytes: bytes, status=0):
    client = MagicMock(spec=paramiko.SSHClient)
    def exec_command(cmd, timeout=...):
        return (MagicMock(), DummyStream(stdout_bytes, status), DummyStream(stderr_bytes, status))
    client.exec_command.side_effect = exec_command
    return client

def test_escape_for_echo():
    assert s.escape_for_echo("pa'ss\\word") == "pa'\"'\"'ss\\\\word"

def test_make_cmds():
    assert "systemctl stop nginx" in s.make_stop_cmd("nginx")
    assert "sudo systemctl stop nginx" in s.make_sudo_stop_cmd("nginx", None)
    assert "echo" in s.make_sudo_stop_cmd("nginx", "pw")

def test_parse_stop_result_ok():
    ok, reason = s.parse_stop_result("some\nOK\n", "")
    assert ok and "stopped" in reason.lower() or ok

def test_parse_stop_result_permission_denied():
    ok, reason = s.parse_stop_result("", "Permission denied")
    assert not ok and "permission denied" in reason.lower()

def test_stop_service_no_sudo_needed():
    client = make_mock_client(b"OK\n", b"", status=0)
    ok, msg = s.stop_service(client, "nginx", None)
    assert ok and "no sudo" in msg.lower()

def test_stop_service_with_sudo_success():
    # First call fails, second (sudo) returns OK
    client = MagicMock(spec=paramiko.SSHClient)
    def exec_command(cmd, timeout=...):
        if cmd.startswith("systemctl"):
            return (MagicMock(), DummyStream(b"FAIL\n", 1), DummyStream(b"",1))
        return (MagicMock(), DummyStream(b"OK\n", 0), DummyStream(b"",0))
    client.exec_command.side_effect = exec_command
    ok, msg = s.stop_service(client, "nginx", "pw")
    assert ok and "sudo" in msg.lower()

def test_stop_service_failures():
    client = make_mock_client(b"FAIL\n", b"some error", status=1)
    ok, msg = s.stop_service(client, "nginx", None)
    assert not ok and "srv stop failed" in msg.lower()
