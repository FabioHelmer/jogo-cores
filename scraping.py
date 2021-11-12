from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

nav = webdriver.Firefox(executable_path=GeckoDriverManager().install())


nav.get("https://www.w3schools.com/colors/colors_names.asp")
sleep(1)

table = nav.find_element_by_id('colornamestable')
divs = table.find_elements_by_tag_name('div')

cores = {}
index = 0

for div in divs:
    text = div.text
    text =  text.split("\n")[0]
    if text != '' and '#' not in text and text not in list(cores.values()):
        cores[index] = text
        index = index + 1

file = open('cores.txt', 'w')


arrStr = '","'.join(list(cores.values()))

file.write(f'["{arrStr}"]')
file.close()

nav.close()

