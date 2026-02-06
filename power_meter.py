sal=int(input("Enter Annual Salary:"))
pmr=int(input("Previous meter reading:"))
cmr=int(input("Current Meter Reading:"))
units=cmr-pmr
print('Units consumed:',+units)
gtype=str(input("Gender M/F:").upper().strip())
ctype=str(input("Meter E/N:").upper().strip())
pvalue=0
discounted=0
final=0
if(units>100):
    if(units>1000):
        pvalue=units*10
        print("Pvalue=",pvalue,"/-")
    elif(units>=800 and units<1000):
        pvalue=units*8
        print("Pvalue=",pvalue,"/-")
    elif(units>=600 and units<800):
        pvalue=units*6
        print("Pvalue=",pvalue,"/-")
    elif(units>=400 and units<600):
        pvalue=units*4
        print("Pvalue=",pvalue,"/-")
    elif(units>=200 and units<400):
        pvalue=units*2
        print("Pvalue=",pvalue,"/-")
    else:
        pvalue=units*1
        print("Pvalue=",pvalue,"/-")
    print('********************')
else:
    print("Units less than 100 so no need to pay current bill")
if(sal>=50000):
    if(gtype=='F' and ctype=='E'):
        if(pvalue>10000):
            discounted=pvalue-(pvalue*0.20)
            print("Pvalue after 20% discount=",discounted)
            final=discounted-1000
            print("Final Bill after applying 1000 voucher=",final)
        elif(pvalue>5000 and pvalue<=10000):
            discounted=pvalue-(pvalue*0.10)
            print("Pvalue after 10% discount=",discounted)
            final=discounted-500
            print("Final Bill after applying 500 voucher=",final)
        elif(pvalue>2000 and pvalue<=5000):
            discounted=pvalue-(pvalue*0.05)
            print("Pvalue after 5% discount=",discounted)
            final=discounted-300
            print("Final Bill after applying 300 voucher=",final)
        else:
            print("Error from developer")
    elif(gtype=='M' and ctype=='E'):
        if(pvalue>10000):
            discounted=pvalue-(pvalue*0.10)
            print("Pvalue after 10% discount=",discounted)
            final=discounted-800
            print("Final Bill after applying 800 voucher=",final)
        elif(pvalue>5000 and pvalue<=10000):
            discounted=pvalue-(pvalue*0.05)
            print("Pvalue after 5% discount=",discounted)
            final=discounted-400
            print("Final Bill after applying 400 voucher=",final)
        elif(pvalue>2000 and pvalue<=5000):
            discounted=pvalue-(pvalue*0.03)
            print("Pvalue after 3% discount=",discounted)
            final=discounted-200
            print("Final Bill after applying 200 voucher=",final)
        else:
            print("Error from developer")
    elif(gtype=='F' and ctype=='N'):
        if(pvalue>10000):
            final=pvalue-(pvalue*0.20)
            print("Final Bill after 20% discount=",final)
        elif(pvalue>5000 and pvalue<=10000):
            final=pvalue-(pvalue*0.10)
            print("Final Bill after 10% discount=",final)
        elif(pvalue>2000 and pvalue<=5000):
            final=pvalue-(pvalue*0.05)
            print("Final Bill after 5% discount=",final)
        else:
            print("Error from developer")
    elif(gtype=='M' and ctype=='N'):
        if(pvalue>10000):
            final=pvalue-(pvalue*0.10)
            print("Final Bill after 10% discount=",final)
        elif(pvalue>5000 and pvalue<=10000):
            final=pvalue-(pvalue*0.05)
            print("Final Bill after 5% discount=",final)
        elif(pvalue>2000 and pvalue<=5000):
            final=pvalue-(pvalue*0.03)
            print("Final Bill after 3% discount=",final)
        else:
            print("Error from developer")
    else:
        print("Error from developer")
else:
    print("Your annual salary is less than 50k, So no need to pay current bill")
