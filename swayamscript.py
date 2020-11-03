 #! /usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import json
import base64

if __name__ == "__main__":

    browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
    browser.get("https://onlinecourses.nptel.ac.in/")
    input("Pls navigate to the assignment page in browser , comeback to terminal and  press enter")
    source = browser.page_source
    sleep(1)
    matches=re.findall(r'JSON\.parse\(window\.atob\(\"(.+?)\"\)',source)
    decodedBytes = base64.urlsafe_b64decode(matches[0])
    json_str = str(decodedBytes, "utf-8")
    json_obj = json.loads(json_str)
    ids=[]
    for key,value in json_obj.items():
        ids.append(key)
    n = len(ids)
    answers = [0] * n
    for i in range(n):
        browser.find_element_by_id(ids[i]).find_element_by_id(ids[i]+"."+str(answers[i])).click()
    sleep(10)
    browser.find_element_by_id("submitbutton")
    sleep(15)
    print("25% completed "+"."*25)
    for j in range(3):
        source = browser.page_source
        matches = re.findall(r'\[(.+?)\]\}',source)
        marks = matches[1].split(", ")
        for k in range(n):
            if marks[k]=="0":
                answers[k] = answers[k]+1
        for l in range(n):
            if marks[l]=="0":
                browser.find_element_by_id(ids[l]).find_element_by_id(ids[l]+"."+str(answers[l])).click()
        sleep(10)
        browser.find_element_by_id("submitbutton")
        sleep(15)
        print(str((j+2)*25)+"% "+"completed"+"."*25)
    sleep(5)
    print("Completed ▨-▨¬ლ(•_•) (▨_▨¬) ლ(▀̿̿Ĺ̯̿̿▀̿ლ)")
    print("Here, answers for you friends （‐＾▽＾‐）")
    print("0 - a ..... 3 - d")
    print(answers)
    browser.quit()
