while True:
    while True:
        height = input("請輸入一個正整數以決定金字塔的高度: ")
        if height.isdigit():  # 檢查輸入是否是正整數
            com = (2 * int(height)) - 1
            break
        else:
            print("輸入值不正確，請輸入一個正整數。")

    half_com = com // 2  # 使用整數除法
    result = [f"{' ' * (half_com - i)}{'*' * (2 * i + 1)}" for i in range(half_com + 1)]
  
    print('\n'.join(result))

    keeprunning = input("是否繼續(y/n): ")
    if keeprunning.lower() not in ("y", "yes"):
      print('掰掰')
      break
