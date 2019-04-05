""" APP@头条（v7.1.3） 自动化测试（模拟器）"""

"""
  判断主页有无推荐新闻及其评论 (且存在相关搜索)
  "deviceName": "172.23.80.69:62001"
"""
import time
import random
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class SingleAppTest(object):

    def __init__(self):
        # 列表形式
        self.cap = {
            "platformName": "Android",
            "platformVersion": "4.4",
            "deviceName": "172.23.80.69:62001",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "noReset": True,
            # "unicodekeyboard": True,  # 中文输入
            # "resetkeyboard": True
            "udid": "127.0.0.1:62001",
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.cap)

        self.find_comment_xpath = "//android.widget.ListView[@resource-id='com.ss.android.article.news:id/a5t']/android.widget.LinearLayout[2]"
        self.find_recommend_id = "com.ss.android.article.news:id/age"
        self.find_recommend_title_id = "com.ss.android.article.news:id/title"
        self.find_return_xpath = "//android.widget.TextView[@resource-id='com.ss.android.article.news:id/a3']"
        self.find_refresh_xpath = "//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
        self.find_ad_xpath = "//android.widget.TextView[@resource-id='com.ss.android.article.news:id/crw']"
        self.find_update_xpath = "//android.widget.TextView[@resource-id='com.ss.android.article.news:id/d5q']"
        self.find_homepage_title_list_class = "android.widget.TextView"

        # 进行随机，之后替换成相对应指令
        self.click_list = [0, 1, 2, 3, 4]
        self.num = random.choice(self.click_list)

        self.x = self.driver.get_window_size()["width"]
        self.y = self.driver.get_window_size()["height"]

    # def get_size(self):
    #     x = self.driver.get_window_size()["width"]
    #     y = self.driver.get_window_size()["height"]
    #     return (x, y)

    init_click = False

    # 设置滑动坐标
    def get_coordinate(self):
        x0 = int(self.x * 0.5)
        y1 = int(self.y * 0.75)
        y11 = int(self.y * 0.4)
        y12 = int(self.y * 0.6)
        y2 = int(self.y * 0.25)
        coordinate_list = [x0, y12, x0, y2, y1, y11]
        return coordinate_list

    def get_next(self, coordinate_list, n):
        try:
            time.sleep(1)
            # 开始出现评论 self.find_comment
            while WebDriverWait(self.driver, 2).until_not(lambda x: x.find_element_by_xpath(self.find_comment_xpath)):
                self.driver.swipe(coordinate_list[0], coordinate_list[1], coordinate_list[2], coordinate_list[3])

                # 浏览并获取内容
                pass

                # 获取推荐新闻
                try:
                    if self.driver.find_element_by_id(self.find_recommend_id):
                        a = self.driver.find_elements_by_id(self.find_recommend_title_id)
                        if a:
                            print("--------------")
                            print("推荐的新闻有：")
                            for i in range(len(a)):
                                title = a[i].get_attribute("text")
                                print(title)
                            print("————点击推荐第{}条————".format(n + 1) + a[n].get_attribute("text"))
                            a[n].click()
                        else:
                            print("----------------------")
                            print("没有推荐新闻，点击返回")
                            # 点击返回
                            self.driver.find_element_by_xpath(self.find_return_xpath).click()
                            print("点击刷新")
                            if WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_xpath(self.find_refresh_xpath)):
                                self.driver.find_element_by_xpath(self.find_refresh_xpath).click()
                except:
                    pass
        except:
            if WebDriverWait(self.driver, 2).until(lambda x: x.find_elements_by_id(self.find_recommend_title_id)):
                a = self.driver.find_elements_by_id(self.find_recommend_title_id)
                print("--------------")
                print("推荐的新闻有：")
                for i in range(len(a)):
                    title = a[i].get_attribute("text")
                    print(title)
                print("————点击推荐第{}条————".format(n + 1) + a[n].get_attribute("text"))
                a[n].click()

    def run(self):
        try:
            while 1:
                # 等待
                time.sleep(6)
                # 广告 点击跳过
                try:
                    if WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_xpath(self.find_ad_xpath)):
                        self.driver.find_element_by_xpath(self.find_ad_xpath).click()
                except:
                    pass

                time.sleep(1)
                # 检测到更新 点击 以后再说 如果蹦不出来就获取不到
                try:
                    if WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_xpath(self.find_update_xpath)):
                        self.driver.tap([(314, 865), (406, 897)])
                except:
                    pass

                # 首页新闻列表选择
                if WebDriverWait(self.driver, 2).until(lambda x: x.find_elements_by_class_name(self.find_homepage_title_list_class)):
                    a = self.driver.find_elements_by_class_name(self.find_homepage_title_list_class)
                    print("----------")
                    print("首页新闻：")
                    print("----------")
                    for i in range(len(a) - 6):
                        title = a[i].get_attribute("text")
                        if len(title) > 4:
                            print(title)
                    # 暂先设置点击首页第三条新闻
                    title = self.driver.find_elements_by_class_name(self.find_homepage_title_list_class)[2].get_attribute("text")
                    self.driver.find_elements_by_class_name(self.find_homepage_title_list_class)[2].click()
                    print("------点击------" + title)

                # 循环点击推荐（由主页进入）
                while True:
                    self.get_next(self.get_coordinate(), random.choice(self.click_list))
        except:
            # 点击返回
            self.driver.find_element_by_xpath(self.find_return_xpath ).click()
            print("----------------------")
            print("没有推荐新闻，返回主页")
            if WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_xpath(self.find_refresh_xpath)):
                self.driver.find_element_by_xpath(self.find_refresh_xpath).click()
            print("点击刷新")


if __name__ == '__main__':
    SingleAppTest().run()




