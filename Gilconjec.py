from collections import Counter
from matplotlib import pyplot as plt
from differece import get_patterns






for i in difference_list:
    if(int(i)%2==0):
        my_pen.right(90)
        my_pen.forward(int(i))
    else:
        my_pen.left(90)
        my_pen.forward(int(i))



#print("From the total number of numbers "+str(len(difference_list)))
#base_vals=set(difference_list)
#print("The base vals for this are "+str(len(base_vals)))
#dic=Counter(difference_list)
#print(dic)

#con=plt.bar(range(int(len(difference_list))),difference_list)
#print(con)
plt.show()