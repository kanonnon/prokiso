"""
**時間つぶし用の課題：やることリスト**

タスクの数とその依存関係のリストを入力にとり、そのすべてのタスクが実行可能か判定する関数を書いてください。

例えば、タスク1がタスク0より前に実行されなければならない場合、その依存関係は[0, 1]と表されます。

実行例
```
can_finish(2, [[1, 0]])
True
can_finish(2, [[1, 0], [0, 1]])
False
can_finish(4, [[1, 0], [2, 1], [3, 2]])
True  # 0->1->2->3 で可能
test_code(can_finish)
#テストケースに全問正解の場合メッセージが表示
```

"""

def can_finish(num_tasks, prerequisites):
    """
    引数：num_tasks: int, prerequisites: List[List[int]]
    返値：bool
    """
    pass

'''
検証用
'''
def gen_random_tasks(n, seed):
    import random
    random.seed(seed)
    prerequisites = set()
    while len(prerequisites) < n // 4 * 3:
        v1 = random.randrange(n)
        v2 = random.randrange(n)
        while v1 == v2:
            v2 = random.randrange(n)
        prerequisites.add((v1, v2))
    return list(prerequisites)

def test_code(fn):
    test_seeds = [3*n + 1 for n in range(20)]
    n = 1000
    results = []
    for test_seed in test_seeds:
        prerequisites = gen_random_tasks(n, test_seed)
        results.append(fn(n, prerequisites))
    x = "".join(map(str, results))

    import hashlib
    cypher = 214676177229716215358805913591335380330
    key = hashlib.md5(bytes(x, 'utf-8')).hexdigest()
    decrypted_hex = cypher ^ int(key, 16)
    try:
        return bytes.fromhex(hex(decrypted_hex)[2:]).decode()
    except:
        return "Decoding error"