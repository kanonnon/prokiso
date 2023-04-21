"""
- ファイル名のXXXXXXXXのところは学籍番号に変更してください
- プログラム中にstudent_numberに自分の学籍番号を入れてください
"""

student_number = 62101046

"""演習1: シーザー暗号の実装

- シーザー暗号とは、アルファベットの文字列を与えられたとき、それぞれ3文字分ずつ前にずらす暗号である。
- 例えばDは「D -> C -> B -> A」とずらしてAと変換され、Cは「C -> B -> A -> Z」とずらしてZと変換される。
- 従って"DC"という文字列が与えられた場合、出力は"AZ"となる。

コンソール入力で与えられた大文字のアルファベットの文字列をシーザー暗号にかけた結果を出力するようなプログラムを作成したい。以下のforループの中身に記述する形で実装せよ。ちなみにコンソールから与えられる文字列が大文字のアルファベット以外である可能性は考えなくて良いものとする。

入力・出力の例:
```
> DC # 入力
AZ
```

ヒント:
- ord()関数は与えた文字のUnicodeを整数値で返す
- chr()関数はUnicode整数を与えると対応した文字列を返す

使用例:
```
> print(ord('A'))
65

> print(chr(65))
A
```
"""

message = input()
new_message = ""
for m in message:
  # ここに実装を書いていく
  num_message = ord(m)
  if num_message > 67:
    num_new_message = num_message - 3
  else:
    num_new_message = num_message + 26 -3
  new_message += chr(num_new_message)
      
print(new_message)
