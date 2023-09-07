# 读取文件内容
with open('file_to_read.txt', 'r') as f:
    text = f.read()

# 统计 "terrible" 出现的次数
count = text.count('terrible')

# 替换操作
terrible_count = 0
new_text = text
while "terrible" in new_text:
    if terrible_count % 2 == 0:
        new_text = new_text.replace("terrible", "pathetic", 1)
    else:
        new_text = new_text.replace("terrible", "marvellous", 1)
    terrible_count += 1

# 写入新文件
with open('result.txt', 'w') as f:
    f.write(new_text)

# 显示 "terrible" 出现的次数
print(f'The total times the word "terrible" appears: {count}')