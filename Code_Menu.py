print ("What do you want to do?")
print ("1. Multiplication Table")   
print ("2. Factorial")
print ("3. Fibonacci Series")
print ("4. Prime Numbers")
print ("5. Odd Numbers")
print ("6. Even Numbers")
print ("7. Exit")

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num = int (input("Enter the number for the multiplication table: "))
        terms = input("Enter how many terms (default 10): ")
        if terms == "":
            terms = 10
        else:
            terms = int(terms)
            
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, terms + 1):
            print(f"{num} × {i} = {num * i}")
    
    elif choice == 2:
        num = int(input("Enter a number to find the factorial: "))
        factorial = 1
        if num < 0:
            print("Factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1, num + 1):
                factorial = factorial * i
            print(f"The factorial of {num} is {factorial}")
            
    elif choice == 3:
        num = int(input("Enter the number of terms for the Fibonacci Series: "))
        n1, n2 = 0, 1
        count = 0
        if num <= 0:
            print("Please enter a positive integer")
        elif num == 1:
            print("Fibonacci Series upto", num, ":")
            print(n1)
        else:
            print("Fibonacci Series:")
            while count < num:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
                
    elif choice == 4:
        num = int(input("Enter a number to find the prime numbers: "))
        print(f"Prime numbers upto {num}:")
        for i in range(2, num + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
                
    elif choice == 5:
        num = int(input("Enter a number to find the odd numbers: "))
        print(f"Odd numbers upto {num}:")
        for i in range(1, num + 1):
            if i % 2 != 0:
                print(i)
                
    elif choice == 6:
        num = int(input("Enter a number to find the even numbers: "))
        print(f"Even numbers upto {num}:")
        for i in range(1, num + 1):
            if i % 2 == 0:
                print(i)
    
    elif choice == 7:
        print("Exiting the program...")
        break
    
    else:
        print("Invalid choice. Please enter a valid choice.")