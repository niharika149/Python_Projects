class order:
    def __init__(self,Total=0):
        self.Total = Total
        
    def Tandoori_Chicken(self,quantity_Tandoori_Chicken):
        self.quantity_Tandoori_Chicken = quantity_Tandoori_Chicken
        self.Total = self.quantity_Tandoori_Chicken * 240 + self.Total
    def Truffle_Cake(self,quantity_Truffle_Cake):
        self.quantity_Truffle_Cake = quantity_Truffle_Cake
        self.Total= self.quantity_Truffle_Cake * 900 + self.Total 
    def Vegan_Burger(self,quantity_Vegan_Burger):
        self.quantity_Vegan_Burger = quantity_Vegan_Burger
        self.Total = self.quantity_Vegan_Burger * 320 + self.Total     
    def getTotal(self):
        return self.Total


class new_order(order):
    def new_order(self):
        print("\n\nMenu")

        print("\nTandoori Chicken (4 pieces) [INR 240] \nVegan Burger (1 Piece) [INR 320] \nTruffle Cake (500gm) [INR 900]")

        while True:
            order = int(input("\n1- Tandoori Chicken \n2- Vegan Burger \n3- Truffle Cake \n4- Payment \n5- Exit"))
    
            if order == 1:
                # Tanduri chicken
                quantity = int(input("Enter the quantity of Tandoori Chicken : "))
                obj.Tandoori_Chicken(quantity)
                print(f"Tanduri Chicken Quantity {quantity}")
                print(f"Payble Amount : {obj.Total}")
                data1 =(f"Tanduri Chicken {quantity} plates 280rs")
                file =  open("Order.txt","a")
                file.write(f"\nTanduri Chicken : {quantity} - 240rs plate")
                file.close()
               

            elif order == 2:
                    #  Vegam Burger
                quantity1 = int(input("Enter the quantity of Vegan Burger : "))
                obj.Vegan_Burger(quantity1)
                print(f"Vegan Burger Quantity {quantity1}")
                print(f"Payble Amount : {obj.Total}")
                dat2 =(f"\nVegan Burger {quantity1} plates 320rs")
                file =  open("Order.txt","a")
                file.write(f"\nVegan Burger : {quantity1} - 320rs plate")
                file.close()
                

    
            elif order == 3:
                   # Truffle cake
                quantity2 = int(input("Enter the quantity of Truffle Cake : "))
                obj.Truffle_Cake(quantity2)
                print(f"Truffle Cake Quantity {quantity2}")
                print(f"Payble Amount : {obj.Total}")
                data3 =(f"\nTruffle cake : {quantity2} plates 900rs")
                file =  open("Order.txt","a")
                file.write(f"\nTruffle Cake : {quantity2} - 900rs plate")
                file.close()
                
            elif order == 4:
                if obj.Total == 0:
                    print("Order First")
                else:
                    from payment import payment
                    payment()

            elif order == 5:
                from user_main import choise
                choise()
            
            else:        
                print("Not the correct option!!!!")
                break
    
        

obj = new_order()