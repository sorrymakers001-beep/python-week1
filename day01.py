print("Hello,AI")
name = "Bin"
print(f"我是{name},开始学AI")
print("我是",name)
print("ws boss")



name = input("请输入姓名：")
money = 999999

def act(x):
    global money
    if x == 1:
        print(f"您的余额为：{money}")
    elif x == 2:
        minus = float(input("您想取出的金额："))
        if minus > money:
            print("余额不足")
        else:
            money -= minus
            print(f"还剩余：{money}")
    elif x == 3:
        add = float(input("您想存入的金额："))
        money += add
        print(f"还剩余：{money}")

def recycle():
    return int(input(f"""{name},欢迎您来到银行
      余额查询：【输入1】
      取款：【输入2】
      存款：【输入3】
      退出：【输入4】
      请输入你的选择:"""))

while True:
    so = recycle()

    if so == 4:
        print("程序结束")
        break
    elif so in (1, 2, 3):
        act(so)
    else:
        print("无效选择，请重新输入")