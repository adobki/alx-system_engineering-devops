#!/usr/bin/env bash
# Configure Nginx to meet ALX web server requirement with a custom HTTP header X-Served-By.

# Update packages and install Nginx if necessary
sudo apt update
sudo apt install -y nginx

# Create pages for default route and 404 error
mkdir -p /var/www/html
echo "Holberton School" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/404.html

# Edit default server to meet ALX web server requirements
sudo chmod 666 /etc/nginx/sites-available/default
printf %s "server{
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;

	location /redirect_me {
		return 301 https://anagrammaster.onrender.com;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}
" > /etc/nginx/sites-available/default
sudo chmod 644 /etc/nginx/sites-available/default

# Check for syntax errors and restart service if none
sudo nginx -t && sudo service nginx restart
