# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup

import lxml
import os
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
soup = BeautifulSoup(open("res/top10.html", encoding="utf8"), features="lxml")
links = soup.find_all('h3')
for link in links:
    print(link.text)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
