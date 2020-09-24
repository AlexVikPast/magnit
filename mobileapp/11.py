from datetime import datetime

# dc = {'11.12.12': 1, '10.12.12': 2}
# #
# dc = dict(dc)
#
# a = max(dc.keys())
# #
# # print({k: v for k, v in dc.keys() if k == a})
# # print([k for k, v in dc.keys() if k == a])
#
# for k, i in dc.items():
#     print(k, i)

#
# d = '2020-08-20'
# datetime_object = datetime.strptime(d, '%Y-%m-%d')
# datetime_object = datetime.strptime(d, '')
# print(datetime_object.year)
#

dc = {'11.12.12': 1}
for k, v in dc.items():
    print(v)