import os
import sys 
import shutil
from pathlib import Path 


dir = input("Enter dir name: ")

curr_dir = Path.cwd()
Path.mkdir(parents=True)
