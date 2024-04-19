#!/usr/bin/pup
# 2-execute_a_command.pp
# kill_process.pp

exec { 'Kill a process':
  command => 'pkill killmenow',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
