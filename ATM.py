import getpass
import string
import os
users=['user1','user2','user3']
pins=['1234','2222','3333']
amounts=[1000,2000,3000]
count=0
while True:
    user=input('\nEnter User Name:')
    user=user.lower()
    if user in users:
        if user==users[0]:
            n=0
            break
        elif user==users[1]:
            n=1
            break
        else:
            n=2
            break
    else:
        print('---------------')
        print('***************')
        print('Invalid Username')
        print('***************')
        print('---------------')
while count<3:
    print('---------------')
    print('***************')
    pin=str(getpass.getpass('Please Enter Pin:'))
    print('***************')
    print('---------------')
    if pin.isdigit():
        if user=='user1':
            if pin==pins[0]:
                break
            else:
                count+=1
                print('---------------')
                print('***************')
                print('Invalid Pin')
                print('***************')
                print('---------------')
                print()
        if user=='user2':
            if pin==pins[1]:
             break
            else:
                count+=1
                print('---------------')
                print('***************')
                print('Invalid Username')
                print('***************')
                print('---------------')
                print()
        if user=='user3':
            if pin==pins[2]:
                break
            else:
                count+=1
                print('---------------')
                print('***************')
                print('Invalid Username')
                print('***************')
                print('---------------')
                print()
    else:
        print('---------------')
        print('***************')
        print('Pin consists of 4 Digits')
        print('***************')
        print('---------------')
        count+=1
if count==3:
    print('---------------')
    print('***************')
    print('3 unsuccessful pin Attempts,Executing')
    print('!!!! your card has been locked!!!!')
    print('***************')
    print('---------------')
    exit()
print('---------------')
print('***************')
print('Login Successful,Continue')
print('***************')
print('---------------')
print()
print('---------------')
print('***************')
print(str.capitalize(user[n]),'Welcome to ATM')
print('***************')
print('------ATM system-------')
while True:
    print('---------------')
    print('***************')
    response=input('Select from following options:\nStatement_(s)\nWithdraw_(w)\nLodgement_(l)\nChange_pin(p)\nQuit_(q)\n:').lower()
    print('***************')
    print('---------------')
    valid_responses=['S','W','L','P','Q']
    response=response.lower()
    if response=='s':
          print('---------------')
          print('***************')
          print(str.capitalize(user[n]),'you have',amounts[n],'Euro on your Account.')
          print('***************')
          print('---------------')
    elif response=='w':
        print('---------------')
        print('***************')
        cash_out=int(input('Enter Amount you would like to withdraw:'))
        print('***************')
        print('---------------')
        if cash_out%10!=0:
            print('---------------')
            print('***************')
            print('Amount you would want to withdraw must to match 10 Euro notes')
            print('***************')
            print('---------------')
        elif cash_out>amounts[n]:
            print('---------------')
            print('***************')
            print('you have insufficient balance')
            print('***************')
            print('---------------')
        else:
            amounts[n]=amounts[n]-cash_out
            print('---------------')
            print('***************')
            print('your new balance is:',amounts[n],'Euro') 
            print('***************')
            print('---------------')
    elif response=='l':
        print()
        print('---------------')
        print('***************')
        cash_in=int(input('Enter amount you want to lodge:')) 
        print('***************')
        print('---------------')
        print()
        if cash_in%10!=0:
            print('---------------')
            print('***************')
            print('Amount you would want to lodge must to match 10 Euro notes')
            print('***************')
            print('---------------')
        else:
            amounts[n]=amounts[n]+cash_in
            print('---------------')
            print('***************')
            print('your new balance is:',amounts[n],'Euro') 
            print('***************')
            print('---------------')
    elif response=='p':
        print('---------------')
        print('***************')
        new_pin=str(getpass.getpass('Enter a new pin:'))
        print('***************')
        print('---------------')
        if new_pin.isdigit() and new_pin!=pin[n] and len(new_pin)==4:
            print('---------------')
            print('***************')
            new_pin=str(getpass.getpass('Confirm new pin:'))
            print('***************')
            print('---------------')
            if new_pin!=new_pin:
                print('---------------')
                print('***************')
                print('Pin Mismatch')
                print('***************')
                print('---------------')
            else:
                pins[n]=new_pin
                print('New Pin Saved')
        else:
            print('---------------')
            print('***************')
            print('New pin must consists of 4 digits\n and must be Different to previous pin')
            print('***************')
            print('---------------')
    elif response=='q':
        exit()
    else:
        print('---------------')
        print('***************')
        print('Response not valid')
        print('***************')
        print('---------------')





           


    

    

















