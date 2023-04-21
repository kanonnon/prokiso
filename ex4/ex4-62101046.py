# -*- coding: utf-8 -*-

"""
student_id及びファイル名のXXXXXXXXを自分の学籍番号で置き換えてください。
"""
student_id = 62101046

#%%
"""
# 演習１：ISBN
"""
def isbn(n):
    """
    引数 n: int
    返値 str
    """
    
    # 入力が9桁でない場合に、先頭の0埋めをする
    n_length = len(str(n)) # 入力された数字の桁を数える（stringにしないとlen関数が使えない）
    n = "0" * (9 - n_length) + str(n) # 9桁に満たない分だけ0を先頭に追加する
    
    # forループを使って、d1以外の桁の足し算をする
    sum = 0
    d1 = 0
    for i in range(9):
        n = str(n) # 後でn[8 - i]をやる時にstringじゃないとできないからstringにしておく
        num1 = i + 2 # かける数
        num2 = int(n[8 - i]) # nの数字列から、今回のループで使う桁の数字を取得
        sum += num1 * num2
        
    # 1から10のforループを使って、d1が何かを考える
    # 1から10を一つずつ当てはめていって、合計が11の倍数になった場合にそれがd1になる
    for guess_d1 in range(11):
        added_11_sum = 0
        added_11_sum = sum + guess_d1
        if added_11_sum % 11 == 0:
            d1 = guess_d1
            if d1 == 10: # 10のときはXにする指定がある
                d1 = "X"
        
    return  str(n) + str(d1) #string型

#%%
"""
# 演習２：文字列操作
"""
def shape_text(text, length, char):
    """
    引数 text: str, length: int, char: str(1文字)
    返値 str
    """
    # 以下にプログラムを記述。
    text_length = len(str(text))
    if text_length >= length:
        result = text[0:length]
    else:
        result = text + char * (length - text_length)
    return result #String型

#%%
"""
#演習３：Wordleを作ろう

###ステップ１

以下の四角をコピーして使ってください。
* 文字が`correct_ans`に含まれていて位置も同じ場合「🟩 」
* 文字が`correct_ans`に含まれているが位置が違う場合「🟨 」
* 文字が`correct_ans`に含まれていない場合「⬜ 」
"""
def wordle_check(correct_ans, ans):
    """
    引数 correct_ans: str, ans: str
    返値 なし
    """
    # shape_textでの文字列を修正
    ans = shape_text(ans, len(correct_ans), "?")
    
    # まずは空の文字列を用意して、ここに四角を足していく
    result = ""
    
    # ansに含まれる各文字と、correct_ansに含まれる各文字の、それぞれを照らし合わせる二重ループ
    for i in range(len(ans)): # ansに含まれる各文字についてのループ
        # まずは場所も文字も一致しているかどうかを確かめる
        ans_letter = ans[i] # ans文字列のi番目の文字を取得
        correct_ans_letter = correct_ans[i] # correct_ans文字列のi番目の文字を取得
        if correct_ans_letter == ans_letter: # 場所も文字も一致しているならば
            result += "🟩 " # 空の文字列resultに四角を足していく
        else:
            for j in range(len(correct_ans)): # correct_ansに含まれる各文字についてのループ
                correct_ans_letter = correct_ans[j] # correct_ans文字列のj番目の文字を取得
                if correct_ans_letter == ans_letter: # 文字が一致しているならば
                    result += "🟨 " # 空の文字列resultに四角を足していく
                    break
                if len(correct_ans) - 1 == j: # ループが終わるのに四角が他されていない（一致しなかった）ならば
                    result += "⬜ " # 空の文字列resultに四角を足していく
    return result

#%%
"""
###ステップ２
"""
import random
WORDLIST_FILENAME = "words.txt"
SEED = None
def load_words_of_length(length):
    """
    Returns a list of valid words of a certain length. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = sorted([word for word in line.split() if len(word) == length])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    if SEED:
        random.seed(SEED)
    return random.choice(wordlist)

def wordle_basic():
    """
    引数・返値　なし
    """
    # wordlistからある1単語を取得する
    correct_ans = choose_word(load_words_of_length(5))
    
    # 6回のループ
    for i in range(6):
        ans = input("Attempt #" + str(i+1) + ":")
        result = wordle_check(correct_ans, ans) # 上で作ったwordle_check関数をここで呼び出す
        print(result) # 結果を出力する（四角が並んで出てくる）
        if result == "🟩 🟩 🟩 🟩 🟩 " and len(correct_ans) == len(ans): # もし全一致しているならば
            print("Correct!")
            break # ゲームは終わりにするのでループを抜けるためにbreakする
        else:
            if i == 5: # 6回目ならば
                print("Correct answer was " + correct_ans)

#%%
"""
###ステップ３
"""
def binary_prefix_search(array, prefix):
    """
    引数 array: list[str], prefix: str
    返値 bool
    """
    # 初期探索範囲は配列の左端から右端まで
    left_index = 0
    right_index = len(array) - 1
    
    # prefixの文字数を取得
    prefix_length = len(prefix)

    # 結果がTrueになるまで二分探索を続けるループ
    while True:
        if right_index == left_index + 1: # right_indexとleft_indexが隣同士の数字になったならば
            # 探索範囲がなくなったとき、数字は見つからなかったものとする
            return False

        center_index = (left_index + right_index) // 2
        
        # array[center_index]で5文字の単語を取得し、[0:prefix_length]でそれをprefixと同じ文字数に短くしている
        # この操作によって、5文字以下の単語が入力された場合に対応できる
        if prefix < array[center_index][0:prefix_length]: # prefixが
            right_index = center_index
        elif prefix > array[center_index][0:prefix_length]:
            left_index = center_index
        else:
            # 探索終了
            return True

#%%
"""
###ステップ４
"""
def wordle_standard():
    """
    引数・返値　なし
    """
    wordlist = load_words_of_length(5)
    correct_ans = choose_word(wordlist)
    
    for i in range(6):
        while True:
            ans = input("Attempt #" + str(i+1) + ": ")
            if binary_prefix_search(wordlist, ans):
                break
            else:
                print("Invalid input")
        result = wordle_check(correct_ans, ans)
        print(result)
        if result == "🟩 🟩 🟩 🟩 🟩 " and len(correct_ans) == len(ans):
            print("Correct!")
            break
        else:
            if i == 5:
                print("Correct answer was " + correct_ans)
