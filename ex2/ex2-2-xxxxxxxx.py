# -*- coding: utf-8 -*-
"""
- ファイル名のXXXXXXXXのところは学籍番号に変更してください
- プログラム中のstudent_numberに自分の学籍番号を入れてください
"""
student_number = 62101046

"""**演習２：３項目ソート**

３つの整数を入力にとり、昇順に並び替えて出力するプログラムを作ってください。ビルトイン関数のmax()及びmin()を用いてもよいです（例えば、`x = max(2,4,7)`のとき、`x`には7が代入されます）。
"""

a = int(input(""))
b = int(input(""))
c = int(input(""))
sorted = None # Do not use sorted

### 以下、max_val, med_val, min_valを求めてください
max_val = max(a, b, c)
min_val = min(a, b, c)
med_val = (a + b + c) - max_val - min_val


print(min_val, med_val, max_val)