class MyIter:
    def __init__(self, objs):
        self.index = 0
        self.objs = objs

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.objs):
            raise StopIteration

        value = self.objs[self.index]
        index = self.index
        self.index += 2
        return (index, value)

my_iter = MyIter(['Spring', 'Summer', 'Fall', 'Winter'])
for i in my_iter:
    print(i)
