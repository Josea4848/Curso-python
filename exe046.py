from time import sleep
from emoji import emojize
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('\033[31m',emojize('BOOM:boom:', use_aliases=True))


