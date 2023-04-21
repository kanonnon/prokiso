"""
- ファイル名のXXXXXXXXのところは学籍番号に変更してください
- プログラム中にstudent_numberに自分の学籍番号を入れてください
"""

student_number = 62101046

"""演習3

与えれた自然数以下の素数を全て並べたい。以下の書きかけのプログラムを完成させよ。ただしコンソールから与えられる値が「2以上の自然数」以外を示す可能性は考慮しなくて良い

実装のヒント
- 最も愚直にやるのであれば、与えられた自然数以下の値全てに対して「自分が自分以下の全ての自然数のどれかひとつで割り切れる場合があるかどうか」を判断すれば良い
- forの2重ループが使える

入力・出力の例
```
> 7 # 入力
2
3
5
7
```
"""

n = int(input())
# 以下に実装を書いていく
for i in range(2, n):
  for j in range(2, i+1):
    if i % j == 0:
      if i == j:
          print(i)
      else:
          break