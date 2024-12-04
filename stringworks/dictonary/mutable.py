# create a dictionary product with keys id,title,price,brand and add expire date

product={"id":12,"title":"facewash","price":120,"brand":"himalayan"}

product["exp.date"]="12-04-2024"
 
print(product)


product["offer"]=5

print(product)

#add offer as 10 if offer exist else add 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)


