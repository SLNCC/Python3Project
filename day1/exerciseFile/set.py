# 集合是一个无序的，不重复的数据组合，它的主要作用如下：
#
#     1.去重，把一个列表变成集合，就自动去重了
#     2.关系测试，测试两组数据之前的交集、差集、并集等关系




s = set([3,5,7,8])  #创建一个数值集合
print(s)

t = set("Hello")   #创建一个唯一字符的集合



print(t)

#并集
a = s|t
print(a)

#交集
st =   set('helloworld')
b = t&st
print( b)

# 求差集（项在t中，但不在s中）

c = t - s
print(c)

d = s-t
print(d)

# 对称差集（项在t或s中，但不会同时出现在二者中）
vae = s^t
print(vae)

# 添加一项
# s.add('hehe')
print(s)
# 添加多项
t.update([1,2,3,4,5,6,7,8])
print(t)

# 使用remove()可以删除一项：
t.remove(1)
print(t)
# set 的长度

print(len(t))
# 测试 x 是否是 s 的成员
print('e' in t)
# 测试 x 是否不是 s 的成员
print(1 not in t)

# 测试是否 s 中的每一个元素都在 t 中
# equitRelust = s.issubset(t)
# equitRelust = s <= t
# print(equitRelust)

# 测试是否 t 中的每一个元素都在 s 中
# equitRelust = s.issuperset(t)
# equitRelust =  s >= t
# print(equitRelust)

# 返回一个新的 set 包含 s 和 t 中的每一个元素
#并集
# print(s|t)
# print(s.union(t))

#返回一个新的 set 包含 s 和 t 中的公共元素
#交集
# print(s.intersection(t))
# print(s&t)


# 返回一个新的 set 包含 s 中有但是 t 中没有的元素
print(s,t)
# print(s.difference(t))
# print(s - t)

# 返回一个新的 set 包含 s 中有但是 t 中不重复的元素

# print(s.symmetric_difference(t))
# print(s ^ t)

# 返回 set “s”的一个浅复制
t_copy = t.copy()
t.add(10)
t_copy.update(['a','b','c'])
print(t_copy,t)

