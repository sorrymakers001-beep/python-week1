name = "bi"
tel = 234567
print("牛"+name+str(tel))
num = 9191
salary = 52778
massage = "我的电话是：%s,我的工资是：%d"%(tel,salary)
print(massage)
num1 = 1234
num2 =3.213532
massage = "%9d,%.3f"%(num1,num2)
print(massage)
name = "洋竹公司"
stock_price = 91.91
stock_growth = 0.91
message1 = f"重庆知名户外背包公司：{name},股票价格：{stock_price}"
message2 = "经过七天的涨幅，股价达到：%.3f"%(stock_price*((1+stock_growth)**7))
print(message1)
print(message2 )
name = input("请输入你的名字：")
print(f"wc,你{name}是个大富豪")
num1 = 91
num2 = 19
result = num1  != num2
print(f"{result}")
print(f"{91>100}")
bin = True
print(f"斌是{bin}")

age = input("your age：")
if int(age) > 18:   
    print("Congratulations,you are an adult!")
else:
    print("You are still a child,please wait for a while")
print("You still  have long way to go")

print("Welcome to my backbag store")
your_spine_length = float(input("请输入你的脊柱长度："))
your_height = float(input("请输入你的身高："))
if your_spine_length < 40 and your_height < 165:
    print("You should choose GREGORY背包")
    if your_spine_length <30 :
        print("You can not go hiking with the backbag")

elif your_spine_length < 45 and your_height < 175:
    print("You should choose OSPREY背包")
elif 50<your_spine_length    < 55 and your_height < 180:
        print("You can choose Kalash")
else:
    print("You should should gou home")