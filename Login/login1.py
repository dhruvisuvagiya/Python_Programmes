import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'student'
)

cur = con.cursor()

k=0
print('\n')
print('Register')
print('Login')

while True:
    n = int(input('\nEnter your choice = '))

    if n==1:
        print('\nRegister\n')
        name = input('Enter Name = ')
        email = input('Enter Email = ')
        password = input('Enter Password = ')

        qry = 'insert into login (name,email,password) values (%s,%s,%s)'
        val = (name,email,password)

        cur.execute(qry,val)
        con.commit()

        print('Your data is submitted successfully...!')
        break

    elif n==2:
        print('\nLogin\n')
        email = input('Enter Email = ')
        password = input('Enter Password = ')

        qry = 'select * from login where email = %s and password = %s'
        val = (email,password)

        cur.execute(qry,val)
        com = cur.fetchall()

        if com:
            while True:
                print('You are login successfully..!')
                qry = 'select * from login where email = %s'
                val = (email,)
                com = cur.fetchone()
                k = com[0]
                break
        else:
            while True:
                print('Enter correct Email and Password....!')
                break
            break

print('\nPress 1 for adding contact details')
print('Press 2 for viewing contact details')

while True:
    ch = int(input('Please select your choice = '))

    if ch==1:
        name = input('Enter Name = ')
        email = input('Enter Email = ')
        contact = input('Enter Contact = ')
        city = input('Enter City = ')

        qry = 'insert into contact (name,email,contact,city,user_id) values (%s,%s,%s,%s,%s)'
        val = (name,email,contact,city,k)

        cur.execute(qry,val)
        con.commit()
        break

    elif ch==2:
        qry = "select * from login where email = %s"
        val = (email,)

        cur.execute(qry,val)

        detail = cur.fetchall()
        for x in detail:
            print(x)
        break


