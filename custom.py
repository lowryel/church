from datetime import datetime
# print(datetime.strftime("%A %d, %B %Y"))
from datetime import date
import time
import asyncio
# import uuid
# id = uuid.uuid4()
# print(id)
list1 = ["name","age","worth"]
list2 = ["Eugene",29,250000]
list3 = dict(zip(list1, list2))

print(list3.items())
print(time.sleep(3))
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

# print(repr(list3))

async def text():
    res = "hello".upper()
    return await res

# @text()
async def call_text():
    return await text()

print((call_text()))


from collections import Counter, deque
c = Counter(["increase", "plan", "build", "test", "deploy"])
c['monitor'] = 0

print(+c)
print(c.most_common())
total = c.total()
print(c.update(["deploy"]))
print(total)

# dech = (1, 2, 3, 4, 5)
# dequed = deque(dech)
# for ele in dequed: print(ele)
# dequed.pop()
# print(dequed)
# dequed.popleft()
# print(dequed)
# dequed.extend([8,9,7,6])
# print(dequed)
# print(list(reversed(dequed)))
# print(dequed)

