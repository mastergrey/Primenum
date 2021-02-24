import numpy as np 
import math 
import time
from differece import get_patterns
from differece import prime_list
from differece import length_of_primelist
from multiprocessing import pool
from numba import njit,jit
#from numba.typed import List
import sys
sys.setrecursionlimit(len(prime_list))

get_len=len(prime_list)

def gilbreath_conjecture(prime_list):
    
    length=len(prime_list)
    iterator=0
    while(iterator<length-1):
        data=int(prime_list[iterator+1])-int(prime_list[iterator])
        prime_list.append(abs(data))
        iterator+=1
    del prime_list[0:length]
    print(prime_list)


gilbreath_conjecture(prime_list)



