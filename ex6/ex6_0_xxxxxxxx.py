# -*- coding: utf-8 -*-
"""ex6-0-XXXXXXXX.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZogAP5Mcv9j-9Xq4GrKyi6Oerren02Ru

これは例題なので提出の必要はありません

- ファイル名のXXXXXXXXのところは学籍番号に変更してください
- プログラム中にstudent_numberに自分の学籍番号を入れてください
"""

student_number = 62101046

"""Pythonの関数の仕様などをコメントに書く作法をDocstringと言い、いくつかの流派が存在する。今回はGoogleのDocstringに従って関数の仕様を定義するので、それに従って関数を実装していくこと

参考: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings


例題1: 以下の関数をDocstringに従って完成させよ
"""

def find_even(min_num: int, max_num: int):
  """min_num以上, max_num以下の整数の中から最小の偶数を返す関数

  min_num以上, max_num以下の整数の中から最小の偶数を1つ返す。もし範囲内に偶数がない場合はNoneを返す
  
  Args:
    min_num: 最小の偶数を探すときの範囲の最小値
    max_num: 最小の偶数を探すときの範囲の最大値

  Returns:
    int or None: 範囲内の最小の偶数。見つからないばあいはNone
  """
  if min_num % 2 == 0:
      return min_num
  else:
     if min_num == max_num:
         return
     else:
         return min_num + 1


"""例題2: 以下の関数をDocstringに従って完成させよ"""

def reverse_string(string: str):
  """文字列を逆にして返す関数

  引数に渡された文字列を逆にした文字列を戻り値として返す
  ただし、引数の型がstrでない場合はNoneを返すこと

  Args:
    string (str): 逆さまにしたい文字列

  Returns:
    str or None: 逆さまにされた文字列。引数の型がstr出ない場合はNone

  """
  if type(string) == str:
      new_str = ''.join(list(reversed(string)))
      return new_str
  else:
      return
