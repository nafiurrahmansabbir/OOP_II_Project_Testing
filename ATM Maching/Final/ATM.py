from Voic_Controller import speak


class ATM:
    
    def __init__(self, users):
        self.__users = users
    
    def authenticate_user(self, name, pin):
        for user in self.__users:
            if user.get_name() == name and user.authenticate(pin):
                return user
        return None
    
    def main_menu(self):
        print("Welcome to the ATM!")
        speak("Welcome to the ATM!")
        
        speak("Enter your name: ")
        name = input("Enter your name: ")
        
        speak("Enter your PIN: ")
        pin = input("Enter your PIN: ")
        
        
        user = self.authenticate_user(name, pin)
        
        if user:
            print("\n\tLogin Succesfully")
            speak("Login Succesfully")
            while True:
                print("\n1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")
                choice = input("Enter your choice: ")
                
                if choice == '1':
                    print("Your balance is:", user.get_balance())
                elif choice == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                elif choice == '3':
                    amount = float(input("Enter amount to deposit: "))
                    user.deposit(amount)
                elif choice == '4':
                    print("Thank you for using the ATM!")
                    speak("Thank you for using the ATM!")
                    break
                else:
                    print("Invalid choice. Please try again.")
                    speak("Invalid choice. Please try again.")
        else:
            print("Authentication failed. Invalid name or PIN.")
            speak("Authentication failed. Invalid name or PIN.")
