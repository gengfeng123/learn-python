#-*- coding:utf-8 -*-

name=['����','����','С��','÷÷']
id=[1403050101,1403050102,1403050103,1403050104]
age=[19,20,21,20]
sex=['��','Ů','��','Ů']
grade=[96.6,95.2,96.3,94.1]

n=len(name)



print '��ӭʹ�ð༶��Ϣ����ϵ\n��ϵͳ��ʵ�����¹��ܣ�\n 1.���ӡ�ɾ��ѧ��\n 2.��ʾ����ѧ������ѧ�ţ��������Ա����䡢�ɼ���Ϣ\
\n 3.�޸ĵ���ѧ������\n 4.����ѧ����Ϣ\n 5.��ʾ������Ա��Ϣ�Ͱ�����Ϣ \n 6.ͳ�Ʒ���\n 7.�˳��༶�������ϵͳ'
i=input('��������Ҫ������ţ���')
if i==1:
    print '1.1 ����ѧ��\n1.2 ɾ��ѧ��'
    p=input('��������Ҫ������ţ���')
    if p==1.1:
        o=[str(raw_input('������'))]
        m=[input('ѧ�ţ�')]
        c=[input('���䣺')]
        d=[str(raw_input('�Ա�'))]
        e=[float(raw_input('�ɼ���'))]
        name.extend(o)
        id.extend(m)
        age.extend(c)
        sex.extend(d)
        grade.extend(e)
        n=len(name)	
        for i in range(n):
            print  '����:%s ѧ��:%r ����:%r �Ա�:%s �ɼ�:%f'%(name[i],id[i],age[i],sex[i],grade[i])
    elif p==1.2:
        print '�Ǻ�'
    else:
        print'�������'
elif i==2:
	for i in range(n):
		print  '����:%s ѧ��:%d ����:%d �Ա�:%s �ɼ�:%g'%(name[i],id[i],age[i],sex[i],grade[i])
elif i==5:
	print'ʹ�ñ�ϵͳ��������Ҫ�������\n������ϵ����������A4¥�´�'
elif i==6:
	print '6.1 �༶����\n6.2 �����С����\n6.3 ƽ������\n6.4 �����ͳɼ�\n6.5 ƽ���ɼ�\n6.6 ���ɼ�����'
	a=input('��������Ҫ������ţ���')
	if a==6.1:
		print 'ѧ������:',n
	elif a==6.2:
		print '�������:',max(age),'��С����:',min(age)
	elif a==6.3:
		print 'ƽ������:',sum(age)/len(age)
	elif a==6.4:
		print '��߳ɼ�:',max(grade),'��ͳɼ�:',min(grade)
	elif a==6.5:
		print 'ƽ���ɼ�:',sum(grade)/len(grade)
	elif a==6.6:
		print '0-0'
	else:
		print'�������'
elif i==7:
	print'ллʹ��'
else:
	print'�������'
	
