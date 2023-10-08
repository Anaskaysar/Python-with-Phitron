class Phone:
    manufacutured = 'China'
    #constructor
    def __init__(self,owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    def send_sms(self,phone,sms):
        text = f'Sending to: {phone} {sms}'
        print(text)

myPhone = Phone("Kala Chan", "Oppo", 12000)
print(myPhone.brand)