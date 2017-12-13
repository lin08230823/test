# -*- coding: UTF-8 -*-
import csv
new_report = []
def first(dir='f:/report.txt'):                         #求每名同学的总成绩，平均并从高到低排序
    global length
    with open(dir) as f:
        for line in f.readlines():
            list = line.strip().split(' ')

            totals = 0
            count = 0
            for score in list[1:]:
                totals += int(score)                           #score为str
                count += 1
            ave = int(totals/count)

            list.append(str(totals))                           #转int为str
            list.append(str(ave))
            length = len(list)-2
            new_report.append(list)
            new_report.sort(key=lambda x:x[-1],reverse=True)   #list.sort() or newlist =sorted(list)
        return new_report



def second():
    aver = []
    for i in range(1,10):
        total = 0
        count = 0
        for list in new_report:
            count +=1
            total += int(list[i])
        ave = int(total/count)
        aver.append(str(ave))
    totals = 0
    counts = 0
    for score in aver:
        totals += int(score)
        counts += 1
    sum_aver = totals/counts
    aver.insert(0,'0')
    aver.insert(1,'平均')
    aver.append(str(totals))
    aver.append(str(sum_aver))
    return aver

def third(new_report):
    new = []
    i = 1
    for singe in new_report:
        singe.insert(0,str(i))
        i += 1
        for score in singe[2:-2]:
            if int(score)< 60:
                singe[singe.index(score)] = '不及格'
        new.append(singe)
    return new


def fouth(filename):
    fin = []
    with open(filename,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分'])
        writer.writerow(aver)
        for singe in new:
            writer.writerow(singe)


new_report = first()
aver = second()
new = third(new_report)

fouth('e:/abcdefh.csv')














