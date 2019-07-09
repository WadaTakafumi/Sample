class car():
    def exclaim(self):
        print("I am a car")

class yugo(car):
    def exclaim(self):
        print("I am a yugo")

    def need_a_push(self):
        print("A little help")

t1=car()
t2=yugo()
t2.need_a_push()
t1.need_a_push()
