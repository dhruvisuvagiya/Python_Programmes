import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'data'
)

cur = con.cursor()

# Name = input('Name = ')	
# Email = input('Email = ')	
# Contact = input('Contact = ')	
# Gender = input('Gender = ')	
# Hobby = input('Hobby = ')
# Religion = input('Religion = ')
# City = input('City = ')
# State = input('State = ')
# Nationality = input('Nationality = ')

# qry = 'insert into form1 (Name,Email,Contact,Gender,Hobby,Religion,City,State,Nationality) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# val = (Name,Email,Contact,Gender,Hobby,Religion,City,State,Nationality)

qry = "select * from form1 where hobby = 'reading'"
cur.execute(qry)
form = cur.fetchall()
print(form)

# for x in form:
#     print(x)

con.commit()

print("Your data is submitted successfully......!")