# 참고 링크
# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/

#region Import
import selenium
import sys

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep
#endregion



#region Initialize
print("Initializing...")
URL = 'https://hcs.eduro.go.kr/#/loginHome'

options = webdriver.ChromeOptions()
# 헤드리스 모드로 동작
options.add_argument("headless")
# 불필요한 로그 비활성화
options.add_experimental_option("excludeSwitches", ["enable-logging"])

try:
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
except selenium.common.exceptions.WebDriverException as err:
    print("[ERROR] chromedriver.exe를 찾을 수 없습니다.")
    quit()
driver.get(url=URL)

# 암묵적 대기 시간
driver.implicitly_wait(5)
# 명시적 대기 시간
wait = WebDriverWait(driver, 5, 0.2)


# 자가진단에 쓸 정보
print('Reading User Info...')
try:
    file = open('user.txt', 'r', encoding='utf-8')
except FileNotFoundError as err:
    print('[ERROR] user.txt 파일을 찾을 수 없습니다.')
    quit()


print('\n계정정보 불러오는 중:\n')
SIDO = file.readline().strip()
LEVEL = file.readline().strip()
SCHOOL_NAME = file.readline().strip()
NAME = file.readline().strip()
DAY_OF_BIRTH = file.readline().strip()
PASSWORD = file.readline().strip()
print('계정정보를 불러왔습니다')
file.close()

#endregion



#region Login
# 1. 초기 페이지에서 자가진단 참여하기 버튼 클릭
driver.find_element_by_id('btnConfirm2').click()



# 2. 학교 검색 버튼 클릭
driver.find_element_by_class_name('searchBtn').click()



# 3. 학교 검색
# 3-1. 시/도 선택
Select(driver.find_element_by_id('sidolabel')).select_by_visible_text(SIDO)

# 3-2. 학교급 선택
Select(driver.find_element_by_id('crseScCode')).select_by_visible_text(LEVEL)

# 3-3. 학교명 입력
driver.find_element_by_id('orgname').send_keys(SCHOOL_NAME)

# 3-4. 학교 검색
driver.find_element_by_class_name('searchBtn').click()

# 3-5. 학교 선택
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a')))
# 선택
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click()
# 제출
driver.find_element_by_class_name('layerFullBtn').click()
sleep(0.5)


# 4. 성명, 생년월일 선택
driver.find_element_by_id('user_name_input').send_keys(NAME)
driver.find_element_by_id('birthday_input').send_keys(DAY_OF_BIRTH)

# 제출
driver.find_element_by_id('btnConfirm').click()

# 5. 비밀번호 선택
sleep(1)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'input_text_common')))
driver.find_element_by_class_name('input_text_common').send_keys(PASSWORD)

# 제출
wait.until(EC.presence_of_element_located((By.ID, 'btnConfirm')))
wait.until(EC.element_to_be_clickable((By.ID, 'btnConfirm')))
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
sleep(3)

print('로그인 완료\n')
#endregion



#region 자가진단

# 학생 리스트 가져오기
items = driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul').find_elements_by_tag_name('li')
print(f'확인된 총 학생 수 : {len(items)}명')


while True:
    # 자가진단 완료하지 않은 학생만 가져오기
    items = driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul').find_elements_by_css_selector('li:not(.active)')
    sleep(0.5)
    if len(items) == 0:
        print('자가진단이 모두 완료되었습니다.')
        break
    print(f'자가진단이 되지 않은 학생 수 : {len(items)}명')
    

    item = items[0]
    name = item.find_element_by_class_name('name').get_attribute('innerHTML')

    #region 자가진단
    sleep(0.5)
    item.find_element_by_class_name('name').click()
    print(f'{name}학생의 자가진단을 시작합니다.')
    sleep(0.5)

    # 조사 응답
    wait.until(EC.element_to_be_clickable((By.ID, 'survey_q1a1')))
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_xpath('//*[@id="survey_q1a1"]'))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="survey_q1a1"]'))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="survey_q2a1"]'))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="survey_q3a1"]'))

    # 응답 제출
    driver.find_element_by_id('btnConfirm').click()
    print(f'{name} 제출 완료')

    # 처음으로 버튼 클릭
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[1]/ul/li/a').click()
    sleep(1)
    #endregion

#endregion
    


# 브라우저 닫기
driver.close()
print("Ctrl+C를 눌러 종료하세요")
sys.exit(0)