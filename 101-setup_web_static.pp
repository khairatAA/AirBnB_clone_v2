# Install Nginx if it not already installed
exec { 'apt-get update':
  path => '/usr/bin:/bin',
}

package { 'nginx':
  ensure => installed,
}

# Create the folder /data/ if it doesn’t already exist
user { 'ubuntu':
  ensure => present,
}

group { 'ubuntu':
  ensure => present,
}

file { '/data/':
  ensure => directory,
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
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

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static

# Add the location configuration to the Nginx.
$location='\n\tlocation /hbnb_static {\n\
        \talias /data/web_static/current/;\n\
        }'
exec { 'edit_config_file':
  command => "sudo sed -i '/server_name _;/a \\ ${location}' /etc/nginx/sites-available/default",
  path    => '/usr/bin:/bin',
}

exec { 'restart_Nginx':
  command => 'sudo service nginx restart > /dev/null',
  path    => '/usr/bin:/bin',
}
