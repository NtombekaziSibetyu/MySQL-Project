#Ntombekazi Sibetyu
#importing the connector function that will connect python to the database
import mysql.connector

#function that displays what the admin can do and does those tasks
def duties():

    print("Welcome admin.Please choose an option from below")

    try:
        #displaying the options of tasks an admin can do
        duty = input("""
                    1.Add user
                    2.Remove user
                    3.View users info
                    4.View all sign-in/out
                    
                    Answer:""")

    except ValueError:
        print("ValueError!")

    #connecting to the database
    mydb = mysql.connector.connect(host="localhost",user="lifechoices_admin",password="admin01",database="lifechoices_online")
    #creating an object of the database that can be use to execute commands
    myconnector = mydb.cursor()

    if duty == "2":
        #when option 2 is chosen th message will be displayed
        user = input("\n Please type in the fullname of the user you want to delete:")

        #sql command statement to delete user
        query ="delete from registration_info where fullname = %s"

        #value of the sql command statement
        values = (user,)
        admin_values = ("delete user",user)

        try:
            #3executing the command statement
            myconnector.execute(query,values)
            #commiting the changes made in the database
            mydb.commit()
            #message that will be displayd if there is no errors
            print("Successfully removed user")

            myconnector.execute("insert into admin(date,changes_made,user_affected) values(current_timestamp(),%s,%s)",admin_values)
            mydb.commit()

        except:
            #mssage that will be displayed when there is an error
            print("Failed to delete user")

    if duty == "1":
        #input that will b asked from user when option1 is chosen
        user = input("\n Please type in the fullname of the user you want to add:")
        gender = input("\nTheir gender, m/f: ")
        age = input("\nAge:")
        contact_no = input("\nOne contact number:")

        #sql command statement to add a user
        query = "insert into register_info values(%s,%s,%s,%s,current_date())"
        #values of the sql statement
        values =(user,gender,age,contact_no)
        admin_values = ("added user",user)

        try:
            #executing the sql command statement
            myconnector.execute(query,values)
            #commiting to the changes made
            mydb.commit()
            #messagee displayed when there are no errors
            print("Successfuly added user")

            myconnector.execute("insert into admin(date,changes_made,user_affected) values(current_timestamp(),%s,%s)",admin_values)
            mydb.commit()

        except:
            #message displayed when there was an error in execution
            print("Failed0")

    if duty == "3":
        #when option 3 is chosen
        #the select * sql statement will be executed
        query = "select * from register_info"
        #executing command
        myconnector.execute(query)
        #gettng the result of the command statement
        db = myconnector.fetchall()

        print("\nRegistered users information\n")
        #for loop to print the records in a new line
        for record in db:
            print(record)

    if duty == "4":
        #sql command statment to display all contents of the table
        query = "select * from online_register"
        #executing the query
        myconnector.execute(query)
        #fetching the output of the sql command
        db = myconnector.fetchall()
        print("\nAll sign-in and sign-outs\n")

        #printing the records in a new line
        for record in db:
            print(record)

#calling the function
duties()