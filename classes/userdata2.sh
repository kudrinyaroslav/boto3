#!/bin/bash
sudo yum -y install httpd
sudo yum install -y mysql
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fsi_template.efs.eu-central-1.amazonaws.com:/ /var/www/html/
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
cd /home/ec2-user
sudo cp -r wordpress/* /var/www/html/
sudo service httpd start