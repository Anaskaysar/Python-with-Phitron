class Shop:
    shopping_mall = "Jamuna"
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []  #here it is an instance attribute
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

