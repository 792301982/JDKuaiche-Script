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

f7=False
f8=False

def worker1():
    global f7
    global f8
    def on_press(key):
        global f7
        global f8
        if(str(key)=='Key.f7'):
            f7=True
        if(str(key)=='Key.f8'):
            f8=True
        #print(str(key))
        
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def worker2():
    global f7
    global f8
    def Beijing_time():
        r=requests.get('https://www.baidu.com')
        t=time.strptime(r.headers['date'],'%a, %d %b %Y %H:%M:%S GMT')
        return time.mktime(t)+28800

    '''if(Beijing_time()-1553361040>86400*5):
        input("测试期已过……请联系作者")
        sys.exit()'''

    #__browser_url=input("360浏览器地址：")
   
    #账号：    软件操作01     密码   ruanjiancaozuo01
    url='https://jzt.jd.com/kuaiche/survey.html#/normal_v2/unitList'
    driverOptions= webdriver.ChromeOptions()
    driverOptions.add_argument('log-level=3')
    driverOptions.add_argument('--start-maximized')
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
    for sku in skus:
        while(1):
            try:
                input("摁回车继续……")
                n+=1
                browser.get(url_1)
                WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.btn-create')))[0].click()
                
                f7=False
                f8=False
                if('st1' in dir()):
                    print("确保当前已进入设置页面，并且鼠标移出浏览器窗口。")
                    print("f7 按上一次设置操作。f8 修改设置。")
                    while(1):
                        if(f7==True):
                            break
                        if(f8==True):
                            st1=input("无线出价系数:")
                            if(st1==''):
                                st1=st1_o
                            else:
                                st1_o=st1
                            st2=input("搜索位PC出价:")
                            if(st2==''):
                                st2=st2_o
                            else:
                                st2_o=st2
                            st3=input("推荐位PC出价:")
                            if(st3==''):
                                st3=st3_o
                            else:
                                st3_o=st3

                            st4=input("搜索位定向人群勾选框(空格分割)：")
                            st5=input("推荐位定向人群勾选框(空格分割)：")
                            cj_num=input("商品推词-出价：")
                            yj1=input("溢价系数1：")
                            yj2=input("溢价系数2：")
                            #input("进入设置页面后回车。")
                            break
                else:
                    print("确保当前已进入设置页面，并且鼠标移出浏览器窗口。")
                    st1=input("无线出价系数:")
                    if(st1==''):
                        st1=st1_o
                    else:
                        st1_o=st1
                    st2=input("搜索位PC出价:")
                    if(st2==''):
                        st2=st2_o
                    else:
                        st2_o=st2
                    st3=input("推荐位PC出价:")
                    if(st3==''):
                        st3=st3_o
                    else:
                        st3_o=st3

                    st4=input("搜索位定向人群勾选框(空格分割)：")
                    st5=input("推荐位定向人群勾选框(空格分割)：")
                    cj_num=input("商品推词-出价：")
                    yj1=input("溢价系数1：")
                    yj2=input("溢价系数2：")
                    #input("进入设置页面后回车。")

                browser.refresh()
                time.sleep(1)
                
                quick=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="quick"]'))).click()
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
                    if(len(inputs)!=5):
                        inputs=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.jad-input')))
                    else:
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
                check_box=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.checkbox-con')))
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
                    if(i<=7 and st4!=''):
                        browser.find_element_by_css_selector(".TestUI-priceInput").send_keys(yj1)
                    else:
                        browser.find_element_by_css_selector(".TestUI-priceInput").send_keys(yj2)



                #推荐位PC出价
                l=browser.find_elements_by_css_selector(".jad-input-wrapper .jad-input-large")
                l[3].click()
                l[3].send_keys(Keys.BACK_SPACE)
                l[3].send_keys(Keys.BACK_SPACE)
                l[3].send_keys(Keys.BACK_SPACE)
                l[3].send_keys(st3)

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
                
                print("已完成 %s，用时 %d 秒。" % (sku.strip(),int(time.time()-time_1)))
                print("------------------------------------------------")
                with open ('sku.txt','w') as f:
                    for i in skus[n+1:]:
                        f.write(i)
                    print("sku.txt已更新。")
                break
            except:
                print(sku.strip(),"出错")
                continue

if __name__ == '__main__':
    '''if(Beijing_time() - 1550926703 > 172800 ):
        input("测试期已过。")
        sys.exit()'''
    t1 =threading.Thread(target=worker1)
    t1.start()   
    t2 =threading.Thread(target=worker2)
    t2.start()         
