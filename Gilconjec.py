from collections import Counter
from matplotlib import pyplot as plt
difference_list=[]

def get_patterns(prime_list):
    size_of_list=len(prime_list)
    i=0
    while(i<size_of_list-1):
        d=int(prime_list[i+1])-int(prime_list[i])
        difference_list.append(d)
        i+=1
    return(difference_list)







prime_num=open("/home/grey/Desktop/pinprime/prime.txt","r")
prime_list = prime_num.readlines()
prime_num.close()
get_patterns(prime_list)

#These are some random stats that you might find interesting
print(difference_list)
print("___________________________________________________________________________")
print("___________________________________________________________________________")
print("___________________________________________________________________________")
print("___________________________________________________________________________")
print("___________________________________________________________________________")
print("___________________________________________________________________________")
print("___________________________________________________________________________")
print("___________________________________________________________________________")


print("From the total number of numbers "+str(len(difference_list)))
base_vals=set(difference_list)
print("The base vals for this are "+str(len(base_vals)))
dic=Counter(difference_list)
print(dic)

con=plt.bar(range(int(len(difference_list))),difference_list)
print(con)
plt.show()