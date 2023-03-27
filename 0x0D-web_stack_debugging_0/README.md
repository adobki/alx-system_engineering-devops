# ReadMe

## ___0x0D.Web stack debugging #0.___
This folder contains the actual results of completing the tasks in the project named ___0x0D.WEB STACK DEBUGGING #0.___

### 0.Give me a page!
> In this first debugging project, there was just one task[^1], which was to get Apache to run in a Docker container and have it return a webpage containing ```Hello Holberton``` when the root of it (the web server) is queried.
> The problem/bug was that the Apache service wasn't running in the container, so this script simply starts the service after setting the ServerName in the Apache config file (to avoid an warning message that would be displayed if said config option isn't set to the current hostname when the service is started).

[^1]: [0-give_me_a_page](0x0D-web_stack_debugging_0/0-give_me_a_page).
