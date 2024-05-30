import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student"
)

mycur = con.cursor()

# name = input('Enter Your Name = ')
# email = input('Enter Email = ')
# password = input('Enter Password = ')
# contact = input('Enter Contact No. = ')
# city = input('Enter Your City = ')
# gender = input('Enter Your Gender = ')
# hobby = input('Enter Your Hobby = ')
email = input('Email = ')
password = input("Password = ")

myqry = "select * from login where email = %s and password = %s"
val = (email,password)

mycur.execute(myqry,val)

Email = mycur.fetchall()
# print(Email)

# con.commit()
i=1

if Email:
    while True:
        print('You are login')
        break
else:
    print('Enter Correct Email and Password....!')
    i+=1




