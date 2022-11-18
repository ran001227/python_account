from email import quoprimime
from tempfile import tempdir
from unittest import registerResult, result


#定义全局变量
money = 1000000
name = None
#输入客户名称
name = input("请输入你的姓名：")
#定义查询函数
def query(show_header):
    if show_header:
        print("----------查询余额----------")
    print(f"{name}你好，你的余额为：{money}元")

#定义存款函数
def saving(num):
    global money   #money定义为全局变量
    money += num
    print("----------存款----------")
    print(f"{name}你好，你已成功存款{num}元")

#调用query函数查询余额
    query(False)
    #print(f"你现在的余额为：{money}元")

#定义取款函数
def get_money(num):
    global money
    money -= num
    print("----------取款----------")
    print(f"{name}你好，你已成功取款{num}元")

#调用query函数查询余额
    query(False)

#定义主菜单函数
def main():
    print("----------主菜单----------")
    print(f"欢迎来到爱情银行，请选择操作：")
    print("查询余额【输入1】")
    print("存款\t【输入2】")
    print("取款\t【输入3】")
    print("退出\t【输入4】")
    return input("输入你的选择：")

#设置无限循环
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("输入你要存款的金额："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("输入你要取款的金额："))
        get_money(num)
        continue
    else:
        print("退出程序")
        break
