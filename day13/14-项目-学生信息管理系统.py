'''
实现功能：
添加学生信息
查询学生信息
编辑学生信息
删除学生信息
'''
class Student:
    def add(self, **kwargs):
        f = open("./student_info", "a", encoding='utf-8')
        f.write(str(kwargs) + "\n")
        f.close()
    def check_all(self):
        '''
        查询所有的学员信息
        '''
        f = open("./student_info", "r", encoding='utf-8')
        all_stu_info = f.read()
        f.close()
        return all_stu_info

    def check(self, stu_num):
        # 1、先查询所有的学员信息
        all_stu_info = self.check_all()
        # 2、将所有的学员信息使用换行分割开 形成一个列表
        stu_info_list = all_stu_info.split("\n")
        # 3、删除最后的空字符串
        if not stu_info_list[-1]:
            del stu_info_list[-1]
        # 4、遍历所有的学员信息 查找指定的学员信息
        for stu in stu_info_list:
            # 把字符串学员信息转换为字典学员信息
            stu_dict = eval(stu)
            # 5、查找出指定的学员信息并打印
            if stu_dict["stu_num"] == stu_num:
                print(stu)

    def edit(self, **kwargs):
        # 获取学员的学号
        stu_num = kwargs['stu_num']
        # print(1, stu_num)
        # 1、先查询所有的学员信息
        all_stu_info = self.check_all()
        # 2、将所有的学员信息使用换行分割开 形成一个列表
        stu_info_list = all_stu_info.split("\n")
        # 3、删除最后的空字符串
        if not stu_info_list[-1]:
            del stu_info_list[-1]
        # 声明一个count 用于判断是否是第一次插入 如果是 则用w方法写入文件
        # 并覆盖掉以前的所有信息
        count = True
        # 4、遍历所有的学员信息 查找指定的学员信息
        for stu in stu_info_list:
            # 把字符串学员信息转换为字典学员信息
            stu_dict = eval(stu)
            # 5、查找出指定的学员信息并打印
            if stu_dict["stu_num"] == stu_num:
                stu_dict["name"] = kwargs["name"]
                stu_dict["age"] = kwargs["age"]
            # 第一次的时候count为True 则使用w的方式进行插入
            if count:
                self.write_w(stu_dict)
            # 第二次则使用追加模式进行插入
            else:
                self.add(stu_num=stu_dict["stu_num"], name=stu_dict["name"], age=stu_dict["age"])
            count = False

    def write_w(self, stu_dict):
        f = open('./student_info', 'w', encoding='utf-8')
        f.write(str(stu_dict) + "\n")
        f.close()

    def dele(self, stu_num):
        # 1、先查询所有的学员信息
        all_stu_info = self.check_all()
        # 2、将所有的学员信息使用换行分割开 形成一个列表
        stu_info_list = all_stu_info.split("\n")
        # 3、删除最后的空字符串
        if not stu_info_list[-1]:
            del stu_info_list[-1]
        count = True
        # 4、遍历所有的学员信息 查找指定的学员信息
        for stu in stu_info_list:
            # 把字符串学员信息转换为字典学员信息
            stu_dict = eval(stu)
            # 如果不是我们要删除的需要 则进行插入操作
            # 如果是则说明什么都不干
            if stu_dict["stu_num"] != stu_num:
                if count:
                    self.write_w(stu_dict)
                else:
                    self.add(stu_num=stu_dict["stu_num"], name=stu_dict["name"], age=stu_dict["age"])
                count = False


print("=========欢迎使用学生信息管理系统=========")
# 实例化学生类的对象
stu = Student()
while True:
    print("请输入您的选择：")
    checked = input("添加（A）查询（C） 编辑（E）删除（D）退出（Q）：")
    checked = checked.lower()
    if checked == "a":
        print("添加操作")
        content = input("请输入[学号 姓名 年龄]中间是一个空格：")
        print(content, type(content))
        result = content.split(" ")
        # print(result)
        stu.add(stu_num=result[0], name=result[1], age=result[2])
        print("添加学生信息成功")
    elif checked == "c":
        print("查询操作")
        flag = input("查询所有学员信息请按1，查询个人学员信息请输入学员学号：")
        if flag == "1":
            # 获取所有的学员信息
            all_stu_info = stu.check_all()
            print(all_stu_info)
            print("查询所有学员信息成功")
        else:
            # 获取单个的学员信息
            stu.check(flag)
    elif checked == "e":
        print("编辑操作")
        content = input("请输入编辑后的学员信息，学号不能变更[学号 姓名 年龄]：")
        result = content.split(" ")
        stu.edit(stu_num=result[0], name=result[1], age=result[2])
        print("编辑学员信息成功")
    elif checked == "d":
        print("删除操作")
        stu_num = input("请输入删除的学号：")
        stu.dele(stu_num)
        print("删除学员信息成功：")
    else:
        print("退出学生管理系统")
        break
