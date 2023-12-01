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
time.sleep(1)
driver.get("https://elearn.hrd.gov.tw/mooc/user/learn_stat.php")
def url_matches(driver):
    return bool(url_pattern.match(driver.current_url))
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
        html = driver.page_source
        print(html)
        print("-" * 100)
        break  # 跳出迴圈

    except Exception as e:
        # 捕捉特定的例外，並可選擇性地印出錯誤信息
        print(f"An exception occurred: {e}")

frame_pathtree = driver.find_element(By.ID, "pathtree")
driver.switch_to.frame(frame_pathtree)
while 1:
    try:
        ul_element = driver.find_element(By.CLASS_NAME, "step-process2")
        print(ul_element)
        time.sleep(5)
        break
    except:
        pass
li_elements = ul_element.find_elements(By.TAG_NAME, "li")

while 1:
    start_time = time.time()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if classtime<elapsed_time:
        break
    driver.set_window_size(random.randint(800, 1000), random.randint(600, 800))
    for li_element in li_elements:
        if "環境檢測" not in li_element.text:
            li_element.find_element(By.TAG_NAME, "a").click()
            time.sleep(10)
# 關閉瀏覽器實例
# driver.quit()
