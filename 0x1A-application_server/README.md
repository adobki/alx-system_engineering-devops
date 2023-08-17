# ReadMe

## ___0x1A.APPLICATION SERVER___
This folder contains the results of completing the tasks in the project ___0x1A.Application Server.___

### Frameworks and Technologies Used
1. Flask
2. Nginx
3. Gunicorn
4. Bash

### Files from the Mandatory Tasks
> ___[2-app_server-nginx_config](2-app_server-nginx_config)___
>
> Nginx config file to serve a page from the route /airbnb-onepage/ on port 80. Nginx should proxy requests to the process listening on port 5000.

> ___[3-app_server-nginx_config](3-app_server-nginx_config)___
>
> Nginx config file to add another route with query parameters.

> ___[4-app_server-nginx_config](4-app_server-nginx_config)___
>
> Nginx config file to add another route for the AirBnB Clone v3 API.

> ___[5-app_server-nginx_config](5-app_server-nginx_config)___
>
> Nginx config file to add another route for the AirBnB Clone v4 webpage.

> ___[gunicorn.service](gunicorn.service)___
>
> Gunicorn service to run tbe application server for AirBnB Clone v4 automatically at boot.


### Files from the Advanced Tasks
> ___[4-reload_gunicorn_no_downtime](4-reload_gunicorn_no_downtime)___
>
> Bash script to reload Gunicorn in a graceful way.
