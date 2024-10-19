import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from app.csdn import bp


@bp.route('/')
def index():
    return 'hello csdn.'


@bp.route('/get_articles/<user_name>')
def categories(user_name: str):
    """
    加载更多，获得全部文章连接
    :return:
    """
    csdn_url = f"https://blog.csdn.net/{user_name}"
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 不需要显示浏览器界面
    chrome_options.add_argument("--disable-gpu")
    chrome = webdriver.Chrome(options=chrome_options)

    try:
        # 打开目标网页
        chrome.get(csdn_url)

        # 等待页面加载完成（根据需要调整）
        WebDriverWait(chrome, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'some-selector'))  # 替换为实际的选择器
        )

        # 定义一个函数来模拟滑动到底部
        def scroll_to_bottom():
            # 执行 JavaScript 脚本滑动到页面底部
            chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 等待一段时间让新内容加载（根据需要调整）
            time.sleep(2)

            # 循环滑动直到没有更多内容加载（这里需要一个条件来判断何时停止）

        while True:
            # 滑动到底部
            scroll_to_bottom()

            # 检查是否有新内容加载（这里需要根据你的网页结构来编写逻辑）
            # 例如，你可以检查某个元素是否存在，或者某个元素的数量是否增加
            # 如果没有新内容加载，则跳出循环
            # 这是一个简单的示例，你可能需要更复杂的逻辑
            try:
                # 假设新内容加载后会出现一个特定的元素
                new_element = WebDriverWait(chrome, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'new-content-selector'))  # 替换为实际的选择器
                )
            except Exception as e:
                # 如果没有找到新元素，则假设没有更多内容加载
                print("No more content to load.")
                break

    finally:
        # 关闭浏览器
        chrome.quit()
