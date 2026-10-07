i = 0
while i<2:
    print("BIN，好帅！")
    i+=1
i = 0
sum = 0
while i<=100:
    sum  += i
    i+=1    
print(f"{sum}")
flag = True
count = 0
import random
num = random.randint(1,3)
while flag:
    count +=1
    your_num = int(input("输入数字："))
    if your_num == num:
        print("congratulations,you are right")
        flag = False
    else:
        if your_num > num:
            print("your num is bigger than answer")
        else: 
            print("your num is smaller than answer")
print(f"your times:{count}")
i = 1
while i<=5:
    print("第%d天，我想吃火锅"%i)
    i += 1
    j = 1
    while j<4:
        print(f"想吃{j}份毛肚")
        j += 1
print(f"第{i}天，终于吃上火锅了")
print("Welcome\tto\tmy\tback\tbagstore")
print("You\twill\trelish\tyour\tshopping1")

i=1
while i<=9:
    j = 1
    while j<=i:
        print(f"{i}*{j} = {i*j}\t",end='')
        j += 1
    i += 1
name = "osprey，Gregory，Kailas，Deuter，arctreryx,mountainhardware,patagonia,marmot"
k = 0
for kk in name:
    if kk == "a":
        k += 1
print(f"有{k}个a")
for l in range(5):
    print(l,end=' ')
for o in range(2,8,2):
    print(o,end=' ') 
    print("hello",end='')
p = 0
for num1 in range(1,99):
    if num1 % 2 == 0:
        p += 1
print(f"有{p}个偶数")    
i = 4   
for e in range(1,10):
    print("I want to study Python by myself.today is %d ds.Keep going"%e)
    for Q in range(1,4):
        print("I want to learn %d programs"%Q)
print(f"今天是第{i}天")

for T in range(1,10):
    for r in range (1,10):
        if r <= T:
            print(f"{r}*{T}={r*T}\t",end='')
for O in range(10):
    print("bin")
    continue
    print("so headsome")
for  W in range(1,511):
    print("kk")
    break
    print(kkk) 
         