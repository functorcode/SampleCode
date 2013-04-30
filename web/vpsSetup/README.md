Just one script to install and optimize Nginx,mysql and php5 ,php-fpm  for 128/512Mb VPS/Cloud instance.

Download: svn co https://github.com/junedmunshi/SampleCode/trunk/web/vpsSetup

OS:

ubuntu 12.04 or later

Install and setup:

chmod +x vpsSetup.sh
chmod +x start.sh
chmod +x stop.sh
sudo ./vpsSetup.sh

To start server
sudo ./start.sh

To stop server
sudo ./stop.sh

Before you run the script:

	Before you blindly run the script, you should read look at configuration files for Nginx and tweak it according to your need. Read Nginx section below.Moreover, you can also change configuration for mysql and php if given configuration file does not suit to your need. Read Mysql and Php5 section below.



What will the script?
It will,
1) Add required debian repository

2) Install all required packeges ( nginx mysql-server mysql-client memcached php5 php-apc php-auth php-net-smtp php-net-socket php-pear php5-curl php5-gd php5-mcrypt php5-mysql php5-fpm php5-memcached php5-tidy vsftpd )

3) Take backup of orignal mysql configuration file. ( /etc/mysql/my.cnf -> /etc/mysql/my.cnf.org)

4) Optimize mysql by patching configuration file from ./mysql/my.cnf to /etc/mysql/my.cnf

5) Apply same step as 3 and 5 for nginx and php5


Nginx

1)nginx/default:
It is your web application configuration file. Current settings are configured for php, fast cgi and cakephp .

Things to check before you deploy:

-port
-servername : your domain name
-root : path to your website code
-access_log and error_log : very useful for debuging your website code (not nginx)
-location : control behaviour for specific locations such "/" or "*.js,*.css,*.jpg (any assests)"

Note:

	1) Following line is not required if you are not using cakephp. Following line ensure that images,css etc. will load properly without generating "path not found " error from theme/plugin.
	try_files $uri $uri/ /../plugins/$1/webroot/$2/$3 /../View/Themed/$2/webroot/$3/$4 ;

	2) You may want to turn of access_log and log_not_found for images,xml etc. files once your site functions properly.

2)ngnix.conf :

Blindly copied from http://www.axelsegebrecht.com/how-to/install-nginx-apc-varnish-wordpress-and-w3-cache-128mb-vps/#Configuring_nginx



PHP

1) php/fpm/php.ini:

The only difference between orignal and patch file is as below.
;cgi.fix_pathinfo=1 -> cgi.fix_pathinfo=0

2) php5/fpm/php-fpm.conf :
Blindly copied from http://www.axelsegebrecht.com/how-to/install-nginx-apc-varnish-wordpress-and-w3-cache-128mb-vps/#Configuring_PHP5-FPM

3) php5/fpm/pool.d/www.conf :
php_admin_value[memory_limit] = You can increase if you have more RAM
php_value[upload_max_filesize] = Change it otherwise leave it if you don't care
php_value[max_execution_time] = Change it otherwise leave it if you don't care
user = www-data
group = www-data








