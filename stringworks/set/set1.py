# print the suggestion for rahul that  not follwed in user friend

user=["rahul","rohit","kohil","rishab","sanju","pandya","siraj"]

rahul_follwer=["rohit","kohil","rishab","rahul"]

sanju_follower=["sanju","rohit","kohil"]

rahul_suggetion=set(user).difference(set(rahul_follwer))

print(rahul_suggetion)


sanju_rahul_mutual=set(rahul_follwer).intersection(set(sanju_follower))

print(sanju_rahul_mutual)