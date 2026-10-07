datas = range(1,9)
def English_Learning(datas):
    print("Keep learning ,you will succeed")
English_Learning(2)
def add(x,y):
    result = (x + y)*10
    return result
r = add(2,2)
print("计算结果为：%s"%r)
def temp(x):
    if x<= 37.5:
        print("You are healthy")
    else:
        print("You need a quarantine")
temp(37)
def money_check(money):
    if money > 1000:
        return"SUCCESS"
    return None
k = money_check(900)
if not k :
    print("a poor men")
def fun_a():
    print(1)
def fun_b():
    fun_a()
    print(2)
fun_b()
num = 100
def test():
    global num 
    num = 1000
    print(num)
print (test(),num) 

name = (input("请输入姓名："))
money = 999999
def act(x):
    global money
    if x == 1:
        print(f"您的余额为：{money}")
    elif x == 2:
        minus = input("您想取出的金额：")
        money -= float(minus)
        print(f"还剩余：{money}")
    elif x == 3:
        add = input("您想存入的金额：")
        money += float(add)
        print(f"还剩余：{money}")
def recycle():
      return int((input(f"""{name},欢迎您来到银行
      余额查询：【输入1】
      取款：【输入2】
      存款：【输入3】
      退出：【输入4】
      请输入你的选择:""")))
    
while True:
    so = recycle()
    if so == 4:
           print("程序结束")
           break
    elif so in (1, 2, 3):
        act(so)
    else:
        print("无效选择，请重新输入")