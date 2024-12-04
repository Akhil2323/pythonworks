def poll(age):

    assert age>18,"invalid age"

    print("voted")

try:
 
 poll(15)

except Exception as e:
   
   print(e)