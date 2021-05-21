
# 字典一种key - value 的数据类型，使用就像我们上学用的字典，通过笔划、字母来查对应页的详细内容。
#
#
#
# 字典的特性：
#
# dict是无序的
# key必须是唯一的,so 天生去重



info = {
 'stu1':'first',
  'stu2':'sec',
 'stu3':'third'
}

print(info)

#增加
info['stu4'] = 'forth'

print(info)

#通过key删除字典中的值
# del info['stu4']
info.pop('stu4')
print(info)

#遍历字典
for key in info:
 print(key+':'+info[key])
 # print(key,info[key])

#遍历字典所有的keys
# print(info.keys())
#遍历字典所有的values
# print(info.values())

#字典转化成列表
# print(info.items())


#setdefault

info.setdefault('stu5','fifth')

#通过key修改value
info['stu2'] = 'sec2'
print(info)





