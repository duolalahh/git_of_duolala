""" 
姓名： 姜琦
班级：信管1803
学号：0121803930115
 """
def lower_list(a=[]):#打印小写字母列表
    for i in range(97,123):
        a.append(chr(i))
    return a
def recognition(c):
    if "A"<c<"Z":
        return c.lower()
    else:
        return c 

def capital(b=[]):#打印大写字母列表
    for i in range(65,91):
        b.append(chr(i))
    return b
def kaisa():#凯撒密码
    letter=capital()
    ciphertext=[str(x) for x in range(18,50)]#打印密文列表
    sign=[' ','，','.','/',':','?']
    letter_sign=letter+sign#明文列表
    transfer=""
    print("1.加密\n2.解密")
    select=input()
    if select=='1':
        password_dict=dict(zip(letter_sign,ciphertext))#加密密码表字典
        text=input("请输入加密文本")
        for i in text:
            if i.upper() in password_dict.keys():
                i=password_dict[i.upper()]
                transfer+=i
            else:
                transfer+=i
    if select=='2':
        password_dict=dict(zip(ciphertext,letter_sign))#解密密码表字典
        text=input("请输入解密文本")
        x,y=0,2
        for i in range(1,int(1+len(text)/2)):
            a=text[x:y]#字符每两个分块
            if a in password_dict.keys():
                a=password_dict[a]
                transfer+=a.lower()
            else:
                transfer+=a.lower()
            x=y
            y=2+2*i
    return transfer
def transfer_password():#转换加密法
    transfer=""
    print("1.加密\n2.解密")
    select=input()
    a=input("请输入相关文本").replace(" ","")#去掉空格
    text_list=[]
    nums=len(a)/5
    t=len(a)%5
    if select=='1':
        for i in range(0,int(nums)):
            text_list.append(a[5*i:5*(1+i)])#字符每五个分块
        if t!=0:
            text_list.append(a[-t:])#输出余下的字符
        for i in range(0,5):
            for x in text_list:
                try:#i可能超出范围，用try避免报错
                    transfer+=x[i]
                except:
                    pass
    if select=='2':
        b=[]
        qie=int(nums+1)
        if t==0:#能凑满行的
            for i in range(0,int(nums)):
                transfer+=a[i::int(nums)]#
        if t!=0:#有余的
            for i in range(0,5):
                if i<t:
                    b.append(a[i*qie:(1+i)*qie])
                else:
                    b.append(a[i*qie+t-i:(1+i)*qie+t-i-1])
            for i in range(0,int(nums)):
                for x in b:
                    transfer+=x[i]
            for i in range(0,t):
                transfer+=b[i][int(nums)]
    return transfer
def letter_sort():
    transfer=""
    cleartext=lower_list()
    ciphertext=capital()
    print("1.加密\n2.解密")
    select=input()
    if select=='1':
        password_dict=dict(zip(cleartext,ciphertext[::-1]))
        text=input("请输入加密文本")
    if select=='2':
        password_dict=dict(zip(ciphertext[::-1],cleartext))
        text=input("请输入解密文本")
    for i in text:
        if  i in password_dict.keys():
            i=password_dict[i]
            transfer+=i
        else:
            transfer+=i
    return transfer
if __name__ == "__main__":#功能和主函数意思一致
    print("选择你所需要的加密方式")
    print("1.凯撒加密\n2.字母倒序法\n3.转换加密法\n输入q停止运行")
    while(1):
        xu=input()
        if xu=='1':
            print("凯撒加密")
            print(kaisa())
        elif xu=='2':
            print("字母排序法")
            print(letter_sort())
        elif xu=='3':
            print("转换加密法")
            print(transfer_password())
        elif xu=='q':
            break
        else:
            print("输入不合法")
        print("请再次选择，输入q停止运行")
