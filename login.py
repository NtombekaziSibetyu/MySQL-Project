#Ntombekazi Sibetyu
#importing the connector function that will connect python to the database
import mysql.connector
#import function that generates date and time
import datetime

#function handles signing in when called
def login():

    print("Please fill in the requirements below to sign in")

    #getting input information from user
    full_name = input("\n Enter your fullname:")
    login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #connecting to the database
    mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="lifechoices_online")
    #creating an object of the database that can be use to execute commands
    myconnector = mydb.cursor()
    #sql command statement to insert values into table
    query = "insert into online_register(fullname,sign_in_time) values(%s,%s)"
    #valuew
    values = (full_name,login_time)

    #sql command statement to insert values into table
    try:
        #executing the command
        myconnector.execute(query,values)
        #commiting the changes made
        mydb.commit()
        print("Successfully signed in")

    except:
        #message to print if theres an error
        print("Unsuccessful, you have to register before you can sign in")

#calling the function
login()