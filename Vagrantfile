# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.network "public_network"
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python3-pip unzip gnome-core xinit libxss1 fonts-liberation libappindicator1 xdg-utils
    sudo apt-get -f install
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
    sudo pip3 install selenium
    wget http://chromedriver.storage.googleapis.com/2.22/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    sudo cp chromedriver /usr/local/bin/
  SHELL
  config.vm.provider :virtualbox do |vb|
    vb.gui = true
  end
end
