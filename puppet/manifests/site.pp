node 'default' {
    include users

    class { 'python':
      version    => 'system',
      dev        => true,
      pip        => true,
      virtualenv => true,
    }

    python::pip { 'docker-compose' :
      pkgname       => 'docker-compose',
      require => Class['python']
    }


    include 'docker'

}
