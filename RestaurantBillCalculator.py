#Build a program that calculates each person's individual bill after a group meal 
print("Welcome to The Tip Calculator\n")
bill = float(input("How much is the total bill?\t"))
tip = float(input("\nWould you like to give a 10, 15, or 20 percent tip?\t"))
num_people = float(input("\nHow many people are splitting the bill?\t"))
total_bill = ((tip/100) + 1) * bill
final_bill = round(float(total_bill),2)
final_bill = "{:.2f}".format(final_bill) #to make sure the value prints with 2 decimal places especially when there are zero
bill_per_person = round((float(final_bill) / num_people),2)
print(f"\nYour final bill is ${final_bill} and each person pays ${bill_per_person}")







