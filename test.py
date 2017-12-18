# -*- coding:utf-8 -*-
import random


def guess(ave=0,times=0):
    while True:
        num = random.randint(1,100)
        times += 1
        count = 1
        print('猜猜数字是几？')
        while True:

            print('第%d次' % count)
            try:
                guess_num = eval((input('请输入100以内的数字:')))
                if 0<guess_num<100:
                    if guess_num<num:
                        print('%d太小了'%guess_num)
                        count += 1
                    elif guess_num>num:
                        print('%d太大了'%guess_num)
                        count += 1
                    else:
                        print('猜中了，答案就是%d'%guess_num)
                        print('你猜中答案一共用了%d次机会'%count)
                        ave = (count+ave*(times-1))/times
                        print('你平均%.1f次猜中答案'%ave)
                        break
            except:
                pass
        answer = input('输入‘go’再玩一次，否则退出游戏：')
        if answer == 'go':
            print('新游戏')
        else:
            return ave,times
            break

def main(filename='e:/abcd.txt'):
    data_all = []
    data_name = []
    with open(filename,'r')as f:
        for line in f.readlines():
            name = line.strip().split(' ')[0]
            times = line.strip().split(' ')[1]
            ave = line.strip().split(' ')[2]
            data_name.append(name)
            data_all.append([name,times,ave])
        nm = input('请输入用户名：')
        if nm in data_name:
            print('欢迎回来%s，祝你游戏愉快'%nm)
            index = data_name.index(nm)
            ave = float(data_all[index][2])
            times = int(data_all[index][1])
            ave,times = guess(ave,times)
            data_all[index][1] = str(times)
            data_all[index][2] = str(ave)

        else:
            print('你好%s，祝你游戏愉快'%nm)
            ave,times = guess()
            data_all.append([nm,str(times),str(ave)])
    with open(filename,'w')as k:
        for each in data_all:
            i = ' '.join(each)+'\n'
            k.write(i)

if __name__ == '__main__':
    main()