# -*- coding: utf-8 -*-
"""
- ファイル名のXXXXXXXXのところは学籍番号に変更してください
- プログラム中のstudent_numberに自分の学籍番号を入れてください
"""
student_number = 62101046

"""**演習４（オプション演習）：夢の住宅購入**

PDFを読んで問題を解いてください。
"""

## 入力を求めて型変換
annual_salary = float(input('Enter your starting annual salary: '))
portion_saved =float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

## ここで計算
portion_down_payment  = 0.25
current_saving = 0
r = 0.04
current_month = 0

while current_saving <= total_cost * portion_down_payment:
    current_month += 1
    current_saving += current_saving * r / 12
    current_saving += annual_salary / 12 * portion_saved
    if  current_month % 12 == 0:
        annual_raise = 1.1
        annual_salary = annual_salary * annual_raise  
    
print('Number of months: {}'.format(current_month))