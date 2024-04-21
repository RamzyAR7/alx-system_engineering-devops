file { '/etc/ssh/ssh_config':
  ensure  => present,
  content =>
    "${file('/etc/ssh/ssh_config')}Host web-01
        HostName 54.237.93.225
        ServerAliveInterval 120
        IdentityFile ~/.ssh/school
        PasswordAuthentication no",
  owner   => 'itsfoss',
  group   => 'itsfoss',
  mode    => '0744'
}
