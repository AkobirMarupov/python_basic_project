# lst = [1,2,3,4]
#
# lst_iterator = iter(lst)
#
# print(next(lst_iterator))
# print(next(lst_iterator))
# print(next(lst_iterator))
# print(next(lst_iterator))


class Iterator:
    def __init__(self,max_n):
        self.max_n = max_n
        self.carrent = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.carrent >= self.max_n:
            raise StopIteration

        result = self.carrent ** 3
        self.carrent += 1
        return result


my_custem_iterator = Iterator(7)
new_iterator = iter(my_custem_iterator)


for i in my_custem_iterator:
    print(i)

