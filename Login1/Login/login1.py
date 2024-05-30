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
if Email:
    while True:
        print('You are login')
        # while True:
        user_id = "select id from login where email = %s"
        value = (email,)
        mycur.execute(user_id,value)
        pid = mycur.fetchall()
        if pid:
                # while True:
            print('User_id = ',pid)
            break
        break
        # break
else:
    while True:
        print('Invalid Credential...!')
        print('Enter Correct Email and Password....!')
        break

# if login:
    # while True:
    #     user_id = "select * from login where id = %s"
    #     value = (id,)
    #     mycur.execute(user_id,value)
    #     pid = mycur.fetchall()
    #     if pid:
    #         while True:
    #             print('User_id = ',user_id)
    #             break
    #     break


# login1 = "select * from login where id = %d"
# val1 = (login1)

# mycur.execute(login1,val1)

# login1 = "insert into login (user_id)values(%d)"
# val2 = (login1)

# mycur.execute(login1,val2)