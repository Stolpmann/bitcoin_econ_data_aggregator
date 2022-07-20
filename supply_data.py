import paramiko
import pandas as pd
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

supply_df.to_excel('supply.xlsx')

del stdin


# Best Block Hash

best_block_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli getbestblockhash"

stdin, stdout, stderr = ssh.exec_command(best_block_command)
best_block_hash = stdout.readlines()

print(best_block_hash)
best_block_df = pd.DataFrame(best_block_hash)


del stdin

# Get Block Hash

get_block_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli getblockhash"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(get_block_command)
get_block_hash = stdout.readlines()

print(get_block_hash)
get_block_df = pd.DataFrame(get_block_hash)

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

del stdin


# Get chain size in bytes

chain_size_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli getmemoryinfo"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(chain_size_command)
chain_size = stdout.readlines()

print(chain_size)
chain_size_df = pd.DataFrame(chain_size)

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

del stdin


# Get Network Hash per second

hashps_command = "docker exec bitcoin_bitcoind_1 bitcoin-cli getnetworkhashps -1"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(hashps_command)
hashps = stdout.readlines()

print(hashps)
hashps_df = pd.DataFrame(hashps)

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

del stdin

horizontal_stack = pd.concat([mempool_df, hashps_df, mining_df, chain_size_df, difficulty_df, chain_stats_df, supply_df], axis=1)


horizontal_stack.to_excel('supply.xlsx')

print("Complete!")