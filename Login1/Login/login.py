import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student"
)

mycur = con.cursor()

print('\nPress 1 for Register')
print('Press 2 for Login')

i = 1;k = 0
while True:
    ch = int(input('\nEnter your choice = '))

    if ch==1:
        print('\nRegister')
        name = input('Enter Your Name = ')
        email = input('Enter Email = ')
        password = input('Enter Password = ')
        contact = input('Enter Contact No. = ')
        city = input('Enter Your City = ')
        gender = input('Enter Your Gender = ')
        hobby = input('Enter Your Hobby = ')

        myqry = "insert into login (name,email,password,contact,city,gender,hobby) values (%s,%s,%s,%s,%s,%s,%s)"
        val = (name,email,password,contact,city,gender,hobby)

        mycur.execute(myqry,val)
    
        con.commit()
        print('You have registered Successfuly...!')   
        break

    elif ch==2:
        print('\nLogin')

        email = input('Email = ')
        password = input("Password = ")

        myqry = "select * from login where email = %s and password = %s"
        val = (email,password)

        mycur.execute(myqry,val)
        Email = mycur.fetchall()

        if Email:
            while True:
                print('You are login')
                id = "select id from login where email = %s"
                value = (email,)
                mycur.execute(id,value)
                pid = mycur.fetchone()
                k = pid[0]
                break
        else:
            while True:
                print('Invalid Credential...!')
                print('Enter Correct Email and Password....!')
                break
        con.commit()
        break

    elif ch<1 or ch<2 or ch>1 or ch>2:
        print('Please choose what do you want to do ? = ')
        i+=1


print('\nPress 1 for Adding contact Details')
print('Press 2 for Viewing Contact Details')
            
while True:
    o=int(input('\nWhat do you want to do next ? = '))
    
    if o==1:
        print('\nAdd Contact')  
        Name = input('Enter Name = ')
        Email = input('Enter Email = ')
        Contact = input('Enter Contact = ')
        Address = input('Enter Address = ')
    
        myqry = "insert into contact (Name,Email,Contact,Address,User_id) values (%s,%s,%s,%s,%s)"
        val = (Name,Email,Contact,Address,k)

        mycur.execute(myqry,val)
        con.commit()
        print('\nYou have added your contact detail successfully....!')
        break   
    
    elif o==2:
        print('\nView Contact') 
        myqry = "select * from login where email = %s"
        val = (email,)

        mycur.execute(myqry,val)

        mydetail = mycur.fetchall()
        for x in mydetail:
            print(x)
        break

    elif o<1 or o<2 or o>1 or o>2:
        print('Please choose what do you want to do next ?')
        i+=1

