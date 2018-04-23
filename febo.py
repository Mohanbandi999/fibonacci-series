def febi(num):
    a,b=0,1
    
    for i in range(num):
        a,b=b,b+a
    return a

def main(num):
    int(input("enter the number:  "))
    for i in range(num):
        print febi(i)