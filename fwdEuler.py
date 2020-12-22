
def func( x, y ): 
    return -Lambda*y 
      
# Function for euler formula 
def euler( x0, y, h, x ): 
    temp = -0
  
    # Iterating till the point at which we 
    # need approximation 
    while x0 < x: 
        temp = y 
        y = y + h * func(x0, y) 
        x0 = x0 + h 
  
    # Printing approximation 
    print("Approximate solution at x = ", x, " is ", "%.6f"% y) 
      
# Driver Code 
# Initial Values 
u0 = 0
Lambda= 1.1
t0=0
t_end =20 

y0 = 1
h = 0.025
  
# Value of x at which we need approximation 
x = 0.1
  
euler(t0, y0, h, t_end) 
