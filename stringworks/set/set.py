st=set()

st1={10,20,30}

print(type(st))

print(type(st1))

print(st1)

#duplicate not allowed

st2={10,10,20,30,40,30}#only one repeated value print bcz duplicate not allowed

print(st2)

#set does not support index

st3={10,20,10,30,40,30,"hello","hai",True}

print(st3)#it doesn't print in order


# add(obect)

color={"red","green","blue"}

color.add("yellow")

print(color)


# list convert to set

arr=[10,10,20,30,40,50,40]

st=set()


for num in arr:

    st.add(num)

print(st)

# print the common element from the two set

st1={10,20,30,40,50}

st2={10,20,60,70,80}

intersection_set=st1.intersection(st2)

print(intersection_set)

# print the union set from the set

union_set=st1.union(st2)

print(union_set)

# print differnce

difference_set=st1.difference(st2)

print(difference_set)#print only not common element from the set

# remove 50 from the set

str={10,20,30,40,50,60}

str.remove(50)

print(str)
