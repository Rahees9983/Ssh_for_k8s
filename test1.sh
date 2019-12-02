#!/bin/bash
echo -e "root\nroot" | passwd root
# echo "PermitRootLogin yes" | cat >> /etc/ssh/sshd_config
service ssh start &