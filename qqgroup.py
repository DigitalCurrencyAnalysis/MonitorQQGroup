#coding:utf-8
import re
from collections import Counter
import xlwt
def time():
    qq_times = []
    with open("qq1.txt", mode='r', encoding='UTF-8') as f:
        data = f.readlines()
        pa = re.compile(r"\d{1,2}:\d\d:\d\d")
        for d in data:
            times = pa.findall(d)
            if len(times)==0:
                pass
            else:
                qq_times.append(times[0])
    count_time = []
    for qq_time in qq_times:
        count_time.append(qq_time.split(':')[0])
    for i in range(0,24):
        b = 0
        for count in count_time:
            #print int(count)
            if i == int(count):
                b += 1
        sheet1.write(i,0,i)
        sheet1.write(i,1,b)
        print("%s时信息次数为%s"%(i,b))
def talker():
    names = []
    pa = re.compile(r"\d{1,2}:\d\d:\d\d")
    with open("qq1.txt", mode='r', encoding='UTF-8') as f:
        data = f.readlines()
        for d in data:
            times = pa.findall(d)
            if len(times) == 0:
                pass
            else:
                names.append(d.split(" ")[2].split("<")[0].split("(")[0])
    count = Counter(names)
    i = 0
    for key in count:
        sheet2.write(i,0,key)
        sheet2.write(i,1,count[key])
        i += 1
        print(key,count[key])


def date():
    dates = []
    pa = re.compile(r"\d{1,2}:\d\d:\d\d")
    with open("qq1.txt", mode='r', encoding='UTF-8') as f:
        data = f.readlines()
        for d in data:
            times = pa.findall(d)
            if len(times) == 0:
                pass
            else:
                dates.append(d.split(" ")[0])
    count = Counter(dates)
    i = 0
    for key in count:
        sheet3.write(i,0,key)
        sheet3.write(i,1,count[key])
        i += 1
        print(key,count[key])
if __name__ == "__main__":
    ws = xlwt.Workbook(encoding="utf-8")
    sheet1=ws.add_sheet(u"时段统计",cell_overwrite_ok=True)
    sheet2=ws.add_sheet(u"个人统计",cell_overwrite_ok=True)
    sheet3=ws.add_sheet(u"日期统计",cell_overwrite_ok=True)
    print(u"每个时段的聊天次数统计")
    time()
    print (u"每个人发言次数统计")
    talker()
    print(u"每个日期发现次数统计")
    date()
    ws.save('data_qq.xlsx')
