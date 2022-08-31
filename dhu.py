# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# res_dict = dict(keys, values)
# print(res_dict)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d=dict1.copy()
d.update(dict2)
print(d)