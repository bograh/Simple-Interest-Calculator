print('Welcome to simple interest calculator')
Bonus = 50

#Prompt user to input credentials
Name = input('Enter your name: ')
P = input('Enter Principal: ')
R = input('Enter Rate: ')
T = input('Enter Time: ')

#Calculate Simple Interest
SI = (int(P) * int(R) * int(T))/100

print(Name, 'your simple interest is:',SI)

#Condition for adding bonus to simple interest
if SI >= 500:
    print('Congratulations!!!', Name, 'you earned a bonus therefore your simple-interest plus bonus is:',(int(SI) + int(Bonus)))
else:
    print(Name,'you could not earn any bonus!')
