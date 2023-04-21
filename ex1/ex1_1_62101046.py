"""
- ファイル名のXXXXXXXXのところは学籍番号に変更してください
- プログラム中にstudent_numberに自分の学籍番号を入れてください
"""

student_number = 62101046

"""
例題: "student_id = 118444", "name = "金子 晋丈""の行を自分の学籍番号・名前に変更せよ。同様に、classnameの年度を今年のものへ変更せよ
"""

student_id = 62101046
name = "雨宮　佳音"
classname = "プログラミング基礎同演習2022"
Pi = 3.1415926535

print("学籍番号: %d" % student_id)
print("名前: %s" % name)
print(f"授業: {classname}")
print("円周率: {:.3}".format(Pi))

"""
演習1: 以下のXXXを式で埋め、円周率Piを用いて、半径rの円の円周の長さを求めよ。単位はrは[m]、circumferenceも[m]とするが、今の時点では気にしなくて良い
"""

Pi = 3.1415926535
r = 5
circumference = 2 * r * Pi
print(circumference)

"""
演習2: 以下のXXXを式で埋め、円周率Piを用いて半径rの円の面積を求めよ。単位はrは[m]、areaは[m^2]とするが、今の時点では気にしなくて良い
"""

Pi = 3.1415926535
r = 5
area = r ** 2 * Pi
print(area)

"""
演習3: 演習1と2の結果を単位も含めてprintしたい。例えばcircumference=10, area=100とした場合、以下のような結果にしたい

```
円周の長さ=10m
面積=100m^2
```

演習2や3の結果 (circumferenceやarea変数) はそのまま使って良いので、以下のXXXを埋めて完成させよ。

注意: 余計な文字・空白・改行は採点プログラムによって不正解と判断される可能性があるので十分に注意すること！
"""

print("演習の長さ＝" + str(circumference) + "m")
print("面積＝" + str(area) + "m^2")
