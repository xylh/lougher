# -*- coding:utf-8 -*-
import csv
import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")



def main():
    #文件读取
    json_file=open('07.json','r')
    #文件写入
    csv_file=open('7.csv','w')
    #文件读写器
    wri=csv.writer(csv_file)
    #转换成list
    data_list=json.load(json_file)
    #获取表头
    head=data_list[0].keys()
    #获取内容
    con=[]
    for  i in data_list:
        con.append(i.values())
    #写入表头
    wri.writerow(head)
    #写入内容
    wri.writerows(con)
    #关闭csv文件
    csv_file.close()

    json_file.close()
    #关闭json文件





if __name__ == '__main__':
    main()