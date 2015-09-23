REQUIRED_PLUGINS = [
  "vagrant-docker-compose",
  "vagrant-exec",
]
uninstalled_required_plugins = REQUIRED_PLUGINS.reject(&Vagrant.method(:has_plugin?))
if ! uninstalled_required_plugins.empty? && ARGV.first != "plugin"
  exec "vagrant plugin install '#{uninstalled_required_plugins.join("' '")}' && vagrant '#{ARGV.join("' '")}'"
end

if ["up", "exec"].include?(ARGV.first)
  puts "IMPORTANT: You should run `vagrant rsync-auto' on a separate terminal to enable auto-reloading features."
end

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 4000, host: 4000

  config.vm.synced_folder ".", "/vagrant",
                          type: "rsync",
                          rsync__exclude: ".git/"

  config.vm.provision :docker
  config.vm.provision :docker_compose
  config.vm.provision "shell", inline: "echo 'cd /vagrant' >> .bashrc"
end
