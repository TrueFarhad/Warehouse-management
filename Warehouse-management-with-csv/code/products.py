import csv
import os

file_name='product.csv'
file_name_two='product_category.csv'
folder_name="csv"

# Returns the current working directory
current_directory=os.getcwd()




class Products:
        # use os module to access to csv files direction
        path_directory=os.path.join(current_directory,folder_name,file_name)
        with open(path_directory, 'r+',newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = ["product_id","name", "quantity", "price","product_description"])
                writer.writeheader()
                                
        
        # add product information
        def add_product(self):
                
                add_product=input('Do you want to add new product? Y:Yes | N:NO: ')
                
                if add_product.capitalize()=='Y':
                        path=os.path.join(current_directory,folder_name,file_name_two)
                        with open(path,'r',newline='') as csvfile:
                                read= csv.reader(csvfile)
                                category=[]
                                for row in read:
                                        category.append(row[0])

                        choose_category=input(f"To which category do you want to add your products? {category}: ")
                        chosen_category=choose_category.capitalize()
                        
                        if chosen_category in category:

                                product_id=input('Enter product_id:')
                                product_name=input('Enter your product name:')
                                product_quantity=input('Enter quantity:')
                                product_price=input('Enter price:')
                                product_description=input('Enter product_description:')
                                path_directory=os.path.join(current_directory,folder_name,file_name)
                                with open(path_directory, 'r+',newline='') as csv_file:
                                        data_reader= csv.reader(csv_file)
                                        datawriter=csv.writer(csv_file)
                                        
                                        is_product_availebl=False

                                        for row in data_reader:
                                                if product_id == row[0]:
                                                        is_product_availebl=True
                                                        break
                                                
                                        if is_product_availebl:
                                                print("This product is already exsict")       
                                                
                                        else:
                                                datawriter.writerow([ product_id,product_name,product_quantity,product_price,product_description])
                                                print("Your product has been successfully added.")
                        else:
                                print('your category name is not exsict!')                        

                elif add_product.capitalize()=='N':                           
                        
                        print("The process is over.")             



        # show the list of products
        def show_product_list(self):
                
                show_list=input('Do you want to see product list? Y:Yes | N:NO: ')

                if show_list.capitalize()=='Y':
                        path=os.path.join(current_directory,folder_name,file_name)
                        with open(path,'r') as filecsv:
                                reader=csv.reader(filecsv)
                                for row in reader:
                                        print(row)

                elif show_list.capitalize()=='N':

                        Products.add_product(self)


        # function for add product category
        def add_product_category(self):
                               
            # add category to csv 
            category_name=input("Please write your category name: ")
            chosen_category=category_name.capitalize()
            path=os.path.join(current_directory,folder_name,file_name_two)
            with open(path, 'r+', newline='') as csvfile:
                datareader = csv.reader(csvfile)
                datawriter=csv.writer(csvfile)
                
                is_category_availebl=False
                
                for row in datareader:
                    if chosen_category == row[0]:
                        is_category_availebl=True
                        break
                
                if is_category_availebl:
                    print("This category is already exsict")       
                
                else:
                    datawriter.writerow([chosen_category])
                    print("Your category has been successfully added.")


p1=Products()
p1.show_product_list()

