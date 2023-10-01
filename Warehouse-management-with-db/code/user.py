import sqlite3
import functions
from constants.constant import db_names,table_names


# sql_connect=sqlite3.connect(db_names["employer"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''CREATE TABLE {table_names["user_table"]}
#                     (job_position text,
#                     employer_id integer,
#                     first_name text,
#                     last_name text,
#                     role text, 
#                     personal_code integer,
#                     salary integer)''' )

# sql_connect.commit()
# sql_connect.close()





class User_info:
     
     # add user_info to table
     def add_user(self):
      
      sql_connect=sqlite3.connect(db_names["user"])
      cursor_sql=sql_connect.cursor()



      print("Enter the following user information to add")  
      job_position=input('Enter job_position:')
      user_id=input('Enter user_id:')
      first_name=input('Enter your first_name:')
      last_name=input('Enter last_name:')
      role=input('Enter role:')
      personal_code=input('Enter personal_code:')
      salary=input('Enter daily_salary:')
      
      
      cursor_sql.execute("SELECT * FROM employers ")
      table_list=cursor_sql.fetchall() 

      is_product_avelible=False
  
      for item in table_list:
            id=int(user_id)
            if item[1]==id:
              is_product_avelible=True
              break

      if is_product_avelible:
            print("This id is already exsict")
            
      else:
            list=[job_position,user_id,first_name,last_name,role,personal_code,salary]
            functions.add_many(list,db_names["user"],table_names["user_table"],len(list))
     
     # showing the user_info from table
     def show_user_list(self):       
               
               show_all_user=input("Do you want to see the whole list of users?")
               
               if show_all_user.capitalize()=='Y':
                functions.show_all(db_names["user"],table_names["user_table"])
               
               elif show_all_user.capitalize()=='N':
                    filter_item=input("What filter do you want to search based on? job position | id | name: ")
                    
                    if filter_item.capitalize()=='Job position':
                         position=input('Enter Job position:')
                         job_position_name=position.capitalize()
                         functions.selection(job_position_name,db_names["user"],table_names["user_table"])
                         
                    elif filter_item=='id':
                         id=input('Enter user_id:')
                         id_number=int(id)
                         functions.selection(id_number,db_names["user"],table_names["user_table"])
                    
                    elif filter_item.capitalize()=='Name':
                         name=input('Enter your user name:')
                         product_name=name.capitalize()
                         functions.selection(product_name,db_names["user"],table_names["user_table"])



# l=[(1,),(2,),(3,)]                            
# functions.delete_items(l,db_names["user"],table_names["user_table"])

  

p1=User_info()
p1.add_user()




