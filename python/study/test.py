import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname='10.50.253.12', port=22, username='root', password='yunshan3302')

stdin, stdout, stderr = client.exec_command('df -h ')

print(stdout.read().decode('utf-8'))

client.close()
