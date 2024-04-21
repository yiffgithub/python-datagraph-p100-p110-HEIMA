# 打开文件，指定模式为写入模式，编码为utf-8
with open('test2.txt', mode='w', encoding='utf-8') as f:
    # 写入中文内容
    f.write('你好，我是mian\n')
    f.write('这是测试\n')

# 文件自动关闭
print('文件写入完成，并已关闭。')
# 打开文件，指定模式为读取模式，编码为utf-8