def function_of_xy(x,y):
    return x+y

h=0.5
x0 = 0.0
y0=1.0

k1 = h*function_of_xy(x0,y0)
k2 = h*function_of_xy((x0)+(1/2*h), y0+(1/2*k1))
k3 = h*function_of_xy((x0+(0.5*h)), y0+(0.5*k2))
k4 = h*function_of_xy(x0+h, y0+k3)

k = ((1/6)*(k1+2*k2+2*k3+k4))
print(k)
print(k1,k2,k3,k4)