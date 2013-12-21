echo "installing postgresql-server and postgis "
sudo apt-get install postgresql-server-dev-9.1 postgresql-9.1-postgis
echo "verify installation"
sudo -u postgres psql -l
echo "downloading django postgis template script"
wget https://docs.djangoproject.com/en/dev/_downloads/create_template_postgis-1.5.sh
echo "executing script"
chmod +x create_template_postgis-1.5.sh
sudo -u postgres ./create_template_postgis-1.5.sh
echo "installing psycopg2"
pip install psycopg2
echo "Execute following command to create db and user."
echo "CREATE DATABASE sample_db TEMPLATE template_postgis;"
echo "CREATE ROLE sample_role WITH PASSWORD 'sample_password' LOGIN;"
echo "GRANT ALL PRIVILEGES ON DATABASE sample_db to sample_role;"
echo "ALTER ROLE sample_role CREATEDB;"




