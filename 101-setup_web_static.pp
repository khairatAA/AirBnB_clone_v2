# sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
package { 'nginx':
  ensure => installed,
}

# Create the folder /data/ if it doesn’t already exist
file { '/data/':
  ensure => directory,
}

# Create the folder /data/web_static/ if it doesn’t already exist
file { '/data/web_static/':
  ensure => directory,
}

# Create the folder /data/web_static/releases/ if it doesn’t already exist
file { '/data/web_static/releases/':
  ensure => directory,
}

# Create the folder /data/web_static/shared/ if it doesn’t already exist
file { '/data/web_static/shared/':
  ensure => directory,
}

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
file { '/data/web_static/releases/test/':
  ensure => directory,
}

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
file { '/data/web_static/releases/test/index.html':
  ensure => file,
}

file { '/data/web_static/releases/test/index.html':
  content => '<html>
                <head></head>
                <body>
                    <h1>Testing Nginx configuration</h1>
                </body>
            </html>',
}

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
}

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
file { '/data/':
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static

# Add the location configuration to the Nginx
$CONF_PATH='/etc/nginx/sites-enabled/default'

file_line { 'add_hbnb_static_location':
  ensure => present,
  path   => $CONF_PATH,
  line   => '        location /hbnb_static/ {',
  after  => '        listen 80 default_server;',
}

file_line { 'add_alias_to_location':
  ensure => present,
  path   => $CONF_PATH,
  line   => '            alias /data/web_static/current/;',
  after  => '        location /hbnb_static/ {',
}

exec {
  commad  => 'service nginx restart'
}
