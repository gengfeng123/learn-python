#-*- coding:utf-8 -*-

name=['张三','李四','小明','梅梅']
id=[1403050101,1403050102,1403050103,1403050104]
age=[19,20,21,20]
sex=['男','女','男','女']
grade=[96.6,95.2,96.3,94.1]

n=len(name)



print '欢迎使用班级信息管理系\n本系统可实现如下功能：\n 1.增加、删除学生\n 2.显示所有学生、的学号，姓名、性别、年龄、成绩信息\
\n 3.修改单个学生的信\n 4.查找学生信息\n 5.显示制作人员信息和帮助信息 \n 6.统计分析\n 7.退出班级管理管理系统'
i=input('请输入需要服务（序号）：')
if i==1:
    print '1.1 增加学生\n1.2 删除学生'
    p=input('请输入需要服务（序号）：')
    if p==1.1:
        o=[str(raw_input('姓名：'))]
        m=[input('学号：')]
        c=[input('年龄：')]
        d=[str(raw_input('性别：'))]
        e=[float(raw_input('成绩：'))]
        name.extend(o)
        id.extend(m)
        age.extend(c)
        sex.extend(d)
        grade.extend(e)
        n=len(name)	
        for i in range(n):
            print  '姓名:%s 学号:%r 年龄:%r 性别:%s 成绩:%f'%(name[i],id[i],age[i],sex[i],grade[i])
    elif p==1.2:
        print '呵呵'
    else:
        print'输入错误'
elif i==2:
	for i in range(n):
		print  '姓名:%s 学号:%d 年龄:%d 性别:%s 成绩:%g'%(name[i],id[i],age[i],sex[i],grade[i])
elif i==5:
	print'使用本系统请输入需要功能序号\n如想联系制作人请在A4楼下大喊'
elif i==6:
	print '6.1 班级人数\n6.2 最大最小年龄\n6.3 平均年龄\n6.4 最高最低成绩\n6.5 平均成绩\n6.6 按成绩排序'
	a=input('请输入需要服务（序号）：')
	if a==6.1:
		print '学生人数:',n
	elif a==6.2:
		print '最大年龄:',max(age),'最小年龄:',min(age)
	elif a==6.3:
		print '平均年龄:',sum(age)/len(age)
	elif a==6.4:
		print '最高成绩:',max(grade),'最低成绩:',min(grade)
	elif a==6.5:
		print '平均成绩:',sum(grade)/len(grade)
	elif a==6.6:
		print '0-0'
	else:
		print'输入错误'
elif i==7:
	print'谢谢使用'
else:
	print'输入错误'
	
