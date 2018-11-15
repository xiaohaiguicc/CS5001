import sys
import math
def main():
    #print(sys.argv)
    max = int(sys.argv[1]) #sys.argv is a list
    
    print(2)
    #i = 3

    #while(i < max):
    for i in range(3,max+1,2):#from start to stop, not including stop with step 2.
        isPrime = True
        k = 2
        while(k < math.sqrt(i) and isPrime): #math.sqrt(i) is better than k < i
            if(i % k == 0):
                isPrime = False
            k += 1
        if(isPrime):
            print(i)
        #i += 2 #instead of i += 1


main()