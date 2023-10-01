
from products import Products
from user  import User_info
from storage import Storage

class Admin:
 
 log_in=False

 def login(self):
    self.username = "fatemeh"
    self.password = "1996m0430"
    user_name=input("Enter your username: ") 

    if user_name==self.username:
  
     enter_password=input("Enter your password: ")
     if enter_password==self.password:
      print("You're logged in!")
      Admin.log_in=True

     else:
      print("your password is false") 

    else:
      print("your username is false")  

# acsses to product section if logged in
 def acsses_product(cls):
   
  if cls. log_in: 
    
    decision=input("choose from the fllowing options: A:add product | S:show list ")
    if decision == 'A':

      Products.add_products(cls)

    elif decision == "S":

      Products.show_product_list(cls)  
            
  else:
    print("You're not logged in!") 

# acsses to user section if logged in
 def acsses_user(cls):
   
   if cls.log_in==True:
    
    decision=input("choose from the fllowing options: A:add user | S:show list ")
    if decision == 'A':

      User_info.add_user(cls)

    elif decision == "S":

      User_info.show_user_list(cls) 
   
   else:
    print("You're not logged in!")
 
# acsses to storage section if logged in 
 def acsses_storage(cls):
   
   if cls.log_in==True:
    
    decision=input("choose from the fllowing options: A:add storage | S:show list ")
    if decision == 'A':

     Storage.add_storage(cls)

    elif decision == "S":

      Storage.show_storage_list(cls)
   
   else:
    print("You're not logged in!")



p1=Admin()    
p1.login()
p1.acsses_product()





