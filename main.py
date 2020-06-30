#Ntombekazi Sibetyu
#this is the first page a user sees when running the programme

#The main_page function displays the options to register,sign in/out
def main_page():

    try:
        user_choice = input("""
                        Welcome to Lifechoices online, please choose an option below
                        1.Register
                        2.Sign-in
                        3.Sign-out
                        4.Admin
                        Please enter your option number here:""")
    except ValueError:
        print("ValueError occured")
    except TypeError:
        print("TpeError occured")

    if user_choice == "1":
        #when the user choose option one the register functon s imported and called
        import register
        return register

    if user_choice == "2":
        #when the user choose option 2 the login function is impoerted and called
        import login
        return login

    if user_choice == "3":
        #when the user chose option 3 the logout function is called
        import logout
        return logout

    if user_choice == "4":
        #when the option 4 is chosen the admin function is imported and called
        import admin
        return admin

#calling the function
main_page()



