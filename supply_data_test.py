import paramiko
import pandas as pd
import numpy as np
import umbrel_secrets


host = umbrel_secrets.host
port = umbrel_secrets.port
username = umbrel_secrets.username
password = umbrel_secrets.password


# Transaction Outset Info

supply_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli gettxoutsetinfo"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(supply_command)
supply = stdout.readlines()

print(supply)

supply_df = pd.DataFrame(supply)

supply_df.to_excel('supply.csv')

del stdin