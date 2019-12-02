import os 
import subprocess
import docker 

client = docker.DockerClient("tcp://10.90.31.33:2375")

mycon2 = client.containers.run("con1_img",name="python_sdk_con2",tty=True, stderr=True, stdout=True,detach=True)
ip = mycon2.exec_run("awk 'END{print $1}' /etc/hosts")
print("Type of ip address variable is ",type(ip))
s = str(ip)
ip = s[33:-4]
print(ip)


