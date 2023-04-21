'''
例題

提出の必要はありません。

（１）
addとmulはそれぞれ2つの引数をとり加算と積算をする関数です。addを参考に、mulを完成させましょう。

（２）
apply_2_and_5は、任意の関数を引数にとり、2と5を当てはめた結果をprintする関数です。
apply_2_and_5を完成させてみましょう。
'''
#%%

def add(a, b):
    return a + b

#ここにmulを定義
???

def apply_2_and_5(fn):
    fn_name = fn.__name__
    print(f"関数{fn_name}に2と5を適用します。")
    result = ???
    print(f"結果は{result}です。")

#%%
'''
セル実行

Spyderには、#%%で区切られたセクション（セル）を個別に実行する機能があります。
まず上のセルを実行してから、ターミナル及びこちらのセルで、apply_2_and_5にaddとmulを適用してみましょう。
'''
apply_2_and_5(add)





#%%
'''
Pythonの小ネタ（Pythonをもっと知りたい人向け）

apply_2_and_5のように、関数を引数にとり、何らかの操作をする関数を「デコレーター」とよんでいます。
デコレーターは次のようにして任意の関数にくっつける書き方があります。以下を実行してみましょう。
一見難解に見えますが、実際には、subが定義されたとき、apply_2_and_5(sub)を実行しているだけなのです。
'''
@apply_2_and_5
def sub(a, b):
    return a - b

# %%
'''
上では、subが定義されると同時にapply_2_and_5が実行されてしまうため、使いどころが狭いのですが、
実際にはデコレーターは関数を返すことによって、呼び出し時に実行されるように記述されます。
この場合、div()の呼び出しにより、wrapper()が実行され、apply_2_and_5(div)が実行されます。
'''
def apply_2_and_5_wrapper(fn):
    def wrapper():
        return apply_2_and_5(fn)
    return wrapper

@apply_2_and_5_wrapper
def div(a, b):
    return a / b

div()

# %%
'''
上記のプログラムは、もとのdivの引数がラッパー関数の引数と異なるため、良いプログラミング例ではありません。
デコレーターの例を参考に、def wrapper(a, b)と引数を追加して「関数fn(a, b)の結果に100を足す」デコレーターを作ってみましょう。
'''
def add_100_to_result(fn):
    def wrapper(a, b):
        return ???
    return wrapper

@add_100_to_result
def mod(a, b):
    return a % b

mod(7, 3)
# %%
