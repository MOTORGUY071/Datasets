# coded by伊玛目的门徒 多个txt提取关键信息生成csv
# coding=utf-8
import os
import pandas as pd

# 获取目标文件夹的路径
filedir = os.getcwd() + ''
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(filedir)
# 打开当前目录下的result.txt文件，如果没有则创建
post_title = []
post_content = []
post_post_author = []
post_date = []
post_date_gmt = []
post_status = []
comment_status = []
post_name = []
post_modified = []
post_modified_gmt = []
guid = []
menu_order = []
post_type = []
comment_count = []
post_parent = []

i = 0
# 先遍历文件名
for filename in filenames:
    i += 1
    print(i)

    if i > 0:
        filepath = filedir + '\\' + filename
        print(filepath[:-4])
        post_title.append(filename[:-4])

        g = open(filepath, encoding='gbk', errors='ignore')

        content = g.read()
        post_content.append(content)

        post_post_author.append('1')
        post_date.append('2019-10-13 14:04:59')
        post_date_gmt.append('2019-10-13 14:02:59')
        post_status.append('publish')
        comment_status.append('open')
        post_name.append(
            '%e4%b8%ad%e5%9b%bd%e9%82%ae%e6%94%bf%e5%82%a8%e8%93%84%e9%93%b6%e8%a1%8c%e6%9c%89%e9%99%90%e8%b4%a3%e4%bb%bb%e5%85%ac%e5%8f%b8%e6%b9%96%e5%8c%97%e7%9c%81%e5%8d%81%e5%a0%b0%e5%b8%82%e4%b8%b9%e6%b1%9f')
        post_modified.append('2019-10-13 14:06:59')
        post_modified_gmt.append('2019-10-13 14:01:40')
        guid.append('http://www.lianhanghao.xyz/quantstrategy/' + str(i + 1))
        menu_order.append('0')
        post_type.append('post')
        comment_count.append('0')
        post_parent.append('0')

print(post_title)
print(post_content[2])

df = pd.DataFrame({'post_title': post_title,
                   'post_content': post_content,
                   'post_post_author': post_post_author,
                   'post_date': post_date,
                   'post_date_gmt': post_date_gmt,
                   'post_status': post_status,
                   'post_name': post_name,
                   'post_modified': post_modified,
                   'post_modified_gmt': post_modified_gmt,
                   'guid': guid,
                   'menu_order': menu_order,
                   'post_type': post_type,
                   'comment_count': comment_count,
                   'post_parent': post_parent,
                   'comment_status': comment_status

                   })
print(df)
df.to_csv("./output.csv", encoding='utf_8_sig')
print('########导出完成############')