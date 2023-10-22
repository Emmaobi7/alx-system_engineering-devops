# Accept lots of http requests

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/15/5000/" /etc/default/nginx',
  before   => Exec['restart-nginx'],
}

exec {'restart-nginx':
  provider => shell,
  command  => 'service nginx restart',
}
