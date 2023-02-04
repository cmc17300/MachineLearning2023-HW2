#loop to print outputs from a list at odd indexes
# question 2
my_list = [10,20,30,40,50,60,70,80,90,100]
for i in range(len(my_list)):
    if(i%2 == 1):
        print(my_list[i])
