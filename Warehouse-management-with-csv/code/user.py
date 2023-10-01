
from products import Products
from user_info import User_info


class Admin():
   
  log_in=False
 
 # admin_accsess 
  def login(self):
    self.username = "fatemeh"
    self.password = "1996m27"
    user_name=input("Enter your username: ") 
    # check username
    if user_name==self.username:
        # check password
        password_character=input("Enter your password: ")
        if password_character==self.password:
          print("You're logged in!")
          Admin.log_in=True

        else:
          print("your password is false") 

    else:
      print("your username is false")  

  # function for acsess admin to product file if log_in
  def acsses_product(cls):
    
    if cls.log_in:
      options=input("What option do you want to acsess? p:add_product | c:add_category | s:show list : ")
      chosen_option=options.capitalize()

      if chosen_option == "P":
        Products.add_product()
      elif chosen_option == "C":
        Products.add_product_category()
      elif chosen_option == "S":
        Products.show_product_list()        
      
    else:
      print("You're not logged in!") 
  # function for acsess admin to employer file if log_in
  def acsses_employer(cls):
    
    if cls.log_in==True:
      options=input("What option do you want to acsess? u:add_user | j:add_job_position | s:show list : ")
      chosen_option=options.capitalize()

      if chosen_option == "U":
        User_info.add_user_info()
      elif chosen_option == "J":
        User_info.add_job_position()
      elif chosen_option == "S":
        User_info.show_user_list() 

    
      User_info.add_user_info()

    else:
      print("You're not logged in!")



p1=Admin()
p1.login()
p1.acsses_product()






