import os

folder_name="db"
product_file_name="product_info.db"
date_file_name="date.db"
staff_file_name="staff.db"
storage_file_name="storage_info.db"
user_file_name="user_info.db"

# use os module to access to database files direction

# Returns the current working directory
current_directory=os.getcwd()

path_product=os.path.join(current_directory,folder_name,product_file_name)
path_date=os.path.join(current_directory,folder_name,date_file_name)
path_staff=os.path.join(current_directory,folder_name,staff_file_name)
path_storage=os.path.join(current_directory,folder_name,storage_file_name)
path_user=os.path.join(current_directory,folder_name,user_file_name)

# project database file names
db_names={
    "product":path_product,
    "user":path_user,
    "storage":path_storage,
    "date":path_date,
    "staff":path_staff
}



# project database table names
table_names={
    "product_table":"products",
    "user_table":"employers",
    "storage_table":"storage",
    "product_enter_date_table":"product_enter_date",
    "user_date_table":"user_date",
    "product_exit_date":"product_exit_date",
    "salary_table":"salary"
    
}


    


