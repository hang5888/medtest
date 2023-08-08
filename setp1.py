import csv

# 讀取 txt 檔案並處理資料
with open('test.txt', 'r') as in_file:
    lines = in_file.read().splitlines()
    data = [line.replace("][", ",").replace("[", "").replace("]", "").split(',')[1:] for line in lines]  # 選取每行的前兩項

data = [sublist for sublist in data if '789' not in sublist]

# 將處理後的資料寫入 csv 檔案
with open('output.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    for item in data:
        writer.writerow(item)  # writerow 需要一個 list 作為輸入
print(data)
