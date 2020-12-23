from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time,json,sys,os
import requests
from pynput import keyboard
import threading
import traceback

def Beijing_time():
    r=requests.get('https://www.baidu.com')
    t=time.strptime(r.headers['date'],'%a, %d %b %Y %H:%M:%S GMT')
    return time.mktime(t)+28800


url='https://jzt.jd.com/kuaiche/survey.html#/normal_v2/unitList'
driverOptions= webdriver.ChromeOptions()
driverOptions.add_argument('log-level=3')
#driverOptions.add_argument('window-size=1920x768')  # 指定浏览器分辨率

#driverOptions.add_argument('--headless')
#driverOptions.binary_location=__browser_url
#driverOptions.add_argument(r"--user-data-dir = C:\Users\79230\AppData\Local\Google\Chrome\User Data")
browser = webdriver.Chrome("chromedriver",0,driverOptions)

browser.get(url)

'''dictCookies = browser.get_cookies()
jsonCookies = json.dumps(dictCookies)
# 登录完成后,将cookies保存到本地文件
with open("cookies.json", "w") as fp:
    fp.write(jsonCookies)

# 读取登录时储存到本地的cookie
with open("cookies.json", "r", encoding="utf8") as fp:
    ListCookies = json.loads(fp.read())
browser.delete_all_cookies()

for i in ListCookies:
    browser.add_cookie(i)

st1=input("无线出价系数:")
st2=input("搜索位PC出价:")
st3=input("推荐位PC出价:")
st4=input("搜索位定向人群勾选框(空格分割)：")
st5=input("推荐位定向人群勾选框(空格分割)：")'''


input("登录到单元列表后回车继续……")

#browser.get(url)
url_1=browser.current_url


    
skus=list()
with open ('sku.txt','r') as f:
    for i in f:
        skus.append(i)
n=0
#账号：    软件操作01     密码   ruanjiancaozuo01
qu_f=int(input("是否添加同款sku（1.是 2.否）："))
st1=input("无线出价系数:")
st2=input("搜索位PC出价:")
st3=input("推荐位PC出价:")
st4=input("搜索位定向人群勾选框(空格分割)：")
st5=input("推荐位定向人群勾选框(空格分割)：")
cj_num=input("商品推词-出价：")
yj1=input("溢价系数1：")
yj2=input("溢价系数2：")
yj3=input("溢价系数3：")



