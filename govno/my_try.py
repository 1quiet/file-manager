import os
import shutil
import sys
from pathlib import Path

print("\nHelo, it is my future file manager))\n")
GB = 2**30
total, used, free = shutil.disk_usage("/")
print("Total: ", total /GB)
print("Used: ", used/GB)
print("Free: ", free/GB)

#items = os.listdir(".")
#
#for item in items:
#    print(item)

current_dir = Path(".")

for item in current_dir.iterdir():
    print(item.name)


for item in current_dir.rglob("*"):
    print(item)
