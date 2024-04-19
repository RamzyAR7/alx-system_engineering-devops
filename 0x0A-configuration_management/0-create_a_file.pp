# 0-create_a_file.pp

# Ensure the directory exists
file { '/tmp':
  ensure => 'directory',
}

# Create the file with specified permissions, owner, and group
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
