x=int(input("x="))
if (x>0) and (x<=125):
    if x/5<=5:
        print("A")
    elif  (x/5>5) and (x/5<=10): 
        print("B")
    elif  (x/5>10) and (x/5<=15):
        print("C")
    elif (x/5>15) and (x/5<=20):
        print("D")
    elif (x/5>20) and (x/5<=25):
        print("E")
