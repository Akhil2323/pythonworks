user_input=input("enter the string")

symbols_dictionary={"{": "}","[": "]", "(": ")" ,"<" : ">"}



symbol_stack=[]


top=-1

is_valid=True

for symbol in user_input:
    
   if symbol in symbols_dictionary:#symbol is an opening
        
      top+=1

      symbol_stack.append(symbol)#push symbol to stack

   elif symbol == symbols_dictionary.get(symbol_stack[top]):

      top-=1

      symbol_stack.pop()

   else:

      is_valid=False
   

if len(symbol_stack)==0 and is_valid==True:

   print("valid")

else:

   print("invalid")






