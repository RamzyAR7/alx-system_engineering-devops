# 1-install_werzeug.pp
# Install the werzeug package using pip3
package { 'werzeug':
  ensure   => 'latest',
  provider => 'pip3',
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
