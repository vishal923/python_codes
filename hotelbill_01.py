# ....Resort customer Information......

from datetime import datetime, timedelta
n = input('enter the name: ')
u = int(input('enter the aadhar number: '))
r = input('room type, Ac/Non-Ac: ')
f = input('food type, veg/Non-veg: ')
d = int(input('number of days stayed: '))
a_in = datetime.now()-timedelta(d)
a_out = datetime.now()
price1 = int(input('enter the price of Ac room: '))
price2 = int(input('enter the price of Non-Ac room: '))
price3 = int(input('enter the price of veg food: '))
price4 = int(input('enter the price of Non-veg food: '))
if r=='Ac' and f == 'veg':
    p = (price1*d) + (price3*d)
elif r=='Ac' and f == 'Non-veg':
    p = (price1*d) + (price4*d)   
elif r=='Non-Ac' and f == 'veg':
    p = (price2*d)+(price3*d)
else:
    p = (price2*d)+(price4*d)
print()
my = 'VISHAL RESORTS'
myy = my.center(100,'*')
print(myy)
q = 'Customer information '
print("\u0332".join(q))   
print('name: ',n)
print('aadhar number: ',u)
print('room type: ',r)
print('food type: ',f)
print('duration of stay: ',d)
print('~check-in: ',a_in.strftime('%d-%m-%Y'),end=' ' )
print('\t\t\t\t\t\t\t ~check-out: ',a_out.strftime('%d-%m-%Y'))
print('Total amount: ',p)
print('-'*100)
print('\t\t\t\t Thanks for coming, please Visit again!!')
print('='*100)
