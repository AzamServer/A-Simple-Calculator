
"""
Application Name: A Simple Calculator
Application Description: The purpose of this application is to compute simple user-generated  equations. This application should be able to compute equations having integers and floats. In addition to that, this program should be able to add to, subtract from, multiply, and divide an equation.
"""

# Import colorama for output text color
from colorama import Fore

# Declare output text color to be red
print(Fore.RED, end = "")

# Print title of application in output
print("A Simple Calculator")

# Print new blank line in output
print()

# Declare list named "list" that will store the equation
list = []

# Declare boolean named "loopOne" to start loop one
loopOne = True

# Start loop one
while loopOne:

  # Ask user for number to add to the equation in output
  print("What number would you like to add to the list?");
  digit = input("> ")

  # Print new blank line in output
  print()

  # Check if user-provided number contains a dot to determine whether it is a number containing a decimal or not
  if digit.count(".") == 1:

    # Remove all dots from user-provided number in order to check for user error later
    checkDigit = digit.replace(".", "")

    # Code will excecute this if the user-provided number has a decimal and has no non-numerical characters
    if checkDigit.isdigit():

      # Stop loop one
      loopOne = False

      # Add the user-provided number to the equation
      list.append(digit)

    # Code will exceute this if the user-provided number has a decimal and has non-numerical characters
    else:

      # Print error saying that number has non-numerical characters
      print("Your decimal number contains a non-numerical number")
      print("Please try again")

      # Print new blank line in output
      print()

  # Code will exceute this if the number is an integer
  elif digit.isdigit():

    # Stop loop one
    loopOne = False
    
    # Add the user-provided number to the equation
    list.append(digit)

  # Code will exceute this if the user-provided number conatins a non-numerical character or contains two or more dots
  else:

      # Print error saying that input is not valid
      print("Your input is not valid")
      print("Please try again")

      # Print new blank line in output
      print()

# Declare boolean named "loopTwo" to start loop two
loopTwo = True

