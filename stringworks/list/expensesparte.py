# # print  saparate expnese from the list

expenses=[12000,11000,13000,14000,15000]

for exp in expenses:

    print(exp)

# print total expense without using function

expenses=[12000,13000,16000,11000,15000]

greater=0

for exp in expenses:

  if exp>greater:

    greater=exp

print(f"largset expenses={greater}")

