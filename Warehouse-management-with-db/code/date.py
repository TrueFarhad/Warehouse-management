import datetime 
import sqlite3
import functions
from constants.constant import db_names,table_names



# show the current date and time
time_module= datetime.datetime.now()

#show the current time 
time=(time_module.strftime("%X"))
# show the current date
date=(time_module.strftime("%x"))


class Date:

    # function to submit the date and time of product entry into the warehouse
    def enter_product(self):

        id=input('Enter product_id:')
        # check id entered with product id from products table (check product availability)
        sql_connect=sqlite3.connect(db_names["product"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM products ")
        table=cursor_sql.fetchall() 
        
        for item in table:
                product_id=int(id)
                if item[1]==product_id:
                    
                    # checking that the item is not duplicated
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM product_enter_date ")
                    table_list=cursor_sql.fetchall()

                    for row in table_list:
                        if date == row[1] and row[0]==product_id :
                            print("You're product have already entered!") 
                            break
                    else:
                        list=[id,date,item[2],time]
                        
                        functions.add_many(list,db_names["date"],table_names["product_enter_date_table"],len(list))
                        break
    # function to submit the date and time of product dpature into the warehouse
    def exit_product(self):
         
        id=input('Enter product_id:')
        # check id entered with product id from products table (check product availability)
        sql_connect=sqlite3.connect(db_names["product"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM products ")
        table=cursor_sql.fetchall() 
        
        for item in table:
                product_id=int(id)
                if item[1]==product_id:

                    # checking that the item is not duplicated
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM product_exit_date ")
                    table_list=cursor_sql.fetchall()

                    for row in table_list:
                        if date == row[1] and row[0]==product_id :
                            print("You're product have already entered!") 
                            break
                    else:
                        list=[id,date,item[2],time]
                        
                        functions.add_many(list,db_names["date"],table_names["product_exit_date"],len(list))
                        break
    # function to submit the date and time of empoyee's entry                             
    def enter_user(self):
        
        
        id=input('Enter user_id:')
        
         # check id entered with user id from employers table (check user availability)
        sql_connect=sqlite3.connect(db_names["user"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM employers ")
        table=cursor_sql.fetchall() 
        
        for item in table:
                user_id=int(id)
                if item[1]==user_id:

                    # checking that the item is not duplicated
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM user_date ")
                    table_list=cursor_sql.fetchall()

                    for row in table_list:
                        if  date == row[0] and row[1]==user_id:
                            print("You're employer have already entered!")
                            break
                    else:
                        list=[date,id,item[2],item[3],time,'']
                        functions.add_many(list,db_names["date"],table_names["user_date_table"],len(list))
                        break         
    # function to submit the time of empoyee's departure        
    def exit_user(self):
            
        id=input('Enter user_id:')
    

                    
        sql_connect=sqlite3.connect(db_names["date"])
        cursor_sql=sql_connect.cursor()
        cursor_sql.execute("SELECT * FROM user_date ")
        cursor_sql.fetchall()         
        time_data=time
        date_data=date
        list=(time_data,date_data,id)
        functions.update(list,db_names["date"],table_names["user_date_table"])
                    





                        
# l=[(1,)]                            
# functions.delete_items(l,db_names["date"],table_names["product_exit_date"])
# def dele(timer):
     
#     sql_connect=sqlite3.connect(db_names["date"])
#     cursor_sql=sql_connect.cursor()
#     cursor_sql.executemany(f"DELETE from {table_names['user_date_table']} WHERE user_id=?",(timer,))
#     sql_connect.commit()
#     sql_connect.close()
    
# li=[9876]    
# dele(li)                                 

product=Date()
product.exit_product()





