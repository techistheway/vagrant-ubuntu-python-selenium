Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "public_network"
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y xvfb python3-pip gconf-service libgconf-2-4 libgtk2.0-0 libnspr4 libnss3 libxss1 fonts-liberation libappindicator1 libpango1.0-0 xdg-utils unzip
    sudo apt-get -f install
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb --quiet
    sudo dpkg -i google-chrome-stable_current_amd64.deb
    sudo pip3 install selenium
    wget "http://chromedriver.storage.googleapis.com/$(curl "http://chromedriver.storage.googleapis.com/LATEST_RELEASE")/chromedriver_linux64.zip" --quiet
    unzip chromedriver_linux64.zip
    sudo cp chromedriver /usr/local/bin/
    sudo cp /vagrant/xvfb /etc/init.d/
    sudo chmod +x /etc/init.d/xvfb
    sudo update-rc.d xvfb defaults
    sudo service xvfb start
    echo "export DISPLAY=:1" >> /home/vagrant/.bashrc
  SHELL
end
