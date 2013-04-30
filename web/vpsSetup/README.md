Just one script to install and optimize Nginx,mysql and php5 ,php-fpm  for 128/512Mb VPS/Cloud instance.

<h4> Download  </h4>  svn co https://github.com/junedmunshi/SampleCode/trunk/web/vpsSetup

<h4> OS required </h4>

ubuntu 12.04 or later

<h4> Install and setup </h4>

chmod +x vpsSetup.sh
chmod +x start.sh
chmod +x stop.sh
sudo ./vpsSetup.sh

<h4> To start server </h4> 
sudo ./start.sh

<h4> To stop server </h4> 
sudo ./stop.sh

<h4>Before you run the script </h4>

	Before you blindly run the script, you should read look at configuration files for Nginx and tweak it according to your need. Read Nginx section below.Moreover, you can also change configuration for mysql and php if given configuration file does not suit to your need. Read Mysql and Php5 section below.



<h4> What will the script do? </h4>
It will,

	1) Add required debian repository
	
	2) Install all required packeges ( nginx mysql-server mysql-client memcached php5 php-apc php-auth php-net-smtp php-net-socket php-pear php5-curl php5-gd php5-mcrypt php5-mysql php5-fpm php5-memcached php5-tidy vsftpd )
	
	3) Take backup of orignal mysql configuration file. ( /etc/mysql/my.cnf -> /etc/mysql/my.cnf.org)
	
	4) Optimize mysql by patching configuration file from ./mysql/my.cnf to /etc/mysql/my.cnf
	
	5) Apply same step as 3 and 5 for nginx and php5


<h4> Nginx </h4>

<h5>1)nginx/default </h5>
It is your web application configuration file. Current settings are configured for php, fast cgi and cakephp .

Things to check before you deploy:
<ul>

<li>port</li>   
<li>servername : your domain name </li>
<li>root : path to your website code </li>
<li>access_log and error_log : very useful for debuging your website code (not nginx) </li>
<li>location : control behaviour for specific locations such "/" or "*.js,*.css,*.jpg (any assests)" </li>
</ul>
Note:

1) Following line is not required if you are not using cakephp. Following line ensure that images,css etc. will load properly without generating "path not found " error from theme/plugin.
	try_files $uri $uri/ /../plugins/$1/webroot/$2/$3 /../View/Themed/$2/webroot/$3/$4 ;
	
2) You may want to turn of access_log and log_not_found for images,xml etc. files once your site functions properly.

<h5>2)ngnix.conf </h5>
Blindly copied from http://www.axelsegebrecht.com/how-to/install-nginx-apc-varnish-wordpress-and-w3-cache-128mb-vps/#Configuring_nginx



<h4>PHP </h4>

<h5>1) php/fpm/php.ini </h5>

The only difference between orignal and patch file is as below.

;cgi.fix_pathinfo=1 -> cgi.fix_pathinfo=0

<h5>2) php5/fpm/php-fpm.conf </h5>
Blindly copied from http://www.axelsegebrecht.com/how-to/install-nginx-apc-varnish-wordpress-and-w3-cache-128mb-vps/#Configuring_PHP5-FPM

<h5>3) php5/fpm/pool.d/www.conf </h5>
<ul>
<li>php_admin_value[memory_limit] = You can increase if you have more RAM </li>
<li>php_value[upload_max_filesize] = Change it otherwise leave it if you don't care </li>
<li>php_value[max_execution_time] = Change it otherwise leave it if you don't care </li>
<li>user = www-data </li>
<li>group = www-data  </li>
</ul>








