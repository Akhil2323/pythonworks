# weight_in_kg/height_in_meter**2
  
weight_in_kg=int(input("enter weight in kg:"))
 
height_in_cm=int(input("enter height in cm:"))
 
height_in_m=height_in_cm/100

bmi=weight_in_kg/height_in_m**2
 
bmi=round(bmi,2)

print(bmi)