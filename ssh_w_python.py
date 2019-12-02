import docker 
import paramiko
import sys
import os
import time 
import os.path



client = docker.DockerClient("tcp://10.90.31.33:2375")
mycon2 = client.containers.run("con1_img",name="python_sdk_con2",tty=True, stderr=True, stdout=True,detach=True)

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
# our main program
# user guesses a number until he/she gets it right
# you need to guess this number
number = 10

passwd = "gslab@123"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # ssh.connect("10.90.31.162", "root", password=passwd)
ssh.connect("10.90.31.33", username="gslab", password=passwd)

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


# while True:
#    try:
#        i_num = int(input("Enter a number: "))
#        if i_num < number:
#            raise ValueTooSmallError
#        elif i_num > number:
#            raise ValueTooLargeError
#        break
#    except ValueTooSmallError:
#        print("This value is too small, try again!")
#        print()
#    except ValueTooLargeError:
#        print("This value is too large, try again!")
#        print()
# print("Congratulations! You guessed it correctly.")