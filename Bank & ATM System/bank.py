import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student",
)

mycur = con.cursor()

print('1 = Saving account')
print('2 = Current account')

i=1;damount=0;wamount=0

while True:
    p=int(input('\nWhich type of account do you want to open ? = '))

    if p==1:
        account = str('Saving account')
        break
    elif p==2:
        account = str('Current account')
        break
    elif p<1 or p<2 or p>1 or p>2:
        print('Please choose your account')
        i+=1

samt=5000
camt=10000

i=1
if p==1:
    while True:
        amt=int(input('\nDeposit amount for Saving account = '))
        if amt<5000:
            print('\nDeposit minimum Rs. 5000 for opening saving account')
            i+=1
        elif amt>5000:
            print('\nYour account is opened')
            break
        elif amt==5000:
            print('\nYour account is opened')
            break

if p==2:
    while True:
        amt=int(input('\nDeposit amount for Current account = '))
        if amt<10000:
            print('\nDeposit minimum Rs. 10000 for opening current account')
            i+=1
        elif amt>10000:
            print('\nYour account is opened')
            break
        elif amt==10000:
            print('\nYour account is opened')
            break

pin=int(input('\nSet your pin of 4 digit = '))
while True:
    cpin=int(input('Confirm pin = '))

    if pin!=cpin:
        print('\nYour pin is not match')
        i+=1
    elif pin==cpin:
        print('\nYour pin is set successfully')
        break

print('\n1 = Withdraw amount')
print('2 = Deposit amount')
print('3 = Check balance')
print('4 = Exit')

while True:
    t=int(input('\nChoose transaction you want to do ? = '))
    if t==1:
        print('\nWithdraw amount')
        while True:
            pin=int(input('\nEnter your pin = '))
            if pin!=cpin:
                print('\nYour pin is not match')
                i+=1
            elif pin==cpin:
                withdraw_amt=int(input('\nEnter amount you want to withdraw = '))
                if withdraw_amt<=amt:
                    print('\nYour amount is withdrawn successfully')
                    break
                else:
                    print('\nYour amount has exceeded limit')
                    break
            
    if t==2:
        print('\nDeposit amount')
        while True:
            pin=int(input('\nEnter your pin = '))
            if pin!=cpin:
                print('\nYour pin is not match')
                i+=1
            elif pin==cpin:
                deposit_amt=int(input('\nEnter amount you want to deposit = '))
                print('\nYour amount is deposited successfully')
                break

    if t==3:
        print('\nCheck balance')
        while True:
            pin=int(input('\nEnter your pin = '))
            if pin!=cpin:
                print('\nYour pin is not match')
                i+=1
            elif pin==cpin:
                if deposit_amt!=0:
                    balance=int(amt)+int(deposit_amt)-int(withdraw_amt)
                    # print('Your balance amount is Rs.',balance)
                    i+=1
                    break
                if withdraw_amt!=0:
                    balance=int(amt)-int(withdraw_amt)+int(deposit_amt)
                    # print('Your balance amount is Rs.',balance)
                    i+=1
                    break
                if deposit_amt==0:
                    balance=int(amt)
                    print('Your balance amount is Rs.',balance)
                    i+=1
                    break
                if withdraw_amt==0:
                    balance=int(amt)
                    print('Your balance amount is Rs.',balance)
                    i+=1
                    break

    if t==4:
        print('\nExit')
        print('\nThanks for banking with us....!')
        break

myqry = "insert into Bank(account,amt,pin,withdraw_amt,deposit_amt,balance)values(%s,%s,%s,%s,%s,%s)"
val = (account,amt,pin,withdraw_amt,deposit_amt,balance)

mycur.execute(myqry,val)

con.commit()

print('\nYour data is submitted successfully....!')

