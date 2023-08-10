import re
import csv

# 讀取 txt 檔案並處理資料
with open('test.txt', 'r') as in_file:
    lines = in_file.read().splitlines()

regex = re.compile(r'\[(.*?)\]')  # 定義用來查找方括號内容的正則表達式
data = [regex.findall(line)[1:] for line in lines if line.strip()]  # 應用正則表達式，並選取除了第一項以外的所有項

# 從資料中移除含有 '789' 的子列表
data = [sublist for sublist in data if '789' not in sublist]
for n in data:
  #data.append(data[n][0]+data[n][3])
  print(n)

# 將處理後的資料寫入 csv 檔案
with open('output.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    for item in data:
        if item:  # 只有當 item 不是空的時候才寫入
            writer.writerow(item)  # writeorw 需要一個 list 作為輸入

print(data)
