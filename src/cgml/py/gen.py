import datetime as dt

#
# def daterange(s, e, fmt="%Y-%m-%d"):
#     for n in range(int((dt.datetime.strptime(e, fmt) - dt.datetime.strptime(s, fmt)).days)+1):
#         yield start_date + dt.timedelta(n)
#
# start_date = dt.date(2013, 1, 1)
# end_date = dt.date(2015, 6, 2)
# for single_date in daterange('2013-01-01', "2015-6-2"):
#     print(single_date.strftime("%Y-%m-%d"))
#

a = lambda i: [dt.datetime.strptime(s, "%Y-%m-%d") + dt.timedelta(n) for s, idx in i for n in range(idx)]

print(a(('2013-01-01', 10)))
