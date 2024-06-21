import random #Best import ever on skib
import math #Second best import ever on skib
list1 = ['1+1=2?','2+2=4?','3+3=6?','4+4=8?','5+5=10?','15+15=30?','16+16=32?','17+17=34?','18+18=36?','19+19=38?']
list2 = ['20+20=10?','6+6=2?','7+7=11?','8+8=32?','9+9=21?','10+10=0?','11+11=4?','12+12=12?','13+13=25?','14+14=13?']
lst = list1 + list2

for _ in range(5):
    value = random.choice(lst)
    print(value)
    Answer = input("Answer: ").upper()
    if(Answer == "Y"):
        if value in list1:
            print("Correct")
        else:
            print("Incorrect")
    elif(Answer == "N"):
        if value in list2:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("Enter Y or N")

