# 1-install_a_package.pp

# Install Flask package using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
