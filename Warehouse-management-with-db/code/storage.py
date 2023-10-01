
import sqlite3
import functions
from constants.constant import db_names,table_names

# sql_connect=sqlite3.connect(db_names["storage"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''CREATE TABLE {table_names["table4"]}
#                     (location text,
#                     storage_name text,
#                     warehouse_products text,
#                     storage_size integer)''' )

# sql_connect.commit()
# sql_connect.close()



class Storage:
     
     # add storage info to table
     def add_storage(self):
      
      sql_connect=sqlite3.connect(db_names["storage"])
      cursor_sql=sql_connect.cursor()



      print("Enter the following storage information to add")  
      storage_name=input('Enter your storage_name:')
      warehouse_products=input('Enter the products in warehouse:')      
      location=input('Enter location:')
      size=input('Enter  storage_space:')
      storage_space=(str(size) + "m")
    
      
      
      cursor_sql.execute("SELECT * FROM storage ")
      table_list=cursor_sql.fetchall() 

      is_product_avelible=False
  
      for item in table_list:
            if item[1]==storage_name:
              is_product_avelible=True
              break

      if is_product_avelible:
            print("This id is already exsict")
            
      else:
            list=[storage_name,warehouse_products,location,storage_space]
            functions.add_many(list,db_names["storage"],table_names["storage_table"],len(list))


     # showing the list of storage_info from table 
     def show_storage_list(self):
    
               show_all_storage=input("Do you want to see the whole list of storage?")
               
               if show_all_storage.capitalize()=='Y':
                  functions.show_all(db_names["storage"],table_names["storage_table"])
               
               elif show_all_storage.capitalize()=='N':
                    filter_item=input("What filter do you want to search based on? name |  warehouse_products | location : ")
                    
                    if filter_item.capitalize()=='Name':
                         name=input('Enter your Name:')
                         storage_name=name.capitalize()
                         functions.selection(storage_name,db_names["storage"],table_names["storage_table"])
                    
                    elif filter_item.capitalize()=='Location':
                         location_in=input('Enter your location:')
                         storage_location=location_in.capitalize()
                         functions.selection(storage_location,db_names["storage"],table_names["storage_table"])
                   
                    elif filter_item.capitalize()=='Warehouse_products':
                         product_name=input('Enter the name of products:')
                         warehouse_products_name=product_name.capitalize()
                         functions.selection(warehouse_products_name,db_names["storage"],table_names["storage_table"])
                    

  


p1=Storage()
p1.show_storage_list()
# x = 'hello'

# Storage.add_storage(x)
