import csv
import os

file_name='storage.csv'
folder_name="csv"

# Returns the current working directory
current_directory=os.getcwd()


class Storage:
        # use os module to access to csv files direction
        path=os.path.join(current_directory,folder_name,file_name)
        with open(file_name, 'r+',newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = ["name", "size", "location"])
            writer.writeheader()
        
        
        # function for add new storage
        def add_storage(self):    
            
            add_storage=input('Do you want to add new storage? Y:Yes | N:NO: ')
            
            if add_storage.capitalize()=='Y':
                name=input('Enter your storage name:')
                storage_name=name.capitalize()
                storage_size=input('Enter your storage size:')
                storage_location=input('Enter your storage location:')
                
                path=os.path.join(current_directory,folder_name,file_name)
                with open(path, 'r+',newline='') as infile:
                        data= csv.reader(infile)
                        datawriter=csv.writer(infile)
                        
                        is_storage_availebl=False
                        # check duplicate items
                        for row in data:
                            if storage_name == row[0]:
                                is_storage_availebl=True
                                break
                                
                        if is_storage_availebl:
                            print("This storage is already exsict")       

                        # submit storage info to csv file
                        else:
                            datawriter.writerow([storage_name,storage_size.capitalize(),storage_location.capitalize()])
                            print("Your storage has been successfully added.")
            # exit function
            elif add_storage.capitalize()=='N':
                
                print("The process is over.") 


        # function for show storage list
        def show_storage_list(self):
            
            show_list=input('Do you want to see storage list? Y:Yes | N:NO: ')
                
            if show_list.capitalize()=='Y':

                path=os.path.join(current_directory,folder_name,file_name)
                with open(path,'r') as csv_file:
                    data=csv_file.reader(csv_file)
                    for row in data:
                        print(row)
            # go to add storage function
            elif show_list.capitalize()=='N':
                
                Storage.add_storage(self)