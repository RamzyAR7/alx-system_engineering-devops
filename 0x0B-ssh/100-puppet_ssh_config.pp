#!/usr/bin/env bash
#use puppet to connect to the remote server

file { '/etc/ssh/ssh_config':
  ensure  => present,
}
file{ 'Turn off password authentication':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#PasswordAuthentication',
}
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#IdentityFile',
}
