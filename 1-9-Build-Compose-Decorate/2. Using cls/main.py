class Counter:

    count = 0
    
    def __init__ (self) :
        
        Counter.count += 1

    @classmethod
    def get_count(cls):

        return f"Number of object created: {cls.count}"
        

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

print(Counter.get_count())