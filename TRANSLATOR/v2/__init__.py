import undetected_chromedriver as uc
from time import sleep

driver = uc.Chrome(headless=True, use_subprocess=True)

def translate_v2(text, language_code):
    driver.get(f'https://papago.naver.com/?sk=auto&tk={language_code}&st={text}')
    while True:
        try:
            translated = driver.find_element('xpath', '//*[@id="txtTarget"]').text.strip()
            if translated:
                return translated
        except Exception as e:
            # print(e)
            continue
