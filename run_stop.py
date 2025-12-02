from stop_services_oops import connect_ssh, stop_service
import getpass, paramiko

host="mymachine"; user="youruser"; key="~/.ssh/id_rsa"
# prompt for password if needed
pw = None
sudo_pw = None

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, key_filename=key)
ok, msg = stop_service(client, "firewalld", sudo_pw)
print("OK" if ok else "FAIL", msg)
client.close()
