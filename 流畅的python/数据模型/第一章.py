## 理解为什么特殊方法是对象行为一致的关键。
import collections
from math import  hypot
'''
collections  这个模块实现了特定目标的容器，以提供Python标准内建容器 dict , list , set , 和 tuple 的替代选择
'''
Card = collections.namedtuple("card",["rank","suit"])

class FrenchDeck:
	ranks = [str(n) for n in range(2,11)]+list("JAkA")
	suits = "spades diamonds clubs hearts".split()

	def __init__(self):
		self._cards = [Card(rank,suit) for suit  in self.suits
					 				for rank in self.ranks]

	# 求列表长度的魔法方法
	def __len__(self):
		return len(self._cards)

	#提供键值对方法
	def __getitem__(self, position):
		return self._cards[position]


##__repr__  __abs__ __add__ __mul__ 实现方法

class Vector:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def __repr__(self):
		return  f"Vector({self.x,self.y})"
	'''
	把对象用字符的形式表达出来
	__repr__和__str__的区别： 后者是在str() 函数才被调用的
	'''

	def __abs__(self):
		return hypot(self.x,self.y)

	def __bool__(self):
		return bool(abs(self))

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x,y)

	def __mul__(self, other):
		return Vector(self.x*other,self.y*other)

if __name__ == "__main__":
	beer_card = Card("7","diamonds")
	#print(beer_card)

	deck = FrenchDeck()
	print(f"deck的长度：{len(deck)}")
	print(f"deck[0]：{deck[0]}")
	print(f"deck[-1]：{deck[-1]}")
	# for card in deck :
	# 	print(card)

	# #reversed 反向迭代
	# for card in reversed(deck) :
	# 	print(card)
	Vector(3,4)
