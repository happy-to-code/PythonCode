def userInfo(name, age, gender):
    """
    简单方法:::
    :param name:
    :param age:
    :param gender:
    :return:
    """
    print(f'名字是{name}，年龄{age}，性别：{gender}')


# 调用方法
userInfo("xiaoming", 20, "男")
userInfo(age=20, gender="男", name="xiaoming")
