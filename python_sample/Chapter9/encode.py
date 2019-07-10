import json

# テスト用のクラス、メソッド付き
class MyClass:
    def my_method(self):
        return True

# テスト用のクラス、ネストして使う用
class ChildClass:
    pass

parent = MyClass()
child = ChildClass()
child.value1 = 'value'
child.value2 = 11
parent.child = child
parent.childList=[child, child, child]

# 以下のような構造になっている
# MyClass{
#     child = ChildClass{
#         value1:'value1',
#         value2:11
#     }
#     childList=[child, child, child]
# }

# ここがポイント
def default_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError

# 作成したメソッドを指定してdumps
print(json.dumps(parent, default=default_method, indent=2))