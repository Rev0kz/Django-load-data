import csv  
from timeit import default_timer as timer  
from supermarket.models import visitors 
from from faker import Faker 

fake = Faker()


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

