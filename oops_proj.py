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
                        5. Exit\n
                        Please enter your choice: """)
        
        if user_input == '1':
            self.login()
        elif user_input == '2':
            self.signup()
        elif user_input == '3':
            self.upload_post()
        elif user_input == '4':
            self.send_message()
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
        if self.username and self.password:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email.split('@')[0] == self.username and password == self.password:
                self.logged_in = True
                print(f"Welcome back, {self.username}!")
            else:
                print("Invalid credentials, please try again.")
        else:
            print("No user registered. Please register first.")
        self.menu()



    def upload_post(self):
        if self.logged_in:
            post_content = input("Enter your post content: ")
            print(f"Post uploaded: {post_content}")
        else:
            print("You need to log in first.")
        self.menu()

    def send_message(self):
        if self.logged_in:
            friend = input("Enter the name of your friend: ")
            message = input("Enter your message: ")
            print(f"Message sent to {friend}: {message}")
        else:
            print("You need to log in first.")
        self.menu()


obj = chatbook()