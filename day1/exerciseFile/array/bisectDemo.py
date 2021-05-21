# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List, Any

__author__ = 'joedd'
import bisect
import sys


"""
    用bisect来搜索
    bisect(haystack, needle) 在 haystack（干草垛）里搜索
    needle（针）的位置，该位置满足的条件是，把 needle 插入这个位
    置之后，haystack 还能保持升序。也就是在说这个函数返回的位置前
    面的值，都小于或等于 needle 的值。其中 haystack 必须是一个有
    序的序列。你可以先用 bisect(haystack, needle) 查找位置
    index，再用 haystack.insert(index, needle) 来插入新值。
    但你也可用 insort 来一步到位，并且后者的速度更快一些。
"""
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

# print(NEEDLES[1])

"""
    {0:2d} {1:3d} {2:4d}是什么意思？

    format()函数
    字符串的参数使用{NUM}进行表示,
        0.表示第一个参数,
        1.表示第二个参数, 以后顺次递加;
        这里面：{0:2d} 表示第一个参数x的格式。0 代表x,:2d 表示两个宽度的10进制数显示。
               {1:3d} 表示第一个参数x*x的格式。1 代表x*x,:3d 表示三个宽度的10进制数显示。
               {2:4d} 表示第一个参数x*x*x的格式。2代表x*x*x,:4d 表示四个宽度的10进制数显示。

"""
"""
    '{0:2d} @ {1:2d} {2}{0:<2d}'

    
    {0:2d}  表示两个宽度的10进制数显示。
    {1:2d} 表示两个宽度的10进制数显示。
    
    
    print "{:.2f}".format(3.1415926) #3.14,保留小数点后两位
    print "{:+.2f}".format(3.1415926) #+3.14 带符号保留小数点后两位
    print "{:+.2f}".format(-10) #-10.00 带符号保留小数点后两位
    print "{:+.0f}".format(-10.00) #-10  不带小数
    print "{:0>2d}".format(1) #01 数字补零 (填充左边, 宽度为2)
    print "{:x<2d}".format(1) #1x 数字补x (填充右边, 宽度为4)
    print "{:x<4d}".format(10) #10xx 数字补x (填充右边, 宽度为4)
    print "{:,}".format(1000000) #1,000,000 以逗号分隔的数字格式
    print "{:.2%}".format(0.12) #12.00% 百分比格式
    print "{:.2e}".format(1000000) #1.00e+06 指数记法
    print "{:<10d}".format(10) #10 左对齐 (宽度为10)
    print "{:>10d}".format(10) #        10 右对齐 (默认, 宽度为10)
    print "{:^10d}".format(10) #    10 中间对齐 (宽度为10)

"""
#{0:<2d} 左对齐
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'


def demo(bisect_fn):
     for needle in reversed(NEEDLES):
         position = bisect_fn(HAYSTACK, needle)
         # print('postion:'+str(position))
         offset = position * ' |'
         # print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':

     if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
     else:
         bisect_fn = bisect.bisect
         # print('DEMO:', bisect_fn.__name__)
         # print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
         demo(bisect_fn)








"""

HAYSTACK1 = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]

NEEDLES1 = [0, 1, 2, 5, 8, 10, 22, 23.0, 29, 30, 31]

# bisect_left 返回的插入位置是原序列中跟被插入元素相等的元素的位置，
#              也就是新元素会被放置于它相等的元素的前面，
             
for needle in reversed(NEEDLES1):
    position = bisect.bisect_left(HAYSTACK2, needle)
    print('postion:' + str(position))
    HAYSTACK2.insert(position, needle)

print(HAYSTACK2)

# bisect_right 返回的则是跟它相等的元素之后的位置。
 

HAYSTACK2 = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]

for needle in reversed(NEEDLES1):
    position = bisect.bisect_right(HAYSTACK, needle)
    print('postion:' + str(position))
    HAYSTACK1.insert(position, needle)

print(HAYSTACK1)

"""

#用bisect.insort插入新元素
#可用 insort 来一步到位，并且后者的速度更快一些

import  random


SIZE = 7


print(random.seed(1729))

my_list: List[Any] = []
#
# for i in range(SIZE):
#     new_item = random.randrange(SIZE *2)
#     bisect.insort(my_list,new_item)
#     print('%2d->'%new_item,my_list)


