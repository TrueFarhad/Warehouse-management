import sqlite3
import time
import functions
from constants.constant import db_names,table_names


# sql_connect=sqlite3.connect(db_names["staff"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''CREATE TABLE {table_names["salary_table"]}
                    
#                     (month text,
#                      employer_id integer,
#                      personal_code integer,
#                      salary integer)''' )

# sql_connect.commit()
# sql_connect.close()

# sql_connect=sqlite3.connect(db_names["staff"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''DROP TABLE {table_names["salary_table"]}''')

# sql_connect.commit()
# sql_connect.close()

# show month in date
month = time.strftime("%m")
monthly=month
                
class Staff:    
  
  def calculate_salary(self):
      
      # get the numbrt of working days from date.db file
      sql_connect=sqlite3.connect(db_names["date"])
      cursor_sql=sql_connect.cursor()
      cursor_sql.execute("SELECT * FROM user_date ")
      items=cursor_sql.fetchall()

      user_id=input('id: ')
      id=int(user_id)

      number_of_working_days=0

      for row in items:
         if id == row[1]:
            number_of_working_days+=1
      
      # get the daily wage from user_info.db file
      sql_connect=sqlite3.connect(db_names["user"])
      cursor_sql=sql_connect.cursor()
      cursor_sql.execute(f"SELECT * FROM employers WHERE employer_id={id} ")
      table=cursor_sql.fetchall()

      for table_item in table:

            # calclation of monthly salary
            daily_salary=table_item[6]
            present_day=number_of_working_days
            salary=daily_salary * present_day

      # add salary to table
      sql_connect=sqlite3.connect(db_names["staff"])
      cursor_sql=sql_connect.cursor()
      cursor_sql.execute(F"SELECT * FROM salary  WHERE employer_id={id}")
      table_list=cursor_sql.fetchall()

      for row in table_list:
     
            if monthly == row[0]:
                  break
      else:
            list_item=[(monthly),(id),(table_item[5]),(salary)]
           
            functions.add_many(list_item,db_names["staff"],table_names["salary_table"],len(list_item))

              


  def show_salary(self):
       
      sql_connect=sqlite3.connect(db_names["date"])
      cursor_sql=sql_connect.cursor()
      cursor_sql.execute("SELECT * FROM user_date ")
      items=cursor_sql.fetchall()

      user_id=input('Enter user_id: ')
      id=int(user_id)

      for row in items:
         if id == row[1]:
             functions.selection(id,db_names["staff"],table_names["salary_table"])



p1=Staff()
p1.show_salary()