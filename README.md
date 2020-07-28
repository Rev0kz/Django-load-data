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

### Start postgres database service
Use the following command to start the postgres database service. Make sure you have already created your database already.    
`service postgres start`   

### Launch django shell
Execute the following command to launch the django shell:  
`python3 manage.py shell`   

 ## Benchmarking django `create`, `save` and `django_postgres_copy` methods 
 Inside the django shell, execute the following command:  
 `from supermarket.models import visitors`  
 
Then run the following python command to upload a csv file from django to postgres database using the method `django_postgres_copy` :
```
start_time = timer()
visitors.objects.from_csv('visitors.csv')
finish_time = timer()
print(finish_time - start_time)
```  
