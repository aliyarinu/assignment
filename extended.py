def egcd(a, b):  
    # by ExtendedEuclidean Algorithm , gcd = ax + by. 
	# if a = 0,then value of gcd = b , x = 0, y = 1.
    
    if a == 0 :   
        return b, 0, 1
             
    gcd, x1, y1 = egcd(b%a, a)  

    #From Lemma1 , gcd(a,b) = gcd(a,r), r = remaider of b/a.
    # r = b - na, n = b//a.

    # gcd(b,r) = ((b-na)x1 +ay1))
    #by comparing , x = y1 - (b//a)x1, y = x1.
   
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd, x, y 
      
  

#let d be the gcd.
d, x, y = egcd(0, 15)  
print(d)  
print(x,y)