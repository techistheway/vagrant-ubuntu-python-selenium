# vagrant-ubuntu-python-selenium
VagrantFile to launch the minimal environment for a Python Selenium testing environment.

# Usage


git clone https://

cd vagrant-ubuntu-python-selenium

vagrant init;vagrant up

# SSH Forwarding tips

#Local Port Forward:

If you want to access a port hosted on the guest from the host, use a local port forward.


vagrant ssh -- L3000:localhost:3000 L4000:localhost:4000 

-L [bind_address:]port:host:hostport

-L [bind_address:]port:remote_socket

-L local_socket:host:hostport

-L local_socket:remote_socket


# Remote Port Forward

If you want to access a port hosted on the host from the guest, use a remote port forward.


vagrant ssh -- -R4000:localhost:4000 -R5000:localhost:5000

-R [bind_address:]port:host:hostport

-R [bind_address:]port:local_socket

-R remote_socket:host:hostport

-R remote_socket:local_socket