"""
  insort 控制查找的范围:用lo 和 hi 两个可选参数
  insort_left，这个变体在背后用的是bisect_left
  适用范围：列表、元组、序列类型
"""

"""
　2.
  当列表不是首选时
      虽然列表既灵活又简单，但面对各类需求时，我们可能会有更好的选
    择。
      比如，要存放 1000 万个浮点数的话，数组（array）的效率要高
    得多，因为数组在背后存的并不是 float 对象，而是数字的机器翻
    译，也就是字节表述。这一点就跟 C 语言中的数组一样。
    
      再比如说，如果需要频繁对序列做先进先出的操作，deque（双端队列）的速度应该
    会更快。
    　如果在你的代码里，包含操作（比如检查一个元素是否出现
    在一个集合中）的频率很高，用 set（集合）会更合适。
    set 专为检查元素是否存在做过优化。但是它并不是序列，因为 set 是无序的。

"""

"""
　2.1 数组

      1）如果我们需要一个只包含数字的列表，那么 array.array（二进制文件比文本文件存取更高效） 比 list 更高效。
      2）数组支持所有跟可变序列有关的操作，包括 .pop、.insert 和.extend。
      3）数组还提供从文件读取和存入文件的更快的方法，如.frombytes 和 .tofile。
  
    Python 数组跟 C 语言数组一样精简。
    
    创建数组需要一个类型码，这个类型码用来表示在底层的 C 语言应该存放怎样的数据类型。
    
        比如 b 类型码代表的是有符号的字符（signed char），因此 array('b') 创建
        出的数组就只能存放一个字节大小的整数，范围从 -128 到 127，这样在
        序列很大的时候，我们能节省很多空间。
        
    而且 Python 不会允许你在数组里存放除指定类型之外的数据。

"""

from array import  array
from  random import  random

#2.1.2一个浮点型数组的创建、存入文件和从文件读取的过程
"""
    Type code   C Type             Minimum size in bytes 
        'b'         signed integer     1 
        'B'         unsigned integer   1 
        'u'         Unicode character  2 (see note) 
        'h'         signed integer     2 
        'H'         unsigned integer   2 
        'i'         signed integer     2 
        'I'         unsigned integer   2 
        'l'         signed integer     4 
        'L'         unsigned integer   4 
        'q'         signed integer     8 (see note) 
        'Q'         unsigned integer   8 (see note) 
        'f'         floating point     4 
        'd'         floating point     8 
"""
floats = array('d',(random() for i in range(10)))  # 'd' 指定的类型编码

print(floats[-1])

fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10)
fp.close()

print(floats2[-1])

print(floats2 == floats)

# for i in floats2:
#     new_item = random()
#     bisect.insort(my_list,new_item)
#     print('%2d->'%new_item,my_list)

print(floats2)
"""
  2.1.2从 Python 3.4 开始，数组类型不再支持诸如 list.sort() 这种就地排序方法。
  要给数组排序的话，得用 sorted 函数新建一个数组.
"""
#sorted(floats2,reverse=True) 这样子写
# bisect.insort(floats3,0.58251911452417136)  导致排序出错。

floats3 = array(floats2.typecode, sorted(floats2,reverse=True))

print(floats3)
bisect.insort(floats3,0.58251911452417136)
print(floats3)


floats4 = array(floats2.typecode, sorted(floats2))

print(floats4)
bisect.insort(floats4,0.58251911452417136)
print(floats4)


""" 
 2.1.3 数组与 memoryview？
  
  内存视图？
  
  Travis Oliphant 是 NumPy 的主要作者，他在回答“When should a memoryview be used?”
  （http://stackoverflow.com/questions/4845418/when-should-amemoryview-be-used/）
  
    这个问题时是这样说的：
    
        内存视图其实是泛化和去数学化的 NumPy 数组。它让你在不需要
        复制内容的前提下，在数据结构之间共享内存。其中数据结构可以
        是任何形式，比如 PIL 图片、SQLite 数据库和 NumPy 的数组,等
        等。这个功能在处理大型数据集合的时候非常重要。
        
        
    memoryview.cast 的概念跟数组模块类似，能用不同的方式读写同一块内存数据，而且内容字节不会随意移动。
    
    这听上去又跟 C 语言中类型转换的概念差不多。
    
    memoryview.cast 会把同一块内存里的内容打包成一个全新的 memoryview 对象给你。
  
"""
#利用 memoryview 精准地修改了一个数组的某个字节，这个数组的元素是 16 位二进制整数。
numbers = array('h',[-2,-1,0,1,2])

