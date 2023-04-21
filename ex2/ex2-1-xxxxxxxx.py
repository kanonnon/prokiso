# -*- coding: utf-8 -*-
"""
- ファイル名のXXXXXXXXのところは学籍番号に変更してください
- プログラム中のstudent_numberに自分の学籍番号を入れてください
"""
student_number = 62101046

"""**演習１：カレンダー計算**

PDFを読んで、曜日を計算するプログラムを作ってください。
"""

y = int(input("y: "))
m = int(input("m: "))
d = int(input("d: "))

y0 = y - (14 - m) // 12
x = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + 31 * m0 //12) % 7

print(d0)