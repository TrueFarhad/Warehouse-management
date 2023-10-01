import datetime
import csv
from tempfile import NamedTemporaryFile
import shutil
import os

tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
employer_file='employer_date.csv'
product_enter_file='product_enter_date.csv'
product_exit_file='product_exit_date.csv'
user_file='user.csv'
product_file='product.csv'
folder_name='csv'


# showing the current date and time
time_module= datetime.datetime.now()

# showing the current time
time=(time_module.strftime("%X"))
# showing the cueernt date
date=(time_module.strftime("%x"))
# Returns the current working directory
current_directory=os.getcwd()

class Date:
   
   # function to submit date and time of employer's entry   
   def employer_enter(self):
        # use os module to access to csv files direction
        path=os.path.join(current_directory,folder_name,employer_file)
        with open(path,'r+',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(['Date','Id','first_name','last_name','Enter_time','Exit_time'])

        user_id_input=input("id: ")
        path=os.path.join(current_directory,folder_name,employer_file)
        with open(path,'r') as csvfile:
            reader=csv.reader(csvfile)
            is_user_enter = False
        
            for row in reader:
                if user_id_input==row[1]:
                    if date==row[0]:
                        print('You have already entered!')
                        is_user_enter = True

        if(not is_user_enter):    
            path_directory=os.path.join(current_directory,folder_name,user_file)
            with open(path_directory,'r') as file:
                user_info=csv.reader(file)

                for info in user_info:
                    if user_id_input==info[0]:
                        path_directory=os.path.join(current_directory,folder_name, employer_file)
                        with open(employer_file,'a+',newline='') as csvfile:
                         write=csv.writer(csvfile)
                         write.writerow([date,user_id_input,info[1],info[2],time])
                         print('successfully enterd!')

   # function to submit time of employer's departure                      
   def employer_exit(self):

    user_id_input=input('id: ')
    # use os module to access to csv files direction
    path=os.path.join(current_directory,folder_name,employer_file)
    with open(path,'r+',newline='') as f,tempfile:
        reader=csv.reader(f)
        write = csv.writer(tempfile, delimiter=',', quotechar='"')
        
        for row in reader:
            if row[1]==user_id_input:
             row.append(time)    
             write.writerow(row)
            else:    
             write.writerow(row)  


        

    shutil.move(tempfile.name, employer_file)               


   # function to submit date and time of product's entry to warehouse
   def product_enter(self):
        # use os module to access to csv files direction
        path=os.path.join(current_directory,folder_name,product_enter_file)
        with open(path,'r+',newline='') as enterfile:
            writer=csv.writer(enterfile)
            writer.writerow(['Id','product_name','Date','time'])

        product_id_input=input("id: ")
        path=os.path.join(current_directory,folder_name,product_enter_file)
        with open(path,'r')as enterfile:
            reader=csv.reader(enterfile)
            is_product_enter=False

            for row in reader:
             if product_id_input == row[0]:
                if date == row[2]:
                    print("You're product have already entered!")
                    is_product_enter=True

        if(not is_product_enter):    
            path_direct=os.path.join(current_directory,folder_name,product_file)
            with open(path_direct,'r') as file:
             item_reader=csv.reader(file)

             for item in item_reader:
                if product_id_input==item[0]:
                    path=os.path.join(current_directory,folder_name,product_enter_file)
                    with open(path,'a+',newline='') as enterfile:
                        write=csv.writer(enterfile)
                        write.writerow([product_id_input,item[1],date,time])
                        print('successfully enterd!')

   # function to submit date and time of product's departure to warehouse
   def product_exit(self):
        # use os module to access to csv files direction
        path=os.path.join(current_directory,folder_name,product_exit_file)
        with open(path,'r+',newline='') as exitfile:
            writer=csv.writer(exitfile)
            writer.writerow(['Id','product_name','Date','time'])

        product_id_input=input("id: ")
        path=os.path.join(current_directory,folder_name,product_exit_file)
        with open(path,'r')as exitfile:
            reader=csv.reader(exitfile)
            is_product_exit=False

            for row in reader:
             if product_id_input == row[0]:
                if date == row[2]:
                    print("You're product have already entered!")
                    is_product_exit=True

        if(not is_product_exit):    
            path_directory=os.path.join(current_directory,folder_name,product_file)
            with open(path_directory,'r') as file:
             item_reader=csv.reader(file)

             for item in item_reader:
                if product_id_input==item[0]:
                    
                    path=os.path.join(current_directory,folder_name,product_exit_file) 
                    with open(path,'a+',newline='') as exitfile:
                        write=csv.writer(exitfile)
                        write.writerow([product_id_input,item[1],date,time])
                        print('successfully enterd!')





# employer=Date()
# employer.product_enter()   