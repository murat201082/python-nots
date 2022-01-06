"""this is module 1. welcome"""

def binary(num):
    a =""
    while num != 0:
        a += str(num %2) 
        num = num // 2
                       
    return a


def cap_to_front(text):
    new_text = ''
    
   
    for i in text:
        if i.isupper() :
            new_text += i
            text = text.replace(i, '')
        
    return (new_text + text)