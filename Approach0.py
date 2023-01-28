import mysql.connector

# Get the connection with MySQL server
cnx = mysql.connector.connect(host= '127.0.0.1', password='root',user='root')
cursor = cnx.cursor()
cursor.execute("use systemdesign")

# Set all fields as empty initially
cursor.execute("update seats set user_id = null")
cnx.commit()

print("welcome to airlines")
print()

# Currently we book for only 4 users. Filling seat number for 120 users is time consuming.
for i in range(1,5):
    seat = int(input("select seat no. = "))
    print(seat)
    cursor.execute(f"Update seats set user_id={i} where id = {seat} ")
cnx.commit()
cursor.execute("select id from seats where user_id is not null")
BookedSeats=[]
for i in cursor:
    BookedSeats.append(i[0])
booked = 1
for i in range(6):
    for j in range(20):
        if booked in BookedSeats:
            print("x ",end="")
        else:
            print(". ", end="")
        booked += 1
    if i==2:
        print()
        print()
    print()