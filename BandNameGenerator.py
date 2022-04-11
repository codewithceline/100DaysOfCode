#1. Create a greeting for your program.
print("Welcome To The World's Simplest Band Name Generator!\n\nMy name is Celine.")
print("\nHello" + " " + input("\nWhat may I call you?\t") + "!" +" "+ "Thanks for stopping by.\n\nI will need some basic information from you to proceed." + " " + "Is that okay with you?")

consent = input("\n(Please enter yes or no)\t")
if consent == "yes":
  print("\nAlright, Let's get started.")
  #2. Ask the user for the city that they grew up in.
  name_city = input("\nWhat city did you grow up in?\t")

#3. Ask the user for the name of a pet.
  name_pet = input('\nWhat is the name of your most loved pet?\t')
#4. Combine the name of their city and pet and show them their band name.
  str(name_city)
  str(name_pet)
  print('\nYour Band name is' +" "+ "The" +" "+ name_city+" "+name_pet)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
else:
  print("\nI understand."+" "+"Thank you for your time," + " " + "hope to see you again soon.")
