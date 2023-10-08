

'''
regular arguments with single astrics return a tupples 
where key argument with double astrics return a dictionary

'''
#taking parameters in order
def full_name(first, last):
    name = f'Full name is: {first} {last}'
    return name

# name = full_name("Alu", "Kodu")
# print(name)


#taking parameters not in order
def famous_name(first, last,**addition):  #double astricks sign for key arguments
    name = f' {first} {last} {addition} '

    for key, value in addition.items():
        print(key, value)
    return name  #key arguments return a dictionary


name2 = famous_name(last="kodu", first= "alu", title = 'hujur', addition="Shayokh")
print(name2)

#in python we can return multiple parameters or arguments
# all the returned parameters will returned as tupple like (x,y,z)
# you can also reutn as list meaning [x,y,z]
