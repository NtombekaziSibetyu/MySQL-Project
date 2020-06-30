#Ntombekazi Sibetyu
#importing the connector function that will connect python to the database
import mysql.connector

#this functon is responsible for registering new users and inserting that data into a table in the database
def register():

    print("Welcome new user.\nPlease answer the following questions to complete your registration")

    #the foolowing lines get information from the user
    fullname = input("\nPlease enter your fullname:")
    gender = input("\nPlease enter your gender,f/m:")
    age = input("\nPlease type in your age:")
    contact_no = input("\nPlease type in your cell/telephone number:")

    #connecting to the database
    mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="lifechoices_online")
    #creating an object of the database that can be use to execute commands
    myconnector = mydb.cursor()

    #sql command statement to insert values into table
    query = "insert into register_info values(%s,%s,%s,%s)"
    #the values that need to be inserted
    values = (fullname,gender,age,contact_no)

    #trying to catch an errors in the code
    try:
        #execution of the sql query
        myconnector.execute(query,values)
        #commiting the changes made to the database
        mydb.commit()
        print("Register successful")

    except:
        #print message if theres an error
        print("unsuccessful")

#calling the function
register()