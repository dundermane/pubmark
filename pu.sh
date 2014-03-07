#!/bin/bash

#This script copies this directory to a directory on another computer
#Warning, this also deletes whatever is on the servers directory
#sta.sh before using!

#You need to create a ssh key to use this script
#To create an ssh key, bash these two lines:
#ssh-keygen -t rsa
#ssh-copy-id -i ~/.ssh/id_rsa.pub user@serveraddress

user="pubmark"
address="66.66.103.33"
endDir="/var/www"


echo "clearing server directory..."
$(ssh $user@$address 'cd /var/www/ && rm -r *')

echo "Uploading current directory..."
$(scp -r . $user@$address:/var/www/)

exit 0
