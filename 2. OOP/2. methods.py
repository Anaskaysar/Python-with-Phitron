def call():
    print("Calling someone I don't know")
    return 'call done'

class Phone:
    price = 1200
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    '''
    Method: declaring a function within class
    Whever we aill add a method to a class we must give a default parameter "self".
    '''
    
    def call(self):  #methods should always have self parameter
        print("calling one person")
    def sendSms(self,phone,sms):
        text = f'Sending sms to : {phone} and message : {sms}'
        return text

myPhone = Phone()
print(myPhone.features)
myPhone.call()
result = myPhone.sendSms(41452,"I missed you")
print(result)