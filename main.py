import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random,re
chrome_path = r''  # 替換為你的 Chrome 執行檔路徑
chromedriver_path = r''  # 替換為你的 ChromeDriver 執行檔路徑

# 初始化 Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
url = "https://www.cp.gov.tw/portal/Clogin.aspx?ReturnUrl=https://elearn.hrd.gov.tw/egov_login.php&ver=Simple&Level=1"  # 要爬取的網址
#個人資料
username = ""
password = ""
classtime=5.1*60*60/2#總時長除以2
# 訪問網頁
driver.get(url)
username_input = driver.find_element(By.ID, "AccountPassword_simple_txt_account")
password_input = driver.find_element(By.ID, "AccountPassword_simple_txt_password")
username_input.send_keys(username)
password_input.send_keys(password)
driver.find_element(By.ID, "AccountPassword_simple_btn_LoginHandler").click()
time.sleep(0.5)
driver.get("https://elearn.hrd.gov.tw/mooc/user/learn_stat.php")
time.sleep(2)
table = driver.find_element(By.ID, "pc_data")
# 找到表格中的所有行
rows = table.find_elements(By.TAG_NAME, "tr")
print(rows)
allclass = []
# 遍歷每一行，獲取每一列的數據
try:
    driver.implicitly_wait(5)
    for row in rows[1:]:
        row_html = row.get_attribute("outerHTML")
        columns = row.find_elements(By.TAG_NAME, "td")
        targettime = re.search(r'(\d+:\d+:\d+)', columns[7].text)
        classid = re.search(r'gotoCourse\((\d+)\)', row_html)
        print(row_html,classid.group(1))
        targettime = targettime.group(1)
        read_time = columns[4].text
        # 如果閱讀時數為 0，進行相應處理
        if read_time == "0":
            read_time = "0:00:00"
        print(targettime, read_time)
        targettime = datetime.strptime(targettime, "%H:%M:%S")
        read_time = datetime.strptime(read_time, "%H:%M:%S")
        classtime = (targettime - read_time).total_seconds()
        if classtime > 0:
            allclass.append(["https://elearn.hrd.gov.tw/info/"+classid.group(1),classtime])
except Exception as e:
    # 捕捉特定的例外，並可選擇性地印出錯誤信息
    print(f"An exception occurred: {e}")
for classs in allclass:
    print(classs)
def url_matches(driver):
    return bool(url_pattern.match(driver.current_url))
for i in allclass:
    driver.get(i[0])
    time.sleep(1)
    btn = driver.find_element(By.XPATH, "//*[@id=\"course-info-bottom\"]/div[2]/button")
    btn.click()
    start = time.time()

    while True:
        try:
            url_pattern = re.compile(r"https://.*\.elearn\.hrd\.gov\.tw/learn/")
            # 使用 WebDriverWait 等待網址為指定值
            WebDriverWait(driver, 10).until(url_matches)
            driver.implicitly_wait(10)
            # 當前網址為指定值，繼續執行以下代碼

            # 找到並切換到 frame
            frame_catalog = driver.find_element(By.ID, "s_catalog")
            driver.switch_to.frame(frame_catalog)
            time.sleep(1)
            break  # 跳出迴圈

        except Exception as e:
            # 捕捉特定的例外，並可選擇性地印出錯誤信息
            print(f"An exception occurred: {e}")

    frame_pathtree = driver.find_element(By.ID, "pathtree")
    driver.switch_to.frame(frame_pathtree)
    while 1:
        try:
            ul_element = driver.find_element(By.CLASS_NAME, "step-process2")
            time.sleep(5)
            break
        except:
            pass

    while 1:
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        for li_element in li_elements:
            if "環境檢測" not in li_element.text:
                driver.set_window_size(random.randint(1000, 1200), random.randint(1000, 1200))
                li_element.find_element(By.TAG_NAME, "a").click()
                time.sleep(30)
            now = time.time()
            print(i[1]-(now-start))
        if now-start>i[1]+300:
            break
