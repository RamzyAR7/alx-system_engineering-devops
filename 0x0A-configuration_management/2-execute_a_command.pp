#!/usr/bin/pup
# 2-execute_a_command.pp
# kill_process.pp

exec { 'Kill killmenow process':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}
