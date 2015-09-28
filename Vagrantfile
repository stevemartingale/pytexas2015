# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "Ubuntu-14.04_64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.hostname = "buzzwords.vm"
  config.vm.network :private_network, ip: "192.167.39.39"

  # VirtualBox Specific Customization
  config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "4096"]
        vb.customize ["modifyvm", :id, "--cpus", "4"]
  end

  # Enable shell provisioning to bootstrap puppet

  config.vm.provision :shell, :path => "bootstrap.sh"

  config.vm.provision :shell do |shell|
    shell.inline = "/usr/bin/apt-get update"
  end

  # Enable provisioning with Puppet stand alone.
  config.vm.provision :puppet do |puppet|
          puppet.manifests_path = "puppet/manifests"
          puppet.manifest_file  = "site.pp"
          puppet.module_path = "puppet/modules"
          puppet.options = "--verbose --debug"
  end 

end