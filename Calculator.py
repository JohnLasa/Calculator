
last_answer = None


#functions

def add(num1, num2):
    global last_answer
    last_answer= num1 + num2
    print(f"Result: {last_answer}")
#f allows me to use expression within a string when in {}

def subtract(num1, num2):
    global last_answer
    last_answer=num1-num2
    print(f"Result: {last_answer}")
    
def mulitply(num1, num2):
    global last_answer
    last_answer=num1*num2
    print(f"Result: {last_answer}")
def divide(num1,num2): 
    global last_answer
    if num2 == 0:
        print("not allowed")
    else:
        last_answer=num1/num2
        print(f"Result: {last_answer}")   
    

while True:
    print("Input EXIT to quit")
    choice = input("Input operation to proceed: ")
    
    if choice in ["add", "subtract", "multiply", "divide"]:
            # Ask the user if they want to reuse the last answer
            if last_answer is not None:
                print(f"Last answer: {last_answer}")
                use_last = input("Do you want to use the last answer as the first number? (yes/no): ").lower()
                if use_last == "yes":
                    num1 = last_answer
                else:
                    num1 = float(input("Enter the first number: "))
            else:
                num1 = float(input("Enter the first number: "))

            # Get the second number
            num2 = float(input("Enter the second number: "))

    if choice == "add":
        add(num1,num2)
    elif choice == "subtract":
        subtract(num1, num2)
    elif choice == "multiply":
        mulitply(num1,num2)
    elif choice == "divide":
        divide(num1, num2)
    elif choice == "EXIT":
        break 
    else:
        print("what did you put in???")