# Start loop two
while loopTwo:

  # Print equation in output
  print("Equation: ", end = "")
  for item in list:
    print(item, end = " ")
  
  # Print new blank line in output
  print()

  # Ask user on what they want to do
  print("What would you like to do?")
  print("Please add the number corresponding to what you would like to do")
  print("1) Add to list")
  print("2) Remove from list")
  print("3) Calculate")
  choice = input("> ")

  # Print new blank line in output
  print()

  # Code will exceute this if user choice is equal to 1
  if choice == "1":

    # Declare boolean named "loopThree" to start loop three
    loopThree = True

    # Start loop three
    while loopThree:

      # Ask user for number to add to the equation in output
      print("What number would you like to add to the list?")
      digit = input("> ")

      # Print new blank line in output
      print()

      # Check if user-provided number contains a dot to determine whether it is a number containing a decimal or not
      if digit.count(".") == 1:

        # Remove all dots from user-provided number in order to check for user error later
        checkDigit = digit.replace(".", "")

        # Code will excecute this if the user-provided number has a decimal and has no non-numerical characters
        if checkDigit.isdigit():

          # Stop loop three
          loopThree = False

          # Declare boolean named "loopFour" to start loop four
          loopFour = True

          # Start loop four
          while loopFour:

            # Ask user for operator to pair with newly added number
            print("What operation did you want to use before \"" + digit + "\"?")
            print("Operator examples: +, -, *, /")
            operation = input("> ")

            # Print new blank line in output
            print()

            # Code will exceute this if user-provided operator is "+" 
            if operation == "+":

              # Stop loop four
              loopFour = False

              # Add the user-provided operator to the equation
              list.append(operation)

              # Add the user-provided number to the equation
              list.append(digit)

            # Code will exceute this if user-provided operator is "-" 
            elif operation == "-":
             
              # Stop loop four
              loopFour = False

              # Add the user-provided operator to the equation
              list.append(operation)

              # Add the user-provided number to the equation
              list.append(digit)

            # Code will exceute this if user-provided operator is "*" 
            elif operation == "*":
              
              # Stop loop four
              loopFour = False

              # Add the user-provided operator to the equation
              list.append(operation)

              # Add the user-provided number to the equation
              list.append(digit)
            
            # Code will exceute this if user-provided operator is "/" 
            elif operation == "/":
              
              # Stop loop four
              loopFour = False

              # Add the user-provided operator to the equation
              list.append(operation)

              # Add the user-provided number to the equation
              list.append(digit)
            
            # Code will exceute this is user-provided operator does not match the four valid operators
            else:

              # Print error saying that input is not valid
              print("Your input in invalid!")
              print("Please try again")

              # Print new blank line in output
              print()

        # Code will exceute this if the user-provided number has a decimal and has non-numerical characters
        else:

          # Print error saying that number has non-numerical characters
          print("Your decimal number contains a non-numerical number")
          print("Please try again")

          # Print new blank line in output
          print()

      # Code will exceute this if the number is an integer
      elif digit.isdigit():

        # Stop loop three
        loopThree = False

        # Declare boolean named "loopFour" to start loop four
        loopFour = True

        # Start loop four
        while loopFour:

          # Ask user for operator to pair with newly added number
          print("What operation did you want to use before \"" + digit + "\"?")
          print("Operator examples: +, -, *, /")
          operation = input("> ")

          # Print new blank line in output
          print()

          # Code will exceute this if user-provided operator is "+" 
          if operation == "+":
            
            # Stop loop four
            loopFour = False

            # Add the user-provided operator to the equation
            list.append(operation)

            # Add the user-provided number to the equation
            list.append(digit)

          # Code will exceute this if user-provided operator is "-" 
          elif operation == "-":
                        
            # Stop loop four
            loopFour = False

            # Add the user-provided operator to the equation
            list.append(operation)

            # Add the user-provided number to the equation
            list.append(digit)

          # Code will exceute this if user-provided operator is "*"
          elif operation == "*":
                        
            # Stop loop four
            loopFour = False

            # Add the user-provided operator to the equation
            list.append(operation)

            # Add the user-provided number to the equation
            list.append(digit)

          # Code will exceute this if user-provided operator is "/"
          elif operation == "/":
                        
            # Stop loop four
            loopFour = False

            # Add the user-provided operator to the equation
            list.append(operation)

            # Add the user-provided number to the equation
            list.append(digit)

          # Code will exceute this is user-provided operator does not match the four valid operators
          else:

            # Print error saying that input is not valid
            print("Your input is not valid!")
            print("Please try again")

            # Print new blank line in output
            print()

      # Code will exceute this if the user-provided number conatins a non-numerical character or contains two or more dots
      else:

        # Print error saying that input is not valid
        print("Your input is not valid")
        print("Please try again")

        # Print new blank line in output
        print()
  
  # Code will exceute this if user choice is equal to 2
  elif choice == "2":

    # Check to see if equation had only one number to avoid errors later
    if(len(list) == 1):

      # If equation only has one number, print an error saying that user cannot remove numbers from the equation when only one number is present in output
      print("You cannot remove from the list when your equation only had 1 intger")
      print("Please add more integers and try again")

      # Print new blank line in output
      print()

      # Declare boolean named "loopThree" to prevent errors later
      loopThree = False

    # Code will exceute this if the equation has more than one number
    else:

      # Declare boolean named "loopThree" to start loop three
      loopThree = True

    # Start loop three
    while loopThree:

      # Ask user what number they would like to remove from the equation in output and print all numbers in equation in output
      print("What number would you like to remove?")
      print("Please enter the number corresonding to the number you would like to remove")
      choiceNumber = 2
      for item in list:
        if choiceNumber % 2 == 0:
          print(str(int(choiceNumber/2)) + ") " + str(item))
          choiceNumber = choiceNumber + 1
        else:
          choiceNumber = choiceNumber + 1
      choice = input("> ")

      # Print new blank line in output
      print()

      # Check if user-given option is valid
      if choice.isdigit():
        if int(choice) < len(list):

          # Stop loop three
          loopThree = False

          # Count to index in which number set for removal is in
          index = -2
          for i in range(int(choice)):
            index = index + 2

          # Code will exceute this if number set for removal is the first number
          if index == 0:

            # Remove first number along with the operator after the first number
            for i in range(2):
              list.pop(index)
          
          # Code will exceute this if number set for removal is after first number
          else:

            # Remove number along with the operator before the  number
            list.pop(index)
            list.pop(index-1)
        
        # Code will exceute this if user-given option given if not an option
        else:

          # Print error saying that input is not valid
          print("Your input is not valid")
          print("Please try again")

          # Print new blank line in output
          print()

      # Code will exceute this if the user-provided number conatins a non-numerical character or is a number containing a decimal
      else:

        # Print error saying that option is not an integer
        print("Your input is not an integer")
        print("Please try again")

        # Print new blank line in output
        print()

  # Code would reach here is user input is equal to 3
  elif choice == "3":

    # Declare str named "equation" to store equation in a String
    equation = ""

    # Add equation to str "equation" using for loop
    for item in list:
      equation = equation + item + " "

    # Print "Result:" in output 
    print("Result:")

    # Print str "equation" and and equal sign in output
    print(equation, end = "= ")

    # Calculate  and print equation in output
    print(eval(equation))

    # Close loopTwo
    loopTwo = False

  # Code would reach here if user input is invalid
  else:

    # Alert user that input is invalid in output
    print("Your input is invalid! Please try again!")

    # Declare new blank line in output
    print()