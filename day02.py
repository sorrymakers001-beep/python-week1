print("ok")
num_int = str(12.9)
print(type(num_int), num_int)
print(int("91"))
print(float("91.19"))
name = "jj"
print(type(name), name)
print(99//8,"99//8=")
print("99//8=", 99//8)
num=9
num/=3
print(num)
c=float(input("请输入摄氏度："))
f=c*1.8+32
print(f"摄氏度{c}对应的华摄氏度{f}")
import math
radius = float(input("半径："))
area = radius**2*math.pi
print(f"半径{radius}的圆的面积是{area}")
money = float(input("买装备需要多少钱："))
travel_money = money+1000
print(f"去旅行要花{travel_money}元")