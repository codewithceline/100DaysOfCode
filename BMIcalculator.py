
print("Welcome to The Simplest BMI calculator")

choice = input("\nWould you like to use the metric (kg) or imperial (lbs) system? (Enter 'a' for metric and 'b' for imperial):")

if choice == 'a':

    weight = input("\nEnter your weight in kg: ")
    height = input("Enter your height in m: ")
    #BMI = weight(kg)/height**2(M)
    BMI = (float(weight))/(float(height)**2)
    print("\nYour BMI is: ", BMI)

elif choice == 'b':
    weight_lb = input("\nEnter your weight in lbs: ")
    height_in = input("Enter your height in inches: ")
    weight_lb_convert = (float(weight_lb))* 0.453592
    height_in_convert = (float(height_in))* 0.0254
    BMI_Metric = weight_lb_convert/(height_in_convert**2)
    print("\nYour BMI is: ", BMI_Metric)



  

#weight_lb = input("Enter your weight in lbs: ")
#height_in = input("Enter your height in inches: ")






