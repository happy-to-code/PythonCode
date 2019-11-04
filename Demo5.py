import codecs

# 打开文件
f = codecs.open("text.txt", 'w', 'utf-8')
# 文件中写入内容
f.write("Hello World,Python! 中国加油！")
# 关闭流
f.close()
