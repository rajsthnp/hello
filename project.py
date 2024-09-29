class Product:
    def __init__(self):
        self.item=[]


    def add_product(self):
       add=input("do you want to add any product: ")
       if add == "yes":
            how_many_items=int(input("how many items do you wanna add: "))
            for i in range (0,how_many_items):
                which_item=input("enter which item do you want to add: ")
                self.item.append(which_item)
            print(f"you added {which_item}")
       else :
           pass
    def remove_product(self):
        removee=input("do you want to remove any product: ")
        if removee=='yes':
            remove_item=input("which item do you want to remove: ")
            self.item.remove(remove_item)
        else :
            pass



    def price(self):
        total_cost = 0
        fruits_price = {
            "apple": 100,
            "banana": 200,
            "mango": 250
        }

        for fruits in self.item:
            if fruits in fruits_price:
                total_cost += fruits_price[fruits]

        print(f"Total cost: {total_cost}")




p1=Product()
p1.add_product()
print(p1.item)
p1.remove_product()
print(p1.item)
p1.price()