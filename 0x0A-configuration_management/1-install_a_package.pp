# 1-install_werzeug.pp

# Install the werzeug package using pip3
package { 'werzeug':
  ensure   => 'latest',
  provider => 'pip3',
}
