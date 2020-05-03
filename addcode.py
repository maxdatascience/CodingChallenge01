import timeit
import fileinput

...

# main section
lines = [line.strip() for line in list(fileinput.input())]
events = [Event(line.split()[0], int(line.split()[1]), int(line.split().[2])) for line in lines]
active_businesses = find_active_businesses(events)
for biz_id in active_businesses:
    print(biz_id)

start = timeit.timeit()
for cycle in range(100000):
    print(find_active_busineses(events))
stop = timeit.timeit()
print(f'\n\n{stop-start}')

