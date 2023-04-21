# -*- coding: utf-8 -*-

"""
student_id及びファイル名のXXXXXXXXを自分の学籍番号で置き換えてください。
"""
student_id = XXXXXXXX

#%%
"""
# 演習１：ISBN
"""
def isbn(n):
    """
    引数 n: int
    返値 str　
    """
    # 以下にプログラムを記述。
    return XXX #string型


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
    return XXX #String型


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
    pass # 以下にプログラムを記述。この行は削除すること。


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
    pass # 以下にプログラムを記述。この行は削除すること。


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

    while True:
        if ?:
            # 探索範囲がなくなったとき、数字は見つからなかったものとする
            return False

        center_index = ?
        if ?:
            right_index = ?
        elif ?:
            left_index = ?
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
    pass # 以下にプログラムを記述。この行は削除すること。
