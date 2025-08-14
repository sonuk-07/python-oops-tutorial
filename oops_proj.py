class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.logged_in = False
        self.menu()
    
    def menu(self):
        user_input = input("""welcome to chatbook! How would you like to proceed?
                        1. Login
                        2. Register
                        3. Write a post
                        4. Message to friend
                        5. Exit""")
        print("\n")
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        elif user_input == '5':
            print("Exiting chatbook. Goodbye!")
            exit()
        else:
            print("Invalid option, please try again.")
            self.menu()

    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email.split('@')[0]
        self.password = password
        print(f"User {self.username} registered successfully!")
        print("\n")
        self.menu()

    def login(self):


obj = chatbook()