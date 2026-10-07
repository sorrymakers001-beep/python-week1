name_list = [["hoka","osprey"],["gregory,kailas","patagonia"],"acg","a","a"]
name1 = list("marmot")
print(name_list[0][-1])
index = name1.index("o")
print(f"下标值为：{index}")
name_list[2] = "duter"
name_list.insert(1,"chamel")
name_list.append("puma,adidas")
name_list.extend(name1[1])
del name1[5]
name1.pop(4)
name1.remove("m")
name1.clear()
print(f"列表{name_list}")
print(name1)
print(name_list.count("a"),len(name_list))
index1 = 0
while index1 < len(name_list):
    ele = name_list[index1]
    print("元素为：%s"%ele)
    index1 += 1
for W in name1:
    print(f"元素为：{W}")
num_list = [1,2,3,4,5,6,7,8]
ind = 0
o_shu = []
while ind < len(num_list):
    index2 = num_list[ind]
    if index2 % 2 == 0:
       o_shu.append(index2)
    ind += 1
print(f"{num_list}中，偶数为：{o_shu}")
day1 = "happy"
goodday = day1.replace("h","H")
print(goodday)
str = "12kailas,mummut,arcteryx,patagonia21"
str_list = str.split(",")
print(str_list)    
print(str.strip("12"))   
i_list = [1,2,3,4,5,6,7,8,9,]
print(i_list[1:5:2])
my_set = {7,7,6,1,1,2,3,4,5,4,5,6}
my_set.add(9)
my_set.remove(2)
my_set.pop()
print(my_set)
set1 = {2,3,4,6,7,4,2,5,6,4,3,5,6,2,3}
set2 = {2,3,4,1,1,2,4,6,9,9,8}
set3 = set2.difference(set1)
set2.difference_update(set1)
set4 = set1.union(set2)
print(set3,set2,set1,set4)
print(max(set3),min(set1),list(set2))
the_dict = {"A":{"语文":90,"数学":90},"B":{"语文":91,"数学":92},"C":{"语文":98,"数学":99}}
stu_score = the_dict[input("你所想要的人查询的分数：")]
special_score = the_dict["A"]["语文"]
the_dict.pop("B")
keys = the_dict.keys()
print(f"分数为：{stu_score}") 
print(special_score)
print(f"姓名：{keys}")
for O in the_dict:
    if the_dict[O]["语文"] < 100:
        the_dict[O]["语文"] += 1
print(the_dict)
        