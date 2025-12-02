#!/usr/bin/env python3
"""
Testable refactor of the 'oops' script. Exposes small functions for unit testing.
Requires paramiko.
"""
import getpass
from typing import Tuple, Optional
import paramiko

def escape_for_echo(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "'\"'\"'")

def make_stop_cmd(service: str) -> str:
    return f"systemctl stop {service} && echo OK || echo FAIL"

def make_sudo_stop_cmd(service: str, sudo_pass: Optional[str]) -> str:
    if sudo_pass is None:
        return f"sudo systemctl stop {service} && echo OK || echo FAIL"
    return f"echo {escape_for_echo(sudo_pass)} | sudo -S systemctl stop {service} && echo OK || echo FAIL"

def run_cmd(client: paramiko.SSHClient, cmd: str, timeout: float = 15.0) -> Tuple[int, str, str]:
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode(errors="ignore")
    err = stderr.read().decode(errors="ignore")
    exit_status = stdout.channel.recv_exit_status()
    return exit_status, out.strip(), err.strip()

def parse_stop_result(out: str, err: str) -> Tuple[bool, str]:
    # Returns (success, reason)
    if "OK" in out:
        return True, "stopped"
    if "permission denied" in (err.lower() + out.lower()):
        return False, "permission denied"
    return False, err or out or "unknown"

def stop_service(client: paramiko.SSHClient, service: str, sudo_pass: Optional[str], timeout: float = 15.0) -> Tuple[bool, str]:
    code, out, err = run_cmd(client, make_stop_cmd(service), timeout)
    ok, reason = parse_stop_result(out, err)
    if ok:
        return True, "stopped (no sudo)"
    # Try sudo
    code2, out2, err2 = run_cmd(client, make_sudo_stop_cmd(service, sudo_pass), timeout)
    ok2, reason2 = parse_stop_result(out2, err2)
    if ok2:
        return True, "stopped (sudo)"
    return False, f"srv stop failed: {reason2}"

# Minimal CLI left out for brevity (keep main in separate module if desired)
if __name__ == "__main__":
    print("Run tests with pytest; this module focuses on testable functions.")
