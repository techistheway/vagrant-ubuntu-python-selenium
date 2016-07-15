# vagrant-ubuntu-python-selenium
Vagrantfile to launch the minimal environment for a Python Selenium(chromedriver) testing environment on Ubuntu. This is not a Selenium server, but a minimal execution environment to run Python3 selenium tests.

Tests run through Xvfb, so using the console window isn't needed, tests can be ran entirely from the command line. Yes, even screenshots. No more screen changes taking your OS focus away.

# Usage

* Prepare the VM

```
git clone https://github.com/techistheway/vagrant-ubuntu-python-selenium
cd vagrant-ubuntu-python-selenium
vagrant up
vagrant ssh
```


* Run your selenium scripts

```
vagrant@vagrant-ubuntu-trusty-64:~$ /vagrant/example.py
Found Google!
```

# SSH Forwarding tips

Sometimes you want to access a host behind hops on the network, you can use remote port forwarding.

Note: If you use domain names instead of IPs, you're asking for trouble.

# Remote Port Forward

If you want to access a port hosted on the host from the guest, use a remote port forward.

```
vagrant ssh -- -R4000:10.0.0.1:4000 -R5000:10.0.0.1:5000
-R [bind_address:]port:host:hostport
-R [bind_address:]port:local_socket
-R remote_socket:host:hostport
-R remote_socket:local_socket
```

# Local Port Forward

If you want to access a port hosted on the guest from the host, use a local port forward.

```
vagrant ssh -- -L3000:localhost:3000 -L4000:localhost:4000
-L [bind_address:]port:host:hostport
-L [bind_address:]port:remote_socket
-L local_socket:host:hostport
-L local_socket:remote_socket
```

# Screenshots for long pages

chromedriver's handling of screenshots only captures what's in the browser's viewport. This function will scroll the page down until the end, taking one screenshot per scroll.

Note that there will be some overlap on the last page. This can be handled, but I didn't for my use case.

```
def screenshot(page,name):
    if page is not None: # if you supply None, it will screenshot the current viewport. Useful for non-url page changes.
        driver.get(page)
    time.sleep(1)
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")

    viewport_width = driver.execute_script("return document.body.clientWidth")
    viewport_height = driver.execute_script("return window.innerHeight")

    if total_height / viewport_height > 1 :
        passes = math.ceil(total_height / viewport_height)
        for i in range(passes):
            if i == 0:
                driver.save_screenshot("screens/" + name + "_0.png")
                continue
            driver.execute_script("window.scrollTo(0, "+ str(i*viewport_height) + ");")
            time.sleep(.2)
            driver.save_screenshot("screens/" + name + "_" + str(i) + ".png")
    else:
        driver.save_screenshot("screens/" + name + ".png")
```

You could also use the ```set_window_size()```  or ```maximize_window()``` property. The size of the Xvfb window is located in /etc/init.d/xvfb.

```
# Python
driver = webdriver.Chrome()
driver.set_window_size(2000, 2000)

# /etc/init.d/xvfb
XVFBARGS=":1 -screen 0 2200x2200x24+32 -ac +extension GLX +render -noreset"
```
