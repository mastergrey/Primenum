difference_list=[]

prime_num=open("/home/grey/Desktop/Primenum/prime.txt","r")
prime_list = prime_num.readlines()
length_of_primelist=len(prime_list)
def get_patterns(prime_list):
    size_of_list=len(prime_list)
    i=0
    while(i<size_of_list-1):
        d=int(prime_list[i+1])-int(prime_list[i])
        difference_list.append(d)
        i+=1
    return(difference_list)




prime_num=open("/home/grey/Desktop/Primenum/prime.txt","r")
prime_list = prime_num.readlines()
prime_num.close()
get_patterns(prime_list)

#These are some random stats that you might find interesting
print(difference_list)
