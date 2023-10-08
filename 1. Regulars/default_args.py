def sum(num1, num2, num3=0):
    result = num1 + num2 + num3
    return result;


total = sum(99,11,12)
# print(total)


#args

def all_sum(*numbers):
    for num in numbers:
        print(num)

total = all_sum(11,23,23)   #it will return tuffle


#def do_a_lot(*args):
    # print(args)