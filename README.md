
# add necessary ubuntu packages

## install mariadb


## set up environment 
 sql
### add user

### add database


### setup tables


# add myphpadmin
Taken from https://pimylifeup.com/raspberry-pi-phpmyadmin/

## Set apache as server
### Edit phpmyadmin conf file
_Include PHPMyAdmin’s configuration and allow it to be loaded in and listened to by Apache._

`Include /etc/phpmyadmin/apache.conf`

### Restart apache2 

`sudo service apache2 restart`

# Add config on host

### Add cronjob to run
`cron -e`
Use crontab guru to set correct format for how often you want job to run
`PYTHONPATH=/home/$USER/metrics /home/$USER/py3_venv/bin/python -m main` 

# add snmp
## download
`sudo apt-get install snmp-mibs-downloader
sudo download-mibs`

## modify conf files
### on local server
We want to enable loading of MIBs by default.  We do this by modifying:

`sudo nano /etc/snmp/snmp.conf`

And adding the line:

`mibs +ALL`


### on remote server
This is for pulling snmp from a remote server.  We want to modify the SNMP daemon running in background.

`sudo nano /etc/snmp/snmpd.conf`

comment out the following:

`agentAddress  udp:127.0.0.1:161`

add the following:

`agentAddress udp:161`

restart the dameon

`sudo service snmpd restart`