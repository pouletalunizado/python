import paramiko

ip='192.168.40.140'
port=22
username='root'
password='password'

cmd='ls' 

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

stdin,stdout,stderr=ssh.exec_command('comando')
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)