#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
if ! command -v nginx &> /dev/null; then
	apt-get update
	apt install nginx -y
fi

# Create the folder /data/ if it doesn’t already exist
if ! [ -d "/data/" ]; then
	mkdir "/data/"
fi

# Create the folder /data/web_static/ if it doesn’t already exist
if ! [ -d "/data/web_static/" ]; then
        mkdir "/data/web_static/"
fi

# Create the folder /data/web_static/releases/ if it doesn’t already exist
if ! [ -d "/data/web_static/releases/" ]; then
        mkdir "/data/web_static/releases/"
fi

# Create the folder /data/web_static/shared/ if it doesn’t already exist
if ! [ -d "/data/web_static/shared/" ]; then
        mkdir "/data/web_static/shared/"
fi

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
if ! [ -d "/data/web_static/releases/test/" ]; then
        mkdir "/data/web_static/releases/test/"
fi

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
content="
<html>
<head>
</head>
<body>
	<h1>Testing Nginx configuration</h1>
</body>
</html>"

echo "$content" > "/data/web_static/releases/test/index.html"

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.

if [ -L "/data/web_static/current" ]; then
        rm  "/data/web_static/current"
fi

ln -s "/data/web_static/releases/test/" "/data/web_static/current"

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
chown -R "ubuntu":"ubuntu" "/data/"

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static

location_config='
    location /hbnb_static {
        alias /data/web_static/current/;
    }
'

# Path to your Nginx configuration file
nginx_config="/etc/nginx/sites-available/default"

# Add the location configuration to the Nginx file
if ! grep -q "$location_config" "$nginx_config"; then
        sudo bash -c "cat <<EOF >>$nginx_config

$location_config
EOF"
fi

service nginx restart
