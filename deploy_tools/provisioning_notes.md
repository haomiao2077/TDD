Provisioning a new site
=======================

# required packages:

* nginx
* python 3.6
* virtualenv + pip
* Git

eg, on ubuntu:

	sudo apt-get install python3 python3.6-venv nginx

## Nginx Virtual Host config
	
* see nginx.template.conf
* replace SITENAME with, e.g. haomiao-cc.xyz

## Systemd service

* sen gunicorn-systemd.template.service
* replace SITENAME

## Folder structure
/home/username
haomiao-cc.xyz
├── database
├── source
├── static
└── virtualenv
