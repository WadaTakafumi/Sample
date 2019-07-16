class Todo:
    def __init__(self,contents,done):
        self.contents=contents
        self.done=done

todo1=Todo("起きる",True)
todo2=Todo("朝ごはんを食べる",False)
todo3=Todo("学校に行く",False)
todos=[todo1,todo2,todo3]
print(todos)
