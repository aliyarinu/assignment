def GCD(a ,b):
    # let a and b be the two integers.
    if b>0:
        a = int(a)
        b = int(b)
        if a == 0 :
            print('GCD is ' + str(b))
    
    
        elif b == 0:
            print('GCD is ' + str(a))
        #gcd(0,n) = n , n is any integer.
        else:
            y = a%b
            while (y != 0):
            
                a = b
                b = y
                y = a%b
        # GCD of two numbers is the largest number that divides both of them.
        # divide the larger number by the smaller number.  
        # as the gcd(a,b) = gcd(b,r), r is the remainder, we keep reducing the equation without changing gcd, until the n th remaider is zero
        # then the gcd(0,r(n-1)) = n-1 th r = gcd(a,b)

            
        print ('GCD IS  ' + str(b))
        
            
GCD(-5,90)
