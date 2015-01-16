# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provision :shell, :path => "provision.sh"

  config.vm.provision "docker" do |d|
    d.pull_images "java:openjdk-7-jre"
    d.pull_images "tomcat:7"
  end

  # The Karma user home folder, has to be mounted as /karma for `docker run`
  config.vm.synced_folder "./karma", "/karma"
  
  # Sample data (Models and CSV)
  config.vm.synced_folder "./data", "/data"

  config.vm.provider "virtualbox" do |vb|
    # Lots of RAM is needed to run Karma
    vb.customize ["modifyvm", :id, "--memory", "6144"]
  end

end
