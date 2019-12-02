import os 
import docker 
import paramiko
import sys
import time 
import os.path
client = docker.DockerClient("tcp://10.90.31.33:2375")

mycon2 = client.containers.run("host_ssh_img",name="python_sdk_con2",tty=True, stderr=True, stdout=True,detach=True)
ip = mycon2.exec_run("awk 'END{print $1}' /etc/hosts")
mycon2.exec_run("./test.sh")
mycon2.exec_run("service ssh start")
print("Type of ip address variable is ",type(ip))
s = str(ip)
ip = s[33:-4]
print(ip)


class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass


passwd = "root"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # ssh.connect("10.90.31.162", "root", password=passwd)
ssh.connect(ip, username="root", password=passwd)

channel = ssh.get_transport().open_session()
channel.get_pty()
channel.invoke_shell()
command_list =set()
print(type(command_list))

while True:
    try:
        command = input('$ ')
        command_list.add(command)


        if command == 'exit':
            break
        if command == 'nano':
            print("You can't use nano ")
            continue
            raise ValueTooLargeError
    except:
       if command in command_list:
           print("Press enter to continue")
           continue  


    channel.send(command + "\n")

    while True:
        if channel.recv_ready():
            output = channel.recv(1024)
            print(output.decode("utf-8"))
        else:
            time.sleep(0.5)
            if not(channel.recv_ready()):
                break

ssh.close()