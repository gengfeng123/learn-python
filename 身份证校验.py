# -*- coding:gbk -*- 
#S+=Sum(Ai*Wi);
#Ti[S%11]
while True:
    
    id_card=raw_input('请输入身份证号码（退出输入t）：')      
    
    jym = str(id_card[len(id_card)-1:len(id_card)])              #取得第18位校验码    
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
        c = str(y_arr.get(b))                                   #校验
        
        if jym == c:                                            #与校验码对比输出结果
            print '经计算校验码为',c,'和实际相同'
        else:
            print '经计算校验码为',c,'和实际不同'
 
    elif id_card == 't':
        break
    else:
        print '身份证位数不对'
        
 