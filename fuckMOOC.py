# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

tele = ''  ##手机号
password = ''  ##密码
course = "https://www.icourse163.org/course/SDCJDX-1449481165"  ##课程地址
unit = 5  ##单元数
waitTime = 0.5  ##等待时间

json = 'var REFRESH_TIME=100;var REG=RegExp(/^http(s)?:\/\/www\.icourse163\.org\/.*\/learn\/hw.*/);var COMMENT_STRINGS_LIST=[];COMMENT_STRINGS_LIST[0]="很好";function getRandomInt(max){return Math.floor(Math.random()*Math.floor(max))}function doIt(){if(window.location.href.match(REG)==null){return}return doItNonCheck()}function parseFloatEx(string){var res="";for(var i=0;i<string.length;i++){var chr=string.charAt(i);if((chr>="0"&&chr<="9")||chr==="."){res+=chr}}return parseFloat(res)}function doItNonCheck(){var i,j,k;if(!window.jQuery){var oScript=document.createElement("script");oScript.type="text/javascript";oScript.src="//s1.hdslb.com/bfs/static/jinkela/long/js/jquery/jquery1.7.2.min.js";document.head.appendChild(oScript)}var scorePanelList=$("div.detail>div.s");for(i=0;i<scorePanelList.length;i++){var scorePanel=scorePanelList[i];var maxScore=-1;var maxIndex=-1;for(j=0;j<scorePanel.children.length;j++){for(k=0;k<scorePanel.children[j].children.length;k++){if(scorePanel.children[j].children[k].type==="radio"){var nowScore=parseFloatEx(scorePanel.children[j].children[k].value);var nowIndex=j;if(maxScore<nowScore){maxScore=nowScore;maxIndex=nowIndex}}}}console.log("maxIndex:"+maxIndex);console.log("maxScore:"+maxScore);if(maxIndex!==-1){for(k=0;k<scorePanel.children[maxIndex].children.length;k++){if(scorePanel.children[maxIndex].children[k].type==="radio"){console.log($(scorePanel.children[maxIndex].children[k]));$(scorePanel.children[maxIndex].children[k]).attr("checked","true")}}}}var commentTextAreaList=$("textarea.j-textarea.inputtxt");for(i=0;i<commentTextAreaList.length;i++){var commentTextArea=commentTextAreaList[i];if(commentTextArea.value===undefined||commentTextArea.value===null||commentTextArea.value===""||commentTextArea.value.length===0){commentTextArea.value=COMMENT_STRINGS_LIST[getRandomInt(COMMENT_STRINGS_LIST.length)]}}}(function(){"use strict";window.onload=window.setInterval(doIt,REFRESH_TIME)})();'
driver = webdriver.Chrome()
driver.get(course)
driver.find_element(By.PARTIAL_LINK_TEXT, "登录").click()
driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div/div/div/div/div[2]/span").click()
driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/ul/li[2]").click()

iframe = driver.find_element(By.XPATH,
                             "/html/body/div[13]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div/iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.ID, "phoneipt").send_keys(tele)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div/div[4]/div[2]/input[2]").send_keys(password)
time.sleep(waitTime)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div/div[6]/a").click()
login = (By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/div/span")
WebDriverWait(driver, 60, 0.5).until(expected_conditions.presence_of_element_located(login))
driver.find_element(By.XPATH,
                    "/html/body/div[4]/div[2]/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/div/span").click()
time.sleep(waitTime)
try:
    driver.find_element(By.XPATH, "/html/body/div[10]/div/div[2]/div/div/p/label/label/input").click()
    driver.find_element(By.XPATH, "/html/body/div[10]/div/div[1]/a").click()
except:
    print(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[1]/div/ul/li[4]/a").click()
time.sleep(waitTime)

for num in range(1, unit + 1):
    units = "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/div[" + str(
        num + 1) + "]/*/*/a[text()='前往作业']"

    time.sleep(waitTime)
    driver.find_element(By.XPATH, units).click()
    time.sleep(waitTime)
    flag = False
    try:
        driver.find_element(By.XPATH,
                            "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div[2]/a").click()
        time.sleep(waitTime)
        while not flag:
            driver.execute_script(json)
            time.sleep(waitTime)
            driver.find_element(By.XPATH,
                                "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[3]/div/div[4]/a[3]").click()
            time.sleep(waitTime)
            driver.find_element(By.XPATH,
                                "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[3]/div/div[1]/p[2]/a").click()
            if driver.find_element(By.XPATH,
                                   "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]").get_attribute(
                'class') == "f-fl status undone j-status done":
                flag = True
            else:
                flag = False
        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/div").click()
    except:
        try:
            driver.find_element(By.LINK_TEXT, "继续进行互评").click()
            time.sleep(waitTime)
            while not flag:
                driver.execute_script(json)
                time.sleep(waitTime)
                driver.find_element(By.XPATH,
                                    "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[3]/div/div[4]/a[3]").click()
                time.sleep(waitTime)
                driver.find_element(By.XPATH,
                                    "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[3]/div/div[1]/p[2]/a").click()
                if driver.find_element(By.XPATH,
                                       "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]").get_attribute(
                    'class') == "f-fl status undone j-status done":
                    flag = True
                else:
                    flag = False
            driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/div").click()
        except:
            driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/div").click()

for num in range(1, unit + 1):
    units = "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/div[" + str(
        num + 1) + "]/*/*/a[text()='前往作业']"
    time.sleep(waitTime)
    driver.find_element(By.XPATH, units).click()
    time.sleep(waitTime)
    if driver.find_element(By.XPATH,
                           "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[4]/div").get_attribute(
        'class') == "f-fl status undone j-status":
        driver.find_element(By.XPATH,
                            "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[3]/div/div/table/tbody/tr/td[2]/a").click()
        driver.execute_script(json)
        time.sleep(waitTime)
        driver.find_element(By.XPATH,
                            "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[3]/div/div[4]/a[3]").click()
        time.sleep(waitTime)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/div").click()
        time.sleep(waitTime)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/div").click()
    else:
        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/div").click()
