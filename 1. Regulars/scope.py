#global scope vs functional scope


balance = 3000

def buy_things (item, price):
    #local scope variable
    #you can access global variable without using the global keyword
    global balance
    balance = balance - price
    print(f'Balance after buying item {item}', balance)

buy_things("Sunglass", 1000)