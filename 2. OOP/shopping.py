class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,item,price,quantity):
        product = {'item':item, 'price':price, 'quantity': quantity}
        self.cart.append(product)
    
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total +=item['price']*item['quantity']
        print('total price',total)
        if amount < total:
            return f'Please provide {total - amount} more'
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')

swapon = Shopping('Mr Shopon')
swapon.add_to_cart("Alu",50,6)
swapon.add_to_cart("Dim",10,12)
swapon.add_to_cart("Tometo",60,5)


print(swapon.cart)
swapon.checkout(1000)