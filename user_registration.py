import re

def registration():
        user = "Pratham"
        password2 = 1234
        option = int(input("\n1- Login \n2- Registration \n"))
        if option == 1:
            username = (input("Username : "))
            password1 = int(input("Password : "))
            if username == user and password1 ==  password2:
                print("Welcome")
            else:
                print("Invalid Username and Password")
                registration()
        elif option == 2:
            start = input("Press Enter to register")
            name = input("\nPlease Enter Your Name : ")
            phone = input(f"{name} Enter your 10 digit phone number = ")
            data = re.findall(r"^[1-9]{1}[0-9]{9}$", phone)
            if data:
                data = input(f"{name} Enter your email id = ")
                result = re.findall(r"^[A-Za-z_+-.0-9]+@[A-Za-z]+\.[a-z]{1,3}$", data)    
                if result:
                    address = input(f"{name} Enter your address : ")
                    print("Password must consist of 1 capital leter,1 small letter,0-9 digit altist 1 ,1 special character, minimum 6 digit maximum 16 digit")
                    password = input(f"{name} Enter your password = ")
                    result1 = re.findall("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z\dd!@#$%^&*()]{6,16}",password)
                    if result1:
                        print(f"\n {name} Welcome to the application!!!!")
                    else:
                        print("Try again and Enter a valid password")
                        registration()                        
                else:
                    print("Try again and Enter valid email id ")
                    registration()
            else:
                print("Try again and Enter valid phone number")
                registration()
        else:
            print("Try again and Enter valid option")
            registration()