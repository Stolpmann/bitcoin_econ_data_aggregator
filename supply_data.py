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

supply_df.to_csv('csv/supply.csv')

del stdin


# Get chain tx stats

chain_stats_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli getchaintxstats"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(chain_stats_command)
chain_stats = stdout.readlines()

print(chain_stats)
chain_stats_df = pd.DataFrame(chain_stats)

chain_stats_df.to_csv('csv/chain_stats.csv')


del stdin


# Get difficulty

difficulty_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli getdifficulty"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(difficulty_command)
difficulty = stdout.readlines()

print(difficulty)
difficulty_df = pd.DataFrame(difficulty)

difficulty_df.to_csv('csv/difficulty.csv')


del stdin


# Get mining info

mining_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli getmininginfo"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(mining_command)
mining = stdout.readlines()

print(mining)
mining_df = pd.DataFrame(mining)

mining_df.to_csv('csv/mining.csv')


del stdin



# Get mempool info

mempool_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli getmempoolinfo"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(mempool_command)
mempool = stdout.readlines()

print(mempool)
mempool_df = pd.DataFrame(mempool)

mempool_df.to_csv('csv/mempool.csv')


del stdin

horizontal_stack = pd.concat([mempool_df, hashps_df, mining_df, chain_size_df, difficulty_df, chain_stats_df, supply_df], axis=1)

horizontal_stack.to_excel('supply.xlsx')

print("Complete!")