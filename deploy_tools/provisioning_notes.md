Provisioning a new site
=======================

##Required packages:

* nginx
* python 3.8
* virtualenv + pip
* Git

eg, on Ubuntu:
		
		sudo apt-get update
		sudo apt-get nginx
		sudp apt-get install python3.8
		sudo apt-get install python3.8-venv
		sudp apt-get install git
		
## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
	sites
		SITENAME
			database
			source
			static
			virtualenv