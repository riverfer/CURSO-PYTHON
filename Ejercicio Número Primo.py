def isPrime(num):
    for i in range(2, num): 
      if i>1: 
        for j in range(2,i): 
            if(i % j==0): 
                break
        else: 
            print(i, end=" ")
isPrime(20)        

