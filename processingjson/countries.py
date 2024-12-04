from json import load

f=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\json\\countries.json",encoding="utf-8")

data=load(f)

# print number of countries

# print(len(data))

# print all countries name 

all_country=[country.get("name") for country in data]

# print(all_country)

# print all regions

all_region=[country.get("region") for country in data]

# print(set(all_region)) #set is used to avoid repeated region

# print the region count 

count_region={region:all_region.count(region) for region in all_region}

# print(count_region)

# print maximum region count

max_region=max(count_region,key=lambda k:count_region.get(k))

# print(max_region,count_region.get(max_region))

# print capital of a specific country india

country_capital=[country.get("capital") for country in data if country.get("name")=="India"]

# print(country_capital)


# enter a country and print the capital

# countrys=input("enter the country")

# country_capital=[country.get("capital") for country in data if country.get("name")==countrys]

# print(country_capital)

country_border={country.get("name"):len(country.get("borders",[])) for country in data}

# print(country_border)

# print the maximum border country Name

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border_country)

# most populated country

most_populated=max(data,key=lambda country:country.get("population",[])).get("name")

# print(most_populated)

# print indian borders share countries

indian_borders=[country.get("borders") for country in data if country.get("name")=="India"][0]

for code in indian_borders:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))

