import mysql.connector

conn = mysql.connector.connect(
host = '127.0.0.1', 
user = "root" , 
password = "12345678",
database = "RealEstate"
)

cursor = conn.cursor(dictionary=True)

def add_office(): 
    location = input("Enter The location of the office: ")
    location = location.title()

    cursor.execute("select officeID from Office where location = %s",
                   (location,))
    
    res = cursor.fetchone()

    if res : 
        print("This office is already exist! ")

    else : 
        cursor.execute("insert into office(location) values (%s)" , 
                       (location,))
        conn.commit()
        print("office added successfully. ")

    print("\n")

def show_office(): 
    cursor.execute("select * from office ")
    res = cursor.fetchall()
    
    for i in res : 
        print(f"{i['officeID']} : {i['location']}")

    print("\n")

def add_Employee(): 
    empName = input("Enter employee Name: ")
    show_office()
    officeID = int(input("Enter office ID: "))
    print("1- Manager")
    print("2- Employee")
    typeOfEmployee = input("Enter your choice 1 or 2: ")

    cursor.execute("insert into Employee(empName) values(%s)" ,
                   (empName.title(),))
    
    conn.commit()
    empID = cursor.lastrowid

    cursor.execute("insert into WorksIn(officeID , empID) values(%s , %s) " , 
                   (officeID, empID))
    conn.commit()
    if typeOfEmployee == "1": 
        cursor.execute("insert into Manage(officeID , empID) values(%s , %s) " , 
                    (officeID, empID))
        conn.commit()       

    print("Added successfully :)\n")    

def show_employee(): 

    cursor.execute("select * from Employee ")
    res = cursor.fetchall()
    
    for i in res : 
        print(f"{i['empID']} : {i['empName']}")

    print("\n")

def show_Manager(): 

    cursor.execute("select Employee.empID, Employee.empName from Employee inner join Manage on Employee.empID = Manage.empID;")
    res = cursor.fetchall()
    
    for i in res : 
        print(f"{i['empID']} : {i['empName']}")

    print("\n")

def add_Property(): 
    address = input("Enter The address: ")
    city = input("Enter The city: ")
    state = input("Enter The state: ")
    zip = input("Enter The zip: ")

    show_office()
    offID = int(input("Enter office ID: "))

    cursor.execute("insert into Property(address, city , state , zip , offID )" \
    "values(%s , %s,%s ,%s , %s) ", 
    (address, city,state, zip, offID))
    conn.commit()

    print("Added successfully")

def show_Property(has_owner=True): 
    if has_owner:
        cursor.execute("""
            SELECT p.propID, p.address, p.city, p.state, p.zip, p.offID
            FROM Property p
            LEFT JOIN Ownership o ON p.propID = o.propID
            WHERE o.ownerID IS NOT NULL;
        """)
    else:
        cursor.execute("""
            SELECT p.propID, p.address, p.city, p.state, p.zip, p.offID
            FROM Property p
            LEFT JOIN Ownership o ON p.propID = o.propID
            WHERE o.ownerID IS NULL;
        """)
    
    res = cursor.fetchall()

    if not res : 
        print("we don't have an Property for this\n")
        return 

    for i in res: 
        print(f"ID: {i['propID']}")
        print(f"Address: {i['address']}")
        print(f"City: {i['city']}")
        print(f"State: {i['state']}")
        print(f"ZIP: {i['zip']}")
        print(f"Office ID: {i['offID']}\n")

def add_Owner(): 
    ownerName = input("Enter owner name: ")


    show_Property(has_owner= False)

    propID = int(input("Enter propID , if it is not exist enter 0 : "))
    if propID == 0 : 
        print("Sorry we don't have any Property now ")
        return


    cursor.execute("insert into Owner(ownerName) values(%s)" , 
                   (ownerName.title(),))
    
    conn.commit()

    ownerID = cursor.lastrowid

    cursor.execute("insert into Ownership(ownerID,propID) values(%s,%s)" ,
                   (ownerID, propID) )
    
    
    
    conn.commit()

    print("Added successfully ")


print("Welcome in our company :) ")
print("---------------------------")

while True:
    print("1- add office")
    print("2- show office")
    print("3- add employee")
    print("4- show employees")
    print("5- show_Manager")
    print("6- add Property")
    print("7- show avaliable property")
    print("8- show owned Property ")
    print("9- add Owner")
    print("10- exit ")

    choice = int(input("Enter your choice (1 -> 10) : "))

    print("\n")
    if choice == 1:
        add_office() 

    elif choice == 2: 
        show_office() 

    elif choice == 3: 
        add_Employee() 

    elif choice == 4: 
        show_employee() 

    elif choice == 5: 
        show_Manager()

    elif choice == 6: 
        add_Property()

    elif choice == 7: 
        show_Property(has_owner=False)

    elif choice == 8: 
        show_Property(has_owner=True)

    elif choice == 9: 
        add_Owner() 

    elif choice == 10:  
        print("Good bye :) ")
        break 


conn.close()