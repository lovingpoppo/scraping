from selenium.webdriver import Firefox, FirefoxOptions

url = "http://www.yahoo.co.jp"

options = FirefoxOptions()
options.add_argument('-headless')

# Firefoxを起動し読み込み
browser = Firefox(options=options)
browser.get(url)

# 画像をセーブ
browser.save_screenshot("yahoo.png")
# 終了
browser.quit()

