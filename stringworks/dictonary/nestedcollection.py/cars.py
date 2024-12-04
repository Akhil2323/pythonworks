cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]

# print total count of vehicles

print(f"Total vehicle=>{(len(cars))}")

# print avilable color of baleno

baleno_color=[c.get("colors") for c in cars if c.get("name")=="baleno"]

print(baleno_color)

print(baleno_color[0])# to remove two  list and print only one list

# print all brand


brands=[c.get("brand") for c in cars]

print(set(brands))

# print car names avilable in amt transmission

amt_transmission=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

print(amt_transmission)

# cars avilable in blue color

blue_color=[c.get("name") for c in cars if "blue" in c.get("colors")]

print(blue_color)

# print all transmission type

all_transmission={t for c in cars for t in c.get("transmissions")}

print(all_transmission)

# print the colors of cars 

all_color={color for c in cars for color in c.get("colors")}

print(all_color)

# print count of colors

colors=[colo for c in cars for colo in c.get("colors")]

color_count={co:colors.count(co) for co in colors}

print(color_count)

# costly cars
costly_car=max(cars,key=lambda d:d.get("price"))

print(costly_car.get("name"))

# car with minimum cost 
mincost_car=min(cars,key=lambda d:d.get("price"))


print(mincost_car.get("name"))


# sort cars wrt price
sort_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)

print(sort_car)


# sorted car with name and price

sort_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sort_car}

print(sorted_car_name)

