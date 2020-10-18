a=int(input("Nr de gaini:"))
b=int(input("Numarul de boabe de porumb:"))
if (b%(a+1)==0):
    print("egalitate")
elif(b%(a+1)!=0):
    print("curcanul a primit cu ", (b%(a+1)), "boabe mai mult")
