Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :forwarded_port, guest: 4000, host: 4000

  config.vm.provision :docker
  config.vm.provision :docker_compose
  config.vm.provision "shell", inline: "echo 'cd /vagrant' >> .bashrc"
end
