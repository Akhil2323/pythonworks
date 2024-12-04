signal=input("enter the signal:").lower()

if signal=="red":
    print("stop")

elif signal=="yellow":
    print("wait")

elif signal=="green":
    print("go")

else:
    print("wrong signal")