# queue

from collections import deque

# push
bank = deque(["Shafayet", "Jamil", "Zim"])
print(bank)

# pop
bank.popleft()
print(bank)

bank.popleft()
bank.popleft()

if not bank:
    print("No person left.")
