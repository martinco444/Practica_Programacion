x = 121
x_str = str(x)
x_list = x_str.split()
x_rev = list(x_str)
x_rev.reverse()  
print(x_list)  
print(x_rev)

if x_list == x_rev:
    print("verdadero")
else:
    print("falso")