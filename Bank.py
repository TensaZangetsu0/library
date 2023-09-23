class Atm:
  def __init__(self):
    self.__pin=""
    self.__balance=0
    print("Welcome To The Atm")

    self.menu()

  def menu(self):
    user_input=input("""
    How would you like to proceed?
    1.Enter 1 to create pin
    2.Enter 2 to deposit
    3.Enter 3 to withdrawl
    4.Enter 4 to check_balance
    5.Enter 5 to exit 
    """) 

    if user_input=='1':
      self.create_pin()
    elif user_input=='2':
      self.deposit()
    elif user_input=='3':
      self.withdrawl()
    elif user_input=='4':
      self.check_balance()
    else:
      self.exit()

  def create_pin(self):
    self.__pin=input("Create Your pin: ")
    print("Pin created sucessfully")

    self.menu()

  def deposit(self):
    temp=input("Enter your pin")
    if temp==self.__pin:
      amount=int(input("Enter the Amount"))
      self.__balance=self.__balance + amount 
      print("Deposited Sucessfully")
    else:
      print("Incorrect pin")

    self.menu()  

  def withdrawl(self):
    temp=input("Enter your pin")
    if temp==self.__pin:
      amount=int(input("Enter the Amount"))
      if amount <= self.__balance:
        self.__balance=self.__balance-amount
        print("Withdrawl sucessfully",amount)
      else:
        print("Insufficient amounts")
    else:
      print("Incorrect pin")   

    self.menu()  

  def check_balance(self):
    temp=input("Enter your pin")
    if temp==self.__pin:
      print("Your Remaining balance",self.__balance)
    else:
      print("Incorrect pin")  

    self.menu()
  
  def exit(self):
    print("bye")
