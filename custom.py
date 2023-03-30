# from datetime import datetime
# print(datetime.strftime("%A %d, %B %Y"))
# from datetime import date
# import time
# import asyncio
# import uuid
# id = uuid.uuid4()
# print(id)
# list1 = ["name","age","worth"]
# list2 = ["Eugene",29,250000]
# list3 = dict(zip(list1, list2))

# print(list3.items())
# print(time.sleep(3))
# print(list(list3.keys()))
# print(list(list3.values()))
# print(len(list3))

# iterate = iter(list3)
# for (k,v) in iterate:
#     print(zip(k,v))


# next_time = date(2023, 1, 15)
# # print(type(next_time))
# print(next_time)

# print(repr(list3))

# async def text():
#     res = "hello".upper()
#     return await res

# @text()
# async def call_text():
#     return await text()

# print((call_text()))


# from collections import Counter, deque
# c = Counter(["increase", "plan", "build", "test", "deploy"])
# c['monitor'] = 0

# print(+c, "+c: return non zero values")
# print(c.most_common())
# total = c.total()
# print(c.update(["deploy"]))
# print(total)

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

# dech = [1, 2, 3, 4, 5]
# for i in enumerate(dech):
#     print(i)
print("=====================================================")
# def gibbo(n):
#     g0=0
#     g1=1
#     if n==0:
#         return g0
#     elif n==1:
#         return g1
#     else:
#         for i in range(2, n-1):
#             c = g0-g1
#             g0 = g1
#             g1 = c
#         return g1


# # for i in range(6, 11):
# print(gibbo(100))

# This function uses a for loop to iterate through the desired range of numbers, starting with the 2nd number in the sequence(1) up to the nth number.
# You can also change the range in the for loop to get more or less numbers.

# print(ord('A'))
# for i in range(65,91):
#     print(chr(i),i)


