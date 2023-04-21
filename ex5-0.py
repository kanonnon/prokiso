"""
例題（スコープ）
＊＊提出不要です＊＊
"""

#%%
"""
例題１：グローバル変数
グローバル変数balanceに引数xを足す関数addAmount(x: int)を書いてください。
"""
balance = 0
def addAmount(x):
    global balance
    balance += x

addAmount(5)
print(balance)

#%%
"""
例題２：仮引数１
次のsubAmountはグローバル変数を変更するか予想しなさい。
なぜそうなるか考えてください。
"""
balance = 10
def subAmount(balance, x):
    balance -= x

print(balance)
subAmount(balance, 5)
print(balance)

# %%
"""
例題３：仮引数２
次のsubAmount2はグローバル変数を変更するか予想しなさい。
なぜそうなるか考えてください。
"""
balances = [10]
def subAmount2(balances, x):
    balances[0] -= x

print(balances)
subAmount2(balances, 5)
print(balances)

# %%
"""
例題４：仮引数３
次のconcatTextはグローバル変数を変更するか予想しなさい。
なぜそうなるか考えてください。
"""
string = "abc"
def concatText(string, x):
    string += x

print(string)
concatText(string, "def")
print(string)
# %%
