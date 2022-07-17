import paramiko
import pandas as pd
import umbrel_secrets

host = umbrel_secrets.host
port = umbrel_secrets.port
username = umbrel_secrets.username
password = umbrel_secrets.password

command = "docker exec bitcoin_bitcoind_1 bitcoin-cli gettxoutsetinfo"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)


stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()


print(lines)

df = pd.DataFrame(lines)

df.to_csv('supply.csv')

Print("Complete!")
del stdin
