# Django-load-data
This show different ways you can load data from a django application to a postgres database

## Requirement:  
django version 2.0.13 

postgres database server(version 10) 

python version 3  

## Getting started  

### Installation 
Install django framework and postgres database server using the following:   
`pip3 install django==2.0.13`
`wget sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'`
`wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`
`sudo apt-get update`
`sudo apt-get install postgresql`

### Create a django project 
Use the following command to create a django project:  
`django-admin.py startproject workdemo` 

### Create a django app 
`python3 manage.py startapp loadata`   



Use the following command to start the postgres database service. Make sure you have already created your database already.    
`service postgres start`   

Execute the following command to launch the django shell:  

`python3 manage.py shell`   


