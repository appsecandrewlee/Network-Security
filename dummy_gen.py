import random
ATTEMPT_NUM = 10000
dummy_domain_lst = []
dummy_domain_prefix = "abcdefghijklmnopqrstuvwxy0987654321"
base_domain = ".test.com"



for i in range(0,ATTEMPT_NUM): 
    str1 = "" #empty string 
    for j in range(0,5): #5 elements 
        str1 +=str(random.choices(dummy_domain_prefix)) #random.choices() 
    str1+=base_domain #concat the ".test.com" 
    dummy_domain_lst.append(str1) #append the elements 
    print(str1)

