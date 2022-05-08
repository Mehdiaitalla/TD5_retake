from Order import Order

def main():
    # Instiations
    buy_1 = Order(15,100,True)
    buy_2 = Order(10,50,True)
    sell_1 = Order(15,100,True)
    sell_2 = Order(10,50,True)
    
    # Methods tests
    print(buy_1+buy_2) 
    print(sell_1+sell_2)
    print(buy_1+sell_2)
    print(buy_2+sell_2)

    buy_1>=buy_2
    buy_1==buy_2
    buy_1 >= sell_1
    buy_1 <= sell_2

if __name__ == "__main__":
    main()