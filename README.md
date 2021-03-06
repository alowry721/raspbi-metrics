
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
