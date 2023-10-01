import csv
import os

employer_file='employer_date.csv'
salary_file='salary.csv'
user_file='user.csv'
folder_name='csv'
# Returns the current working directory
current_directory=os.getcwd()

class Staff:
    

   # calculate monthly salary 
   def calculate_salary(self):
      # use os module to access to csv files direction
      path=os.path.join(current_directory,folder_name,salary_file)
      with open(path,'r+',newline='') as salary_csv:
         write=csv.DictWriter(salary_csv, fieldnames=["personal code","salary"])
         write.writeheader()

      user_id=input('id: ')
      
      # get the number of working days(use date_csv_file)
      person_day=0
      path_directory=os.path.join(current_directory,folder_name,employer_file)
      with open(path_directory,'r',newline='') as filecsv:
         reader=csv.reader(filecsv)

         for row in reader:
            if user_id==row[1]:
               person_day+=1

      daily_salary=5000
      present_day=person_day
      
      # calculate monthly salary
      salary=(daily_salary * present_day)

      # to check the id and personal code of user is exist(use user.csv file)
      path_direct=os.path.join(current_directory,folder_name,user_file)
      with open(path_direct,'r+',newline='') as user_info:
         reader= csv.reader(user_info)
         for row in reader:
               if user_id == row[0]:
                  Personal_code = row[1]
                  # to check duplicate item
                  path_dir=os.path.join(current_directory,folder_name,salary_file)
                  with open(path_dir,'r') as read:
                     reader=csv.reader(read)

                     is_exsict=False

                     for row in reader:
                        if Personal_code==row[0]: 
                           print('This id has already exisct!')
                           is_exsict=True
                     # submit salary to csv file
                     if( not is_exsict):
                           path_dir=os.path.join(current_directory,folder_name,salary_file)   
                           with open(path_dir,"a+",newline='') as write:
                              writer=csv.writer(write)
                              writer.writerow([Personal_code,salary])

   # function to show csv list  
   def user_see_salary(self):

      user_input =input("enter your personal code: ")
      path=os.path.join(current_directory,folder_name,salary_file)
      with open(path,'r') as read:
         reader=csv.reader(read)
         for row in reader:
            if user_input == row[0]:
                  print(row[1])

            





