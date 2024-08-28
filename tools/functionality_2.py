def chunk_matcher(test_string, actual_string):
    if len(test_string)<=len(actual_string):
        final_blow = False
        for i in range(len(test_string)):
            if test_string[:len(test_string-i)] in actual_string:
                final_blow = True
                final_text = test_string[:len(test_string)-i]
                break
    return final_text    
        
    


def similarity_percentage(actual_string, test_string):
    final_percentage = 0
    if actual_string.upper() == test_string.upper():
        final_percentage =100
    else:
        for i in range(len(test_string)):
            if test_string[0].upper()== actual_string[0].upper():    
                if test_string[i].upper() == actual_string[i].upper():
                    final_percentage += 100/len(test_string)
                
                elif i+1>=len(actual_string) or (test_string[i].upper() == actual_string[i+1] or test_string[i].upper() == actual_string[i-1]):
                    final_percentage += 100/(len(test_string)*1.5)
                
                elif i+2>=len(actual_string) or (test_string[i].upper() == actual_string[i+2] or test_string[i].upper() == actual_string[i-2]):
                    final_percentage += 100/(len(test_string)*3)
                print(final_percentage,i)
        final_percentage-=10
    return final_percentage


print(similarity_percentage("chicken", "chickn"))
print(".................")
print(similarity_percentage("chicken", "cihcken"))
print(".................")
print(similarity_percentage("chicken", "chicken"))
print(".................")
print(similarity_percentage("chicken", "chicke"))
print(".................")
print(similarity_percentage("chicken", "beef"))
print(".................")
print(similarity_percentage("chicken", "pork"))
print(".................")
print(similarity_percentage("chicken", "chicke"))

print(".................")