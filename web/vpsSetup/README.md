Just one script to install and optimize Nginx,mysql and php5 ,php-fpm  for 128/512Mb VPS/Cloud instance.

<h4> Download  </h4>  svn co https://github.com/junedmunshi/SampleCode/trunk/web/vpsSetup

<h4> OS </h4>

Tested on vanilla ubuntu 12.04 .

<h4> Install and setup </h4>

chmod +x vpsSetup.sh

chmod +x start.sh

chmod +x stop.sh

sudo ./vpsSetup.sh

<h4> To start server </h4> 
sudo ./start.sh

<h4> To stop server </h4> 
sudo ./stop.sh

<h4>But before you run the script </h4>
   _Before you blindly run the script, you should look at configuration files for Nginx and modify it according to your need._ __Everything should work off the shelf except modifying few parameters in ./nginx/default .__ _Read Nginx section below._
   
  _Moreover, you can also change configuration for mysql and php if given configuration file does not suit to your need.Read Mysql and Php5 section below._


<h4> What will the script do? </h4>
It will,

	1) Add required debian repository
	
	2) Install all required packeges ( nginx mysql-server mysql-client memcached php5 php-apc php-auth php-net-smtp php-net-socket php-pear php5-curl php5-gd php5-mcrypt php5-mysql php5-fpm php5-memcached php5-tidy vsftpd )
	
	3) Take backup of orignal mysql configuration file. ( /etc/mysql/my.cnf -> /etc/mysql/my.cnf.org)
	
	4) Optimize mysql by patching configuration file from ./mysql/my.cnf to /etc/mysql/my.cnf
	
	5) Apply same step as 3 and 5 for nginx and php5
<h4> Files Detail </h4>
* vpsSetup.sh   : Installation script    
* mysql/my.cnf  : MySQL server configuration file tunned for 512Mb server running mysql and nginx
* nginx/nginx.conf : Nginx server configuration file tunned for 512Mb server running mysql and nginx
* nginx/default :  Configuration file for your web application.It will patched to /etc/nginx/sites-available .
* php5/fmp/php.ini : See the php section below
* php5/fmp/php-fpm.conf : See the php section below
* php5/fpm/pool.d/www.conf : Tunned for 512Mb server.   

<h4> If services do not start after applying optimal settings </h4>  
1. If Nginx does not start , it may be possible that there is something wrong with either /etc/nginx/ngnix.conf or site-available/default.  
Run _sudo service nginx start_ and look for error.  
2. If MySQL does not start , please check MySQL troubleshoot guide.[http://junedmunshiblog.blogspot.in/2013/05/troubleshooting-mysql.html](http://junedmunshiblog.blogspot.in/2013/05/troubleshooting-mysql.html)


<h4> Nginx </h4>

<h5>1)nginx/default </h5>
It is your web application configuration file. Current settings are configured for php, fast cgi and cakephp .

Things to check before you deploy:


	port   
	servername : your domain name   
	root : path to your website code 
	access_log and error_log : very useful for debuging your website code (not nginx) 
	location : control behaviour for specific locations such "/" or "*.js,*.css,*.jpg (any assests)" 

Note:

1) Following line is not required if you are not using cakephp. Following line ensure that images,css etc. will load properly without generating "path not found " error from theme/plugin.

	try_files $uri $uri/ /../plugins/$1/webroot/$2/$3 /../View/Themed/$2/webroot/$3/$4 ;

Ref: http://lennaert.nu/2011/01/21/cakephp-performance-rewrite-plugin-assets-in-nginx/	

2) You may want to turn of access_log and log_not_found for images,xml etc. files once your site functions properly.

<h5>2)ngnix.conf </h5>
Blindly copied from http://www.axelsegebrecht.com/how-to/install-nginx-apc-varnish-wordpress-and-w3-cache-128mb-vps/#Configuring_nginx

<h4> MySQL </h4>
<h5> my.cnf </h5>

1 You may consider further tunning following paramters under '[mysqld]' section if current settings are not best fit for you.   
       
       
       key_buffer = 16K  	 (Default is 16M)   
       max_allowed_packet = 1M  (Default is 16M)    
       thread_stack = 64K    	 (Default is 192K)   
       thread_cache_size  = 4	 (Default is 8)   

2 Innodb
    
    
      Disable if not needed.Uncomment #skip-innodb
2 Fine tune if you are using it.
       
       
       innodb_buffer_pool_size = 16M  	     (Default is 128M)  
       innodb_additional_mem_pool_size = 2M   



<h4>PHP </h4>

<h5>1) ./php5/fpm/php.ini </h5>

The only difference between orignal and patch file is as below.

    ;cgi.fix_pathinfo=1 -> cgi.fix_pathinfo=0

<h5>2) php5/fpm/php-fpm.conf </h5>
Blindly copied from http://www.axelsegebrecht.com/how-to/install-nginx-apc-varnish-wordpress-and-w3-cache-128mb-vps/#Configuring_PHP5-FPM

<h5>3) php5/fpm/pool.d/www.conf </h5>


 	php_admin_value[memory_limit] = You can increase if you have more RAM
	php_value[upload_max_filesize] = Change it otherwise leave it if you don't care
	php_value[max_execution_time] = Change it otherwise leave it if you don't care
	user = www-data 
	group = www-data  
</ul>








