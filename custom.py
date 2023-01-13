from datetime import datetime
# print(datetime.strftime("%A %d, %B %Y"))
from datetime import date
list1 = ["name","age","worth"]
list2 = ["Eugene",29,250000]
list3 = dict(zip(list1, list2))

print(list3.items())
print(list(list3.keys()))
print(list(list3.values()))
print(len(list3))

iterate = iter(list3)
# for (k,v) in iterate:
#     print(zip(k,v))
print(iterate.__next__())
print(iterate.__next__())
print(iterate.__next__())
try:
    print(repr(iterate.__next__()))
except StopIteration:
    print("Values exhausted")

next_time = date(2023, 1, 15)
# print(type(next_time))
print(next_time)

print(repr(list3))




