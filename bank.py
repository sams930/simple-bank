# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
# 

balance = 0

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':

        choice2 = int(input("cik lielu jūs gribat depozītu? izvēlaties summu."))
        


        balance = balance + choice2
        pass
    elif choice == '2':

        choice3 = int(input("cik jūs gribat izņemt no konta?izvēlaties summu."))


        if choice3 > balance:
            print("nav naudas")
        else:
            balance = balance - choice3  

        pass
    elif choice == '3':

        print("jūsu balance ir " + str(balance))

        pass
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
