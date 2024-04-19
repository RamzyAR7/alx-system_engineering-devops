#!/usr/bin/pup
# 2-execute_a_command.pp

# Use exec resource to kill the process named 'killmenow' using pkill
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin:/usr/local/bin', # Ensure pkill is in the path
  refreshonly => true, # Execute only when notified by another resource
}