memv = memoryview(numbers)
print(str.__sizeof__ (str(0)))
# print(memv) #<memory at 0x10b70d7c8>
print(len(memv))

memv_oct = memv.cast('B')
print(memv_oct)

print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)


""" 
 2.1.4 NumPy和SciPy
    1）、NumPy 实现了多维同质数组（homogeneous array）和矩阵，
        
        这些数据结构不但能处理数字，还能存放其他由用户定义的记录。
    
    2)、SciPy  是基于 NumPy 的另一个库，它提供了很多跟科学计算有关的算法，专为线性代数、数值积分和统计学而设计。
    
        SciPy 的高效和可靠性归功于其背后的 C 和 Fortran 代码，而这些跟计算有关的部分都源自于 Netlib 库
        
   load 方法 ：利用了一种叫作内存映射的机制，它让我们在内存不足的情况下仍然可以对数组做切片。

"""
import numpy

a = numpy.arange(12)
print(a)
print(type(a)) #<class 'numpy.ndarray'>

print(a.shape) #一维数组含有12个元素

a.shape = (3,4) #指定为二维数组三行四列  X*X = 12
print(a.shape)

print(a)
#打印第三行所有元素
print(a[2])

#打印第三行第四列的元素
print(a[2][2],a[2,2])

#打印第三列所有的元素
print(a[:,3])

#把行和列交换，得到新的数组
print(a.transpose())

"""
  2.1.5双向队列和其他形式的队列
    1）、collections.deque 类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型。
  
"""
from collections import  deque

#maxlen 是一个可选参数，代表这个队列可以容纳的元素的数量，而且一旦设定，这个属性就不能修改了。
dq = deque(range(10),maxlen=10)
print(dq)


# 队列旋转操作接受一个参数n,
# 当n > 0,队列的最右边的n个元素会被移动到队列的左边，
# 当n<0，最左边的n个元素会被移动到右边

#最右边的三个元素移动到左边
dq.rotate(3)
print(dq)

#最左边的四个元素移动到右边
dq.rotate(-4)
print(dq)


#向左边添加一个元素
"""
  当试图对一个已满（len(d) == d.maxlen）的队列做尾部添加操作的时候，它头部的元素会被删除掉。
  注意在下一行里，元素 0 被删除了。
"""
dq.appendleft(-3)
print(dq)

#向右边添加一个元素
dq.append(3)
print(dq)

# 在尾部添加 3 个元素的操作会挤掉 -1、1 和 2。
dq.extend([11,22,33])
print(dq)

# extendleft(iter) 方法
# 会把迭代器里的元素逐个添加到双向队列的左边,

# 因此迭代器里的元素会逆序出现在队列里。

dq.extendleft([10,20,30,40])

print(dq)

dq.popleft()
dq.pop()
print(dq)


"""
queue
　　提供了同步（线程安全）类 Queue、LifoQueue 和
PriorityQueue，不同的线程可以利用这些数据类型来交换信息。这
三个类的构造方法都有一个可选参数 maxsize，它接收正整数作为输
入值，用来限定队列的大小。但是在满员的时候，这些类不会扔掉旧的
元素来腾出位置。相反，如果队列满了，它就会被锁住，直到另外的线
程移除了某个元素而腾出了位置。这一特性让这些类很适合用来控制活
跃线程的数量。

multiprocessing
　　这个包实现了自己的 Queue，它跟 queue.Queue 类似，是设计
给进程间通信用的。同时还有一个专门的
multiprocessing.JoinableQueue 类型，可以让任务管理变得更
方便。

asyncio
　　Python 3.4 新提供的包，里面有
Queue、LifoQueue、PriorityQueue 和 JoinableQueue，这些
类受到 queue 和 multiprocessing 模块的影响，但是为异步编程里
的任务管理提供了专门的便利。

heapq
　　跟上面三个模块不同的是，heapq 没有队列类，而是提供了
heappush 和 heappop 方法，让用户可以把可变序列当作堆队列或者
优先队列来使用。
到了这里，我们对列表之外的类的介绍也就告一段落了，是时候阶段性
地总结一下对序列类型的探索了






"""





