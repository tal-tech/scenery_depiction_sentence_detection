import sys
from module.description import Description

if __name__ == "__main__":
    desc = Description()
    state, description = desc.init()
    print(state, description)
    if state < 0:
        sys.exit(0)

    sentence_list = [
        '竹子摸上去硬硬的，像一块砖头。' # 景物
        # '我的妈妈先推开门，再xiān开被子接着说：“起床了起床了。”妈妈走出了房门。', # 语言
        # '她闭着眼睛，绝美的脸庞显露出痛苦的神情', # 神态
        # '我心里像喝了蜜一样，甜滋滋的。', # 心理
        # '一枚新月如同一朵白色梨花，安静地开放在浅蓝色的天空中。', # 环境
        # '在这烟波浩渺的大海之中，屹立着一座山峰，它的形状很像笔架，因此叫它“笔架山”。' # 环境
    ]
    state, desc_info = desc.get_all_descriptions(sentence_list)
    if desc_info['num'] == 1:
        print("是景物描写")
    else:
        print("不是景物描写")

