#!/bin/bash

#This script copies the server directory to an archive directory

#You need to create a ssh key to use this script
#To create an ssh key, bash these two lines:
#ssh-keygen -t rsa
#ssh-copy-id -i ~/.ssh/id_rsa.pub user@serveraddress

user="pubmark"
address="66.66.103.33"
endDir="/var/www"


echo "archiving the apache server contents..."

date=$(date +%Y%m%d%H)
$(ssh $user@$address cp -r /var/www/ /home/pubmark/www-archive$date)

exit 0
