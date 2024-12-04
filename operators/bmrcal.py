weight=int(input("enter the weight in kg:"))

height=int(input("enter the height in cm:"))

age=int(input("enter the age:"))

gender=input("enter the gender:").lower()

print(weight,height,age,gender)

if gender=="male":
   
   bmr=10*weight+6.25*height-5*age+5

elif gender=="female":
   
   bmr=10*weight+6.25*height-5*age-161                                                                                                                                                                                                                                                                                                                                     


else:
   print("***please enter valid gender***")


print(bmr)

activity_level=int(input("""
                   select activity level:
                      press 1 for sedentary
                         press 2 for lightly active
                         press 3 for moderatly active
                         press 4 for very active
                         press 5 for extra active
                         """))

if activity_level==1:
   
   calories=bmr*1.2

elif activity_level==2:

     calories=bmr*1.375

elif activity_level==3:
   
    calories=bmr*1.55

elif activity_level==4:
     
     calories=bmr*1.725

elif activity_level==5:
    
    calories=bmr*1.9

else:
    print("***selecet valid number***")

print(f"total number of calories you need in order to maintain current weight={calories}")

target_weight=int(input("enter weight to reduce in kg:"))

duration=int(input("enter duration in week:"))

calories_deficit=target_weight*7700

days=duration*7

daily_calories=calories_deficit/days

print(f"daily calories needed to reduce={daily_calories}")


