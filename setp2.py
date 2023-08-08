import re
with open('test.txt', 'r') as f:
  text = f.read()

# 將文字按段落分割並移除非必要的段落
paragraphs = text.split('\n')
paragraphs = [p for p in paragraphs if p.startswith('[') and p.endswith(']')]

# 連接段落并打印
result = '\n'.join(paragraphs)
print(result)
