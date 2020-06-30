#Ntombekazi Sibetyu

#the function signs in the admin and verifies if the user is admin or not
def admin():

    print("Welcome admin. Please enter your login details to get admin access.")

    try:
        admin_name = input("\nEnter your admin username:")
        admin_pw = input("\nEnter admin password:")

    except ValueError:
        print("ValueError occured")

    #verifying if the given username and password is correct
    if admin_name == "lifechoices_admin" and admin_pw == "admin01":

        #if correct import and call admin_duties
        import admin_duties
        return admin_duties

    else:
        #when incorrect print message
        print("either username or password incorrect")

        #display other options
        next_move = input("""
                             1.Go back to main menu
                             2. Exit 
                             Answer:""")


        if next_move == "1":
            #when option 1 is chosen import and call the mainpage function
            from main import main_page
            return main_page

        if next_move == "2":
            #when option 2 is selected exit the programme
            exit()

#calling the function
admin()