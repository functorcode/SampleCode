BASEDIR=$(readlink -f $0 | xargs dirname)
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:nginx/php5

apt-get update && apt-get upgrade
apt-get install  iptables curl
apt-get install libssl0.9.8
apt-get install nginx mysql-server mysql-client memcached php5 php-apc php-auth php-net-smtp php-net-socket php-pear php5-curl php5-gd php5-mcrypt php5-mysql php5-fpm php5-memcached php5-tidy vsftpd
echo "configuring mysql.."
mv /etc/mysql/my.cnf /etc/mysql/my.cnf.org
cp $BASEDIR/mysql/my.cnf /etc/mysql/my.cnf

echo "configuring nginx.."
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.org
cp $BASEDIR/nginx/nginx.conf /etc/nginx/nginx.conf
mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.org 
cp $BASEDIR/nginx/default /etc/nginx/sites-available/default

echo "configuring php-fpm.."
mv /etc/php5/fpm/php.ini /etc/php5/fpm/php.ini.org
cp $BASEDIR/php5/fpm/php.ini /etc/php5/fpm/php.ini 
mv /etc/php5/fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf.org
cp $BASEDIR/php5/fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf 
mv /etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf.org
cp $BASEDIR/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf

echo "Done.your server is ready for hosting.Run start.sh to start"



