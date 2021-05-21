menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


exit_flag = False
current_layer = menu

layers = [menu]


# while not exit_flag:
#     for k in current_layer:
#         print(k)
#         choice = input('>>:').strip()

while not  exit_flag:
    for k in current_layer:
        print(k)
        #Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        #选择输入级别
        print("change to laster", current_layer)
        layers.pop()
        #并不存在此key 继续判断
    elif choice not  in current_layer:continue
    else:
        #存在并且添加
        layers.append(current_layer)
        #下级key
        current_layer = current_layer[choice]
