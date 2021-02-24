prime=[2,3,5,7,11,13,17,19,23]



def differece(prime):
    length=len(prime)
    i=0
    while(i<length-1):
        d=prime[i+1]-prime[i]
        prime.append(abs(d))
        i+=1
    del prime[0:length]   
    print(prime)
    while(len(prime)>=1):
        differece(prime)


differece(prime)