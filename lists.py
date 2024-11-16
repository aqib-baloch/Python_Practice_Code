"""list is mutable , we can perefoorm a methods or function on the list
and we use [] for lists:
"""
#lists = [3,5,6,7,33,55,77,22,66,44,976]
# max = lists[0];
# for number in lists:
#     if number > max:
#         max = number;
# print(max)

# from functools import reduce
# heights = [100, 2, 300, 10, 11, 1000]
# max_height = reduce(max, heights)
# print(max_height)

list = [44,4,5,5,6,3,7,8,9,10,11,11,33,44,33]
uniques=[]
for number in list:
    if number not in uniques:
        uniques.append(number)
print(uniques)
uniques.sort();
print(uniques);



     
        

 