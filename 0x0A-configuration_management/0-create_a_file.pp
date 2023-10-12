# creates a file

file { 'school':
  ensure  => 'file',
  content => 'I love Puppet',
  mode    => '0744',
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
}
