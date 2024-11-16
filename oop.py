class Item:
    pay_rate = 0.8
    def __init__(self, name:str, price:int, quantity:int):
        #check the validation
        assert price >= 0 , f" price {price} is not greater than or equal to zero "
        assert quantity >= 0 , f" price {quantity} is not greater than or equal to zero "

        #passing the attributes to self
        self.name= name
        self.price= price
        self.quantity = quantity

    def total_amount_calculation(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate



item1 = Item("laptop", 48000, 2)
item2 = Item("Mobile", 2000, 10)
item3 = Item("Tablet", 10000, 5)
item4 = Item("Pro_book", 68000, 8)

print(item1.apply_discount)
 




        