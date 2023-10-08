class Shop:
    cart = []  #class attribute
    def __init__(self, buyer):
        self.buyer = buyer
    def add_to_cart(self, item):
        self.cart.append(item)

mehzbeen = Shop('Meh Jabeen')
mehzbeen.add_to_cart("Shoes")
mehzbeen.add_to_cart("Phone")
print(mehzbeen.cart)

nisho = Shop("noisho")
nisho.add_to_cart("Cap")
nisho.add_to_cart("Headphone")
print(nisho.cart)
