import csv  
from timeit import default_timer as timer  
from supermarket.models import visitors 
from from faker import Faker

def create_csv_file():

   with open('info.csv', 'w', newline='') as csvfile:

      fieldnames = ['name', 'location', 'country', 'email']

      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

      writer.writeheader()

      for i in range(range_value):

        writer.writerow (

         {   

             'name': fake.user_name(),
            'location':  fake.city(),
            'phone':   fake.country(),
            'email':   fake.email(),

         }

     )  
     
     
def upload_csv_with_copy():
start_time = timer()
visitors.objects.from_csv('visitors.csv')
finish_time = timer()
print(finish_time - start_time)   


def upload_csv_with_create(): 
start = timer()
data = csv.DictReader(open("visitors.csv")) 
for row in data:
     visitors.objects.create(name=row['name'], location=row['location'],
     country=row['country'], email=row['email'])
end = timer()
print("records inserted from csv file to postgres database")
print(end - start)
