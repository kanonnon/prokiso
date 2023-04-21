"""
~~~ 工夫したこと ~~~
・flow()は関数の再帰を繰り返すため、実行に時間がかかる。vertical_flow()を実行してから、それでもパーコレートしなかったものについて、flow()を実行した。
・_flow()を再帰的に呼び出す前に、すでにパーコレートしているかどうかを確かめ、していたら再帰をやめるよう実装したが、パーコレートしているかを確かめるのにも実行時間がかかったため、これは取り入れなかった
・パーコレートしているかどうか確かめるvertically_percolates（）とpercolates（）では、1箇所でもパーコレートしていたらループを抜けて実行を早くするようにしている
・閾値を求めるのに二分探索を利用して、効率的に値の範囲を狭められるようにした
"""

import numpy as np
import sys
sys.setrecursionlimit(1500)
SEED = None

def generate_percolator(n, p):
    if SEED:
        np.random.seed(SEED)
    return np.random.binomial(1, p, n*n).reshape(n, n).astype(bool).tolist()


def vertical_flow(isOpen):
    """
    引数：isOpen: list[list[bool]]
    返値：list[list[bool]]
    """
    # isOpen行列の、行列の大きさを取得する
    n = len(isOpen)
    
    # isFull行列を初期化する
    isFull = []
    for i in range(n):
        isFull.append([False] * n)
    
    # 垂直に開放しているのか、forループでで調べる
    for i in range(n): #行列の左から右に向かうforループ
        for j in range(n): #行列の上から下に向かうforループ
            if isOpen[j][i] == True:
                isFull[j][i] = True
            else:
                break # 対象のsiteがFalseのときは、それより下のsiteは調べないのでbreakする
    return isFull


def vertically_percolates(isOpen):
    """
    引数：isOpen: list[list[bool]]
    返値：bool
    """
    # バーコレートしているかを表すBool型変数（初期値はFalseでパーコレートしてたらTrueにする）
    percolates = False
    
    # isOpen行列の、行列の大きさを取得する
    n = len(isOpen)
    
    # isFullを生成する
    isFull = vertical_flow(isOpen)
    
    # 最下部の列を検査して、パーコレートしているか確かめる
    for i in range(n):
        if isFull[n-1][i] == True:
            percolates = True
            break
        
    return percolates


def _flow(isOpen, isFull, i, j):
    """
    引数：isOpen: list[list[bool]], i: int, j: int
    返値：None
    """
    
    # isOpen行列の、行列の大きさを取得する
    n = len(isOpen)

    # iとjの境界条件を満たさないならreturn
    if not (0 <= i < n and 0 <= j < n):
        return
        
    # isOpen[i][j]がOpenでないならreturn
    if isOpen[i][j] == False:
        return
    
    # isFull[i][j]がFullならreturn
    if isFull[i][j] == True:
        return

    # isFull[i][j]をTrueに設定
    isFull[i][j] = True
    
    # site[i+1][j], site[i][j+1], site[i][j-1], site[i-1][j]に対して_flowを呼び出す
    _flow(isOpen, isFull, i+1, j)
    _flow(isOpen, isFull, i, j+1)     
    _flow(isOpen, isFull, i, j-1)
    _flow(isOpen, isFull, i-1, j)


def flow(isOpen):
    """
    引数：isOpen: list[list[bool]]
    返値：list[list[bool]]
    """
    # isOpen行列の、行列の大きさを取得する
    n = len(isOpen)
    
    # isFull行列を初期化する
    isFull = []
    for i in range(n):
        isFull.append([False] * n)
        
    # 最上部のsiteすべてについて、_flowを呼び出す
    for i in range(n):
        _flow(isOpen, isFull, 0, i)
        
    # isFullをreturn
    return isFull


def percolates(isOpen):
    """
    引数：isOpen: list[list[bool]]
    返値：bool
    """
    # バーコレートしているかを表すBool型変数（初期値はFalseでパーコレートしてたらTrueにする）
    percolates = False
    
    # isOpen行列の、行列の大きさを取得する
    n = len(isOpen)
    
    # isFullを生成する
    isFull = flow(isOpen)
    
    # 最下部の列を検査して、パーコレートしているか確かめる
    for i in range(n):
        if isFull[n-1][i] == True:
            percolates = True
            break
        
    return percolates


def evaluate_percolation(n, p, trials):
    """
    引数：行列の大きさ n: int, 開放率 p: float, 試行回数 trials: int
    返値：パーコレーション確立 float
    """
    count = 0
    
    # trials回数試行するforループ
    for i in range(trials):
        isOpen = generate_percolator(n, p)
        if vertically_percolates(isOpen):
            count += 1
        elif percolates(isOpen):
            count += 1
    
    probability = count / trials
    return probability


if __name__=="__main__":
    p_left = 0.58
    p_rigtht = 0.62
    for i in range(10):
        p_center = (p_left +  p_rigtht) / 2
        probability = evaluate_percolation(100, p_center, 1000)
        if probability >= 0.5:
            p_rigtht = p_center
        else:
            p_left = p_center
    print(p_center)
    

run_time = "49sec"
p_th = 0.5924608993530274