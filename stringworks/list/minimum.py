expenses=[12000,13000,16000,11000,15000]

minimum=expenses[0]

for exp in expenses:

  if exp<minimum:

    minimum=exp

print(f"minimum expenses={minimum}")