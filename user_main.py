from user_registration import registration

#  please refer to user registration for login username and password else do registration !!!!
registration()

# Giving option to place order,view order history,update profile
def choise():
    option = int(input("\n1-Place New Order \n2-Order History \n3-Update Profile\n"))
    
    # For Placing New Order
    if option == 1:
        from order import new_order
        obj = new_order()
        obj.new_order()

    # For Order History
    elif option == 2:
        try:
            file = open("Order.txt",'r+')
            print(file.read())
            file.close()        
            choise()
        except:
            print("Please order first if you are using the app for the first time")
            choise()

    # For Updating The Profile
    elif option == 3:
        from update_profile import update_profile
        update_profile()
    
    # If Someone Choose Other option Rather Than 1,2,3  
    else:
        print("Seclect Valid information")
        choise()

choise()