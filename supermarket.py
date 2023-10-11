from datetime import datetime
name=input("Enter your name:")
#list of items
lists='''
Rice    Rs 50/kg
Sugar   Rs 30/kg
Salt    Rs 10/kg
Oil     Rs 110/litre
Paneer  Rs 120/kg
Maggie  Rs 50/kg
Boost   Rs 80/each
Shampoo Rs 20/each
Colgate Rs 50/each
'''
#Declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#Rates for items
items={'Rice':50,
'Sugar':30,
'Salt':10,
'Oil':110,
'Paneer':120,
'Maggie':50,
'Boost':80,'Shampoo':20,'Colgate':50}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your Items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
    if finalamount!=0:
        print(25*"=","Srikanth Supermarket",25*"=")
        print(30*" ","Kavali")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ",'Quantity',5*" ",'price')
        for i in range(len(pricelist)):
            print(i,10*' ',ilist[i],8*' ',qlist[i],12*' ',plist[i])
        print(75*'-')
        print(50*" ",'Totalamount:','Rs',totalprice)
        print(51*" ",'gst amount:','Rs',gst)
        print(75*"-")
        print(50*" ",'finalamount:','Rs',finalamount)
        print(75*"-")
        print(20*" ","Thanks for Visiting")
        print(75*"-")
            



