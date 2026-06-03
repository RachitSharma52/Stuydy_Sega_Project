import random


d1=[1,3,5,6,8]
d2=[1,4,3,6,9]

user1=0
user2=0

for i in range(6):
    print('press 1 for user 1 ,press 2 for user 2:')
    a=int(input("enter input:"))
    if(a==1):
    
        user1=random.choice(d1)+user1
        print(user1)
    elif(a==2):
      
        user2=random.choice(d2)+user2
        print(user2)
        
    else:
        print("invalid input")        
        a=int(input("enter input:"))
        
print(user1)        
print(user2)