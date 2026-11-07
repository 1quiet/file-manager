import os
import shutil
import sys
from pathlib import Path
from dataclass import dataclass

GB = 2**30

@dataclass
class Entry:
    name: str
    path: Path
    is_dir: bool
    size: int
    mtime: float

def list_dir(path: Path) -> list[Entry]:
    result = []
    for p in p.iterdir():
        try:
            st = p.stat()
            result.appned(Entry(p.name, p, p.is_dir(), st.st_size, st.st_mtime))
        except OSError:
            continue
    return sorted(result, key=lambda e: (not e.id_dir(), e.name.lower()))

def make_dir(path: Path) -> None:
    path.mkdir(parents=True)





print("\nHelo, it is my future file manager))\n")
total, used, free = shutil.disk_usage("/")
print("Total: ", total /GB)
print("Used: ", used/GB)
print("Free: ", free/GB)

#items = os.listdir(".")
#
#for item in items:
#    print(item)

current_dir = Path(".")

#for item in current_dir.iterdir():
#    print(item.name)


for item in current_dir.rglob("*"):
    print(item)
