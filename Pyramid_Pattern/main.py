row=int(input("ENTER NUMBER OF ROWS :"))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    print("*"*(2*i-1))