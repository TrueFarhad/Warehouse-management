
import csv
import os

file_name='user.csv'
file_name_two='employer_category.csv'
folder_name="csv" 

# Returns the current working directory
current_directory=os.getcwd()

class User_info:
        # use os module to access to csv files direction
        path_directory=os.path.join(current_directory,folder_name,file_name)
        with open(path_directory,'r+',newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = ["id",'personal_code',"first_name", "last_name", "role"])
                writer.writeheader()

        # function for add user information in csv file
        def add_user_info(self):
                
                add_user=input('Do you want to add new user? Y:Yes | N:NO: ')

                if add_user.capitalize()=='Y':
                        path_directory=os.path.join(current_directory,folder_name,file_name_two)
                        with open(path_directory,'r',newline='') as csvfile:
                                read= csv.reader(csvfile)
                                job_position_list=[]
                                for row in read:
                                      job_position_list.append(row[0]) 

                        position_category=input(f"To which job position do you want to add  new employer? {job_position_list}: ")
                        chosen_position=position_category.capitalize()

                        if chosen_position in job_position_list:
                                
                                user_id=input('Enter user_id:')
                                user_personal_code=input('Enter personal_code:')
                                first_name=input('Enter first_name:')
                                last_name=input('Enter last_name:')
                                user_role=input('Enter role: admin | employer: ')

                                path=os.path.join(current_directory,folder_name,file_name)
                                with open(path, 'r+',newline='') as csv_file:
                                        data_reader= csv.reader(csv_file)
                                        datawriter=csv.writer(csv_file)
                                        
                                        is_user_availebl=False
                                        # check duplicate items
                                        for row in data_reader:
                                                if user_id == row[0]:
                                                        is_user_availebl=True
                                                        break
                                                
                                        if is_user_availebl:
                                                print("This user is already exsict")
                                        # submit new user to csv file
                                        else:
                                                datawriter.writerow([user_id,user_personal_code,first_name.capitalize(),last_name.capitalize(),user_role.capitalize()])
                                                print("Your user has been successfully added.")
                        else:
                                print('your job position name is not exsict!')

                # exit function
                elif add_user.capitalize()=='N':
                        print("The process is over.")
                        

        # function to show csv list
        def show_user_list(self):
                show_list=input('Do you want to see user list? Y:Yes | N:NO: ')

                if show_list.capitalize()=='Y':
                        path=os.path.join(current_directory,folder_name,file_name)
                        with open(path,'r') as csvfile:
                                data_reader=csv.reader(csvfile)
                                for row in data_reader:
                                        print(row)
                # go to add_user_info function
                elif show_list.capitalize()=='N':
                        User_info.add_user_info(self)                              


        # this function add new job position
        def add_job_position(self):

                job_name=input("Please write your job position name: ")
                position=job_name.capitalize()

                path_directory=os.path.join(current_directory,folder_name,file_name_two)
                with open(path_directory, 'r+', newline='') as csv_file:
                        datareader = csv.reader(csv_file)
                        datawriter=csv.writer(csv_file)

                        is_category_availebl=False

                        for row in datareader:
                                if position == row[0]:
                                        is_category_availebl=True
                                        break

                        if is_category_availebl:
                                print("This job position is already exsict")       

                        else:
                                datawriter.writerow([position])
                                print("Your job position has been successfully added.")


# p1=User_info()
# p1.add_job_position()                    