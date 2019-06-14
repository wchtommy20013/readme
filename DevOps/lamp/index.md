# LAMP (Linux, Apache, MySQL/MariaDB, PHP)

# Ubuntu / Debian

# CentOS 7 / RedHat 
```bash
# Yum update
yum update -y
yum install yum-utils -y
yum install epel-release -y
yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm -y 

# Utils
yum install wget -y
yum install zip unzip -y

# Apache
yum install httpd -y
service httpd start

# MariaDB (MySQL)
yum install mariadb mariadb-server -y
service mariadb start
/usr/bin/mysql_secure_installation

# PHP
yum-config-manager --disable remi-php54
yum-config-manager --enable remi-php73
yum install php -y

yum install php-fpm php-mysql php-curl php-gd php-mbstring php-xml php-xmlrpc php-zip php-opcache -y

service httpd restart
echo "<?php phpinfo();?>" | php


# Default Service On
chkconfig httpd on
chkconfig mariadb on


# Firewall Setting
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent
firewall-cmd --list-all --permanent
service firewalld restart

# PhpMyAdmin
sudo yum install phpmyadmin -y
vi /etc/httpd/conf.d/phpMyAdmin.conf
    # <RequireAny>
    #   Require ip 127.0.0.1
    #   Require ip ::1
    #   Require ip <your IP>
    #</RequireAny>

service httpd restart


# Configure Swap Memory
free -m
sudo dd if=/dev/zero of=/swapfile count=4096 bs=1MiB
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
free -m

echo "/swapfile   swap    swap    sw  0   0" >> /etc/fstab
sudo sysctl vm.swappiness=10

echo "vm.swappiness = 10" >> /etc/sysctl.conf
echo "vm.vfs_cache_pressure = 50" >> /etc/sysctl.conf


```