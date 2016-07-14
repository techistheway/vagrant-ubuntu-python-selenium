# vagrant-ubuntu-python-selenium
VagrantFile to launch the minimal environment for a Python Selenium testing environment.

# Usage


git clone https://github.com/techistheway/vagrant-ubuntu-python-selenium

cd vagrant-ubuntu-python-selenium

vagrant init;vagrant up

# SSH Forwarding tips

# # Local Port Forward:

If you want to access a port hosted on the guest from the host, use a local port forward.


vagrant ssh -- L3000:localhost:3000 L4000:localhost:4000


```
-L [bind_address:]port:host:hostport
-L [bind_address:]port:remote_socket
-L local_socket:host:hostport
-L local_socket:remote_socket
```

# # Remote Port Forward

If you want to access a port hosted on the host from the guest, use a remote port forward.


vagrant ssh -- -R4000:localhost:4000 -R5000:localhost:5000


```
-R [bind_address:]port:host:hostport
-R [bind_address:]port:local_socket
-R remote_socket:host:hostport
-R remote_socket:local_socket
```

# Screenshots for long pages

chromedriver's handling of screenshots only captures what's in the browser's viewport. This function will scroll the page down until the end, taking one screenshot per scroll.

Note that there will be some overlap on the lap page. This can be handled, but I didn't for my use case.

```
def screenshot(page,name):
    if page is not None:
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
