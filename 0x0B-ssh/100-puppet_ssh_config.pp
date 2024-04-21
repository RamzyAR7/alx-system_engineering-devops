#!/usr/bin/env bash

# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure  => present,
}

# Turn off password authentication
file_line { 'Turn off password authentication':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?\s*PasswordAuthentication',
}

# Declare identity file
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?\s*IdentityFile',
}
