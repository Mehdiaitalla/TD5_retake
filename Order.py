class Order:
    def __init__(self, quantity, price, is_a_buy):
        self.set_quantity(quantity)
        self.set_price(price)
        self.set_is_a_buy(is_a_buy)

    # getters 
    def get_quantity(self):
        return self.quantity
    
    def get_price(self):
        return self.price

    def get_is_a_buy(self):
        return self.is_a_buy

    # setters
    def set_quantity(self, value):
        self.quantity = value
    
    def set_price(self, value):
        self.price = value
    
    def set_is_a_buy(self, value):
        self.is_a_buy = value


    # Methods
    def __ge__(self, other):
            if self.is_a_buy and not other.is_a_buy or not self.is_a_buy and other.is_a_buy : 
                raise TypeError('Orders doesn\'t have the same type.')

            self_value = self.quantity * self.price
            other_value = other.quantity * other.price

            if self_value >= other_value : 
                print( "self is greater then other" )
                return True
            else : 
                print( "other is greater then self" )
                return False

    def __le__(self, other):
            if self.is_a_buy and not other.is_a_buy or not self.is_a_buy and other.is_a_buy : 
                raise TypeError('Orders doesn\'t have the same type.')

            self_value = self.quantity * self.price
            other_value = other.quantity * other.price

            if self_value <= other_value : 
                print( "self is lower then other" )
                return True
            else : 
                print( "other is lower then self" )
                return False

    def __add__(self, other):
        if self.is_a_buy and not other.is_a_buy or not self.is_a_buy and other.is_a_buy : 
                raise TypeError('Orders doesn\'t have the same type.')
        return Order(self.quantity + other.quantity, self.price + other.price, self.is_a_buy)
       
    def __str__(self):
        details = f"Order properties :\n  -Quantity : {self.quantity}\n  -Price : {self.price}\n  -Is a buy : {self.is_a_buy}\n" 
        with open("output.txt", "a") as myfile:
            myfile.write(details)
        return details