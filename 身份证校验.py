# -*- coding:gbk -*- 
#S+=Sum(Ai*Wi);
#Ti[S%11]
while True:
    
    id_card=raw_input('���������֤���루�˳�����t����')      
    
    jym = str(id_card[len(id_card)-1:len(id_card)])              #ȡ�õ�18λУ����    
    if len(id_card) == 18 :
        
        x_arr = {'1': '7',
                 '2': '9',
                 '3': '10',
                 '4': '5',
                 '5': '8',
                 '6': '4',
                 '7': '2',
                 '8': '1',
                 '9': '6',
                 '10': '3',
                 '11': '7',
                 '12': '9',
                 '13': '10',
                 '14': '5',
                 '15': '8',
                 '16': '4',
                 '17': '2'}
        a=0
        for i in range(1,len(id_card),1):
            e = id_card[i-1:i]
            a = a + int(e)*int(x_arr.get(str(i)))            
        b = str(a%11)
        
        y_arr = {'0': '1',
                 '1': '0',
                 '2': 'x',
                 '3': '9',
                 '4': '8',
                 '5': '7',
                 '6': '6',
                 '7': '6',
                 '8': '4',
                 '9': '3',
                 '10': '2'}
        c = str(y_arr.get(b))                                   #У��
        
        if jym == c:                                            #��У����Ա�������
            print '������У����Ϊ',c,'��ʵ����ͬ'
        else:
            print '������У����Ϊ',c,'��ʵ�ʲ�ͬ'
 
    elif id_card == 't':
        break
    else:
        print '���֤λ������'
        
 