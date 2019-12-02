FROM python:slim
RUN apt-get update
RUN pip3 install flask
RUN pip3 install docker
RUN apt -y install openssh-server
RUN pip3 install paramiko
WORKDIR  /for_ssh
COPY  . /for_ssh
# RUN chmod +x test2.sh 
# RUN ./test2.sh
EXPOSE  5005 22
# CMD [ "python3","flask4_ssh.py" ]
CMD [ "python3", "final_ssh_4_k8s.py" ]
