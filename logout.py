#Ntombekazi Sibetyu
#importing the connector function that will connect python to the database
import mysql.connector
import datetime

#function that handles signing in of the users
def logout():

    print("Please fill in the required details to sign out")

    try:
        #input asked from the user for signng in
        fullname = input("\nEnter your fullname:")
        sign_out = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        current_date = datetime.datetime.today().strftime("%Y-%m-%d")

    except ValueError:
        print("ValueError!")

    except TypeError:
        print("TypeError!")

    #connecting to the database
    my_db = mysql.connector.connect(host="localhost",user="root",password="1234",database="lifechoices_online")
    #creating an object of the database to execute sql commands
    my_connector = my_db.cursor()

    #sql statements to update
    query = "UPDATE online_register SET signout_time = current_timestamp() WHERE fullname =%s OR sign_in_time = current_date()"
   #values of the sql statement
    value = (fullname,)

    try:
        #executing the query
        my_connector.execute(query,value)
        #commiting the changes made
        my_db.commit()

        #message displayed when execution was successful
        print("Successfully signed out")

    except:
        #
        print("Sign in was unsuccessful")

logout()