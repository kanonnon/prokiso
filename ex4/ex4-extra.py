"""**力試し課題：カレンダー再び**

この課題は提出しないでください。

この課題の難易度は中級です。プログラミング初学者でもいままでの知識で解くことができるので、積極的に挑戦してください。

問題：以下のようなカレンダーを出力する関数drawCalenderを作ってください。

テストケース：
```
drawCalender(2020, 2)
2020/2
 S  M Tu  W Th  F  S
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29

drawCalender(2000, 2)
2000/2
 S  M Tu  W Th  F  S
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 

drawCalender(2100, 2)
2100/2
 S  M Tu  W Th  F  S
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 
```
"""

# こちらに自由に関数を定義してよい。

def drawCalender(year, month):
    pass # 以下にプログラムを記述。この行は削除すること。




"""**暇つぶし用課題：いい（１１）感じのn進数**

この課題は提出しないでください。

問題：3以上の整数$x$の$n$進数表現を$(x)_n$と表すとき、$(x)_n$がすべて1で表現されることを「いい感じになる」と定義します。$(x)_n$がいい感じになる最小の$n$を求めてください。なお、$x < 10^{18}, n >= 2$である。

例：
$$(13)_{10} → (111)_3$$
$$(15)_{10} → (1111)_2$$
$$(20)_{10} → (11)_{19}$$
したがって、
```
calc_smallest_good_n(13)
3
calc_smallest_good_n(15)
2
calc_smallest_good_n(20)
19
```
必要に応じて、以下の関数を用いても良い。
```
import math
math.log(a, b) # bを底とするaの対数を返す。
```
テストケース：
```
calc_smallest_good_n(23227344339325621)
12345
check_answer(calc_smallest_good_n)
# テストケースに全問正解の場合、メッセージが現れます
```
"""

import math

def check_answer(fn):
    import hashlib
    test_input = [23227344339325621, 13247354345325761, 9668886503657665, 
                  75047317648499560, 85037317649971934, 28531167061]
    x = "".join(map(str, map(fn, test_input)))
    cypher = 113362408063145597568669130889891273767
    key = hashlib.md5(bytes(x, 'utf-8')).hexdigest()
    decrypted_hex = cypher ^ int(key, 16)
    try:
        return bytes.fromhex(hex(decrypted_hex)[2:]).decode()
    except:
        return "Decoding error"