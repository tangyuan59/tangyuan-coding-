# list、str、bytes、tuple、...

'''
容器类型:list,tuple,collections.deque 这些序列能存放不同类型的数据

扁平类型：str、bytes、bytesarray,memoryview和array,array 这类序列只能容纳一种类型
'''

# 列表推导式和生成器推导式

symbols = "$%^&*("
codes = []
for symbol in symbols:
	codes.append(ord(symbol))
print(codes)
#列表推导式
codes = [ord(symbol) for symbol in symbols]
print(codes)

#列表推导式和filter和map的比较
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 40 ]
print(f"beyond_ascii:{beyond_ascii}")

beyond_ascii = list(filter(lambda c:c >40,map(ord,symbols)))
print(f"beyond_ascii_map:{beyond_ascii}")


# 生成器表达式 节省内存
# 使用生成器表达式计算笛卡尔积
colors = ["black","white"]
sizes = ["S","M","L"]
for tshirt in (f"{c} {s}" for c in colors for s in sizes):
	print(tshirt)

# 元组 把元组用作记录
lax_coordinates = (33.9425,-118.408056)
city,year,pop,chg,area = ("tokyo",2003,32450,0.66,8014)
traverler_ids = [("usa","31195855"),("bra","ce342567"),("esp","xda205856")]

for passport in sorted(traverler_ids):
	print("%s-%s"%passport)


# 元组--拆包
#将元组内的数据赋值给变量，要求标量数量和元组内值数量一致


## 具名元组 --collections.namedtuple  --可用来构造带名字的元组
#切片  对对象切片 s[a:b:c] 在a,b间以c为间隔进行切片
