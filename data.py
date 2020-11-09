dat = open("data.dat","wb")
data = open("data.txt","w")
list_x = []
list_y = []
i = 0
while(i < 1000):
    list_x.append(i)
    print(list_x[i])
    if i == 0:
        list_y.append(float(1/3))
    else:
        list_y.append((list_y[i-1]+1)/(list_y[i-1]+3))
    print(list_y[i])
    data.write(str(list_y[i]) + "\n")
    i = i + 1

value = abs(list_y[5] - list_y[7])
print("wynik warunku: " + str(value) + " dla n = 6\n")
data.close()
dat.close()
