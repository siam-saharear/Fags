import random


def random_id_generator( n=18,upper= True, lower = True, number = True,indentation = False):
    alphabates =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    product_id = """"""

    while len(product_id) != n:
        step = random.randint(0,3)
        
        if step == 1 and upper == True:
            product_id += str(alphabates[random.randint(1,25)]).upper()
        
        elif step == 2 and lower == True:
            product_id += str(alphabates[random.randint(0,5)].lower())
        
        elif step == 3 and number == True:
            product_id += str(random.randint(0,9))
    
    return product_id
random_number = random_id_generator(number = False , n = 26)
print(random_number,"\nlength",len(random_number))





























