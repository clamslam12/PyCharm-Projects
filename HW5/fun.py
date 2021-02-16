phoneL = []
e = True
while True:

    print("Welcome to Perfect 10 Nails Salon")
    custPhone = int(input("Please enter your phone number:"))
    if custPhone not in phoneL:
        phoneL.append(custPhone)
        print("Your number has been saved!")
    elif custPhone in phoneL:
      e = True
      while e:
         print("Welcome back!")
         print("Please choose your service:")
         print("1. Manicure")
         print("2. Pedicure")
         print("3. Eyebrows")
         print("4. Exit")
         selection = int(input("Enter a number:"))
         if selection == 1:
            print("$25; +20 points")
         elif selection == 2:
            print("$35; +25 points")
         elif selection == 3:
            print("$45; +30 points")
         else:
            e = False



