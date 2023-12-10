# sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
exec { 'apt-get update':
  path => '/usr/bin:/bin',
}

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
  content => '<html>
  <head></head>
  <body>
    <h1>Testing Nginx configuration</h1>
  </body>
            </html>',
  mode    => '0644',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
exec { 'ln -sfn /data/web_static/releases/test/ /data/web_static/current':
  path => ['/usr/bin', '/bin'],
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static

# Add the location configuration to the Nginx
$conf_path='/etc/nginx/sites-enabled/default'

file_line { 'add_hbnb_static_location':
  ensure => present,
  path   => $conf_path,
  line   => '        location /hbnb_static/ {',
  after  => '        listen 80 default_server;',
}

file_line { 'add_alias_to_location':
  ensure => present,
  path   => $conf_path,
  line   => '            alias /data/web_static/current/;',
  after  => '        location /hbnb_static/ {',
}

exec { 'restart_nginx':
  command  => '/usr/sbin/service nginx restart'
}
