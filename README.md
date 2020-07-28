# Django-load-data
This show different ways you can load data from a django application to a postgres database

## Requirement:  
django version 2.0.13 

postgres database server(version 10) 

python version 3  

## Getting started  

### Installation 
Install django framework and postgres database server using the following:   
`pip install django-postgres-copy`

`pip3 install django==2.0.13`   

`pip install Faker`

`wget sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'`

`wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`

`sudo apt-get update`

`sudo apt-get install postgresql`  

### Generate csv file with Faker 
Run the following command to generate a csv file with python faker:
`python3 generate_csvfile.py`

### Create a django project 
Use the following command to create a django project:  
`django-admin.py startproject workdemo` 

### Create a django app 
`python3 manage.py startapp supermarket`   

### Start postgres database service
Use the following command to start the postgres database service. Make sure you have already created your database already.    
`service postgres start`

### Create a postgres database
Use the command to create a postgres database named supermarket:
`CREATE DATABASE supermarket`   

### Create a user for the database
`CREATE USER sysadmin WITH PASSWORD 'sysmap'`  

`GRANT ALL PRIVILEGES ON DATABASE stock TO sysadmin`


### Edit django settings.py file 
edit the settings.py file in django and replace the database configuration settings with that of `database_config.py` file

### Launch django shell
Execute the following command to launch the django shell:  
`python3 manage.py shell`

### Migrate database
`python3 manage.py makemigrations`

`python3 manage.py migrate`

 ## Benchmarking django `django_postgres_copy`,  and `create` methods 
 Inside the django shell, execute the following command:  
 `from supermarket.models import visitors`  
 
 `from timeit import default_timer as timer`  
 
 ### Load data with django_postgres_copy
 
Then run the following python command via the django shell to upload a csv file from django to postgres database using the method `django_postgres_copy`.
```
start_time = timer()
visitors.objects.from_csv('visitors.csv')
finish_time = timer()
print(finish_time - start_time)
```  

### Load data with django create method  
Run the following python command via the django shell to upload a csv file from django to postgres database using the create method `create()` method. 
```
start = timer()
data = csv.DictReader(open("visitors.csv")) 
for row in data:
     visitors.objects.create(name=row['name'], location=row['location'],
     country=row['country'], email=row['email'])
end = timer()
print("records inserted from csv file to postgres database")
print(end - start)
```