while(1):
    if(len(skus)==0):
        input("已全部完成，按回车退出……")
        sys.exit(0)
    sku=skus.pop()
    while(1):
        try:
            #input("摁回车继续……")
            n+=1
            browser.get(url_1)
            WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.btn-create')))[0].click()
            try:
                WebDriverWait(browser,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.jad-modal-dialog')))
                WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.jad-btn-large'))).click()
            except:
                pass
            try:
                WebDriverWait(browser,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.jad-guid-pop-close')))
            except:
                pass
            browser.refresh()
            time.sleep(1)
            try:
                WebDriverWait(browser,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.jad-guid-pop-close'))).click()
            except:
                pass
            if(qu_f!=1):
                quick=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="quick"]'))).click()
            else:
                pass
            input1=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.jad-input')))
            input1[0].click()
            input1[0].send_keys(sku.strip())
            input1[2].click()
            input1[2].send_keys(sku)
            bu=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'button')))
            bu[0].click()
            bs=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'input[name="selectedProduct"]')))
            bs[0].click()
            
            bu[3].click()

            time_1=time.time()
            inputs=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.jad-input')))
            while(1):
                if(len(inputs)!=6 and len(inputs)!=5):
                    inputs=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.jad-input')))
                else:
                    #browser.refresh()
                    break
            #无线出价系数
            inputs[0].click()
            inputs[0].send_keys(Keys.BACK_SPACE)
            inputs[0].send_keys(Keys.BACK_SPACE)
            inputs[0].send_keys(Keys.BACK_SPACE)
            inputs[0].send_keys(st1)

            #PC出价（￥）
            inputs[1].click()
            inputs[1].send_keys(Keys.BACK_SPACE)
            inputs[1].send_keys(Keys.BACK_SPACE)
            inputs[1].send_keys(Keys.BACK_SPACE)
            inputs[1].send_keys(st2)

            #tcPa设置
            WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.idea-state')))[0].click()
            button=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.TestUI-set')))

            
            boxs=st4.split(" ")
            if(len(boxs)!=1 and boxs[0]!=''):
                #定向推荐人群
                button[0].click()

                time.sleep(1)
                #input("顶部选框：")
                check_box=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.checkbox-con')))
                check_box[1].click()
                check_box[1].click()    #全选
                
                for i in boxs:
                    check_box[int(i)+1].click()
                
                #input("顶部选框：")

                #定向人群名称
                check_box[-1].click()
                check_box[-2].click()
                check_box[-4].click()
                check_box[-5].click()
                check_box[-6].click()
                browser.find_element_by_css_selector(".TestUI-ok").click()#确定

            #精选人群
            '''button[1].click()
            check_box=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.checkbox-con')))
            check_box[2].click()
            check_box[3].click()
            check_box[4].click()
            browser.find_element_by_css_selector(".TestUI-ok").click()'''#确定
            time.sleep(1)
            switchs=browser.find_elements_by_css_selector(".TestUI-jSelectionList .TestUI-switch")
            for i in switchs:
                i.click()


            #DMP人群设置
            button[2].click()
            time.sleep(1)
            check_box=WebDriverWait(browser,3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.checkbox-con')))
            num=len(check_box)
            for i in range(1,num):
                check_box[i].click()
            browser.find_element_by_css_selector(".TestUI-ok").click()#确定

            time.sleep(1)
            #溢价系数
            l=browser.find_elements_by_css_selector(".TestUI-adGroupPrice")
            pen=browser.find_elements_by_css_selector('.jad-icon-pencil2')

            for i in range(len(l)):
                l[i].click()
                time.sleep(1)
                pen[i].click()
                browser.find_element_by_css_selector(".TestUI-priceInput").send_keys(Keys.BACK_SPACE)
                browser.find_element_by_css_selector(".TestUI-priceInput").send_keys(Keys.BACK_SPACE)
                
                if(i<=4 and st4!=''):
                    browser.find_element_by_css_selector(".TestUI-priceInput").send_keys(yj1)
                elif(i<=7 and st4!=''):
                    browser.find_element_by_css_selector(".TestUI-priceInput").send_keys(yj2)
                elif(i<=2):
                    browser.find_element_by_css_selector(".TestUI-priceInput").send_keys(yj2)
                else:
                    browser.find_element_by_css_selector(".TestUI-priceInput").send_keys(yj3)



            #推荐位PC出价
            l=browser.find_elements_by_css_selector(".jad-input-wrapper .jad-input-large")
            l[3].click()
            l[3].send_keys(Keys.BACK_SPACE)
            l[3].send_keys(Keys.BACK_SPACE)
            l[3].send_keys(Keys.BACK_SPACE)
            l[3].send_keys(st3)

            try:
                WebDriverWait(browser,4).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.idea-state')))[1].click()
            except:
                pass
            try:
                WebDriverWait(browser,4).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.idea-state')))[2].click()
            except:
                pass
            try:
                WebDriverWait(browser,4).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.idea-state')))[3].click()
            except:
                pass

            
            button=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.TestUI-set')))
                
            boxs=st5.split(" ")
            if(len(boxs)!=1 and boxs[0]!=''):
                #推荐位人群
                #定向推荐人群
                button[3].click()
                time.sleep(1)
                #input("顶部选框：")
                check_box=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.checkbox-con')))
                check_box[1].click()                #全选
                check_box[1].click()
                
                for i in boxs:
                    check_box[int(i)+1].click()

                #定向人群名称
                check_box[-1].click()
                check_box[-2].click()
                check_box[-4].click()
                check_box[-5].click()
                check_box[-6].click()
                browser.find_element_by_css_selector(".TestUI-ok").click()#确定
            time.sleep(1)
            
            #精选人群
            button[4].click()
            time.sleep(1)
            check_box=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.checkbox-con')))
            check_box[2].click()
            check_box[3].click()
            check_box[4].click()
            browser.find_element_by_css_selector(".TestUI-ok").click()#确定
            time.sleep(1)

            #DMP人群设置
            button[5].click()
            time.sleep(1)
            check_box=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.checkbox-con')))
            num=len(check_box)
            for i in range(1,num):
                check_box[i].click()
            browser.find_element_by_css_selector(".TestUI-ok").click()#确定
            js='document.getElementsByClassName("blue")[5].click();'
            time.sleep(1)
            #browser.find_elements_by_css_selector(".clearfix .setting-content .blue")[2].click()
            browser.execute_script(js)
            time.sleep(1)
            if(cj_num!=''):
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.w300'))).click()
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.w300'))).send_keys(sku)
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.pull-left .btn-creat'))).click()
                time.sleep(2)
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.add-keyWord tbody tr')))
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.add-keyWord .jad-table-selection'))).click()
                time.sleep(2)
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.add-keys .jad-table-selection'))).click()
                time.sleep(1)
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.xgcj-btn'))).click()
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.w150'))).click()
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.w150'))).send_keys(cj_num)
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn-success'))).click()
                WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.modal-footer button'))).click()
            else:
                browser.find_elements_by_css_selector(".jad-tab-nav li")[-1].click()
                browser.find_element_by_css_selector(".fileupload-new").click()
            
            WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.jad-btn-secondary'))).click()
            time.sleep(3)
            try:
                WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.complete-mark')))
            except:
                print(sku.strip(),"提交不成功，重试中……")
                continue
            print("已完成 %s，用时 %d 秒。" % (sku.strip(),int(time.time()-time_1)))
            print("------------------------------------------------")
            with open ('sku.txt','w') as f:
                for i in skus:
                    f.write(i)
                print("sku.txt已更新。")
            break
        except:
            input(sku.strip()+" 出错，纠正后，按回车继续……")
            print(traceback.format_exc())
            continue
