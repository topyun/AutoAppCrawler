""" APP@头条（v7.1.3） 自动化测试（模拟器）"""
"""
    获取新闻详情内容 
"""
import time
import random
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class ScrapeContent(object):

    def __init__(self):
        self.cap = {
            "platformName": "Android",
            "platformVersion": "4.4",
            "deviceName": "172.23.80.69:62001",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "noReset": True,
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.cap)

        self.x = self.driver.get_window_size()["width"]
        self.y = self.driver.get_window_size()["height"]

        self.find_comment_xpath = "//android.widget.ListView[@resource-id='com.ss.android.article.news:id/a5t']/android.widget.LinearLayout[2]"
        self.find_recommend_id = "com.ss.android.article.news:id/age"
        self.find_recommend_title_id = "com.ss.android.article.news:id/title"
        self.find_return_xpath = "//android.widget.TextView[@resource-id='com.ss.android.article.news:id/a3']"
        self.find_refresh_xpath = "//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
        self.find_ad_xpath = "//android.widget.TextView[@resource-id='com.ss.android.article.news:id/crw']"
        self.find_update_xpath = "//android.widget.TextView[@resource-id='com.ss.android.article.news:id/d5q']"
        self.find_homepage_title_list_class = "android.widget.TextView"
        self.find_like_id = "com.ss.android.article.news:id/av3"
        self.find_content_class = "android.view.View"

    def get_coordinate(self):
        x0 = int(self.x * 0.5)
        y1 = int(self.y * 0.75)
        y11 = int(self.y * 0.4)
        y12 = int(self.y * 0.6)
        y2 = int(self.y * 0.25)
        coordinate_list = [x0, y12, x0, y2, y1, y11]
        return coordinate_list

    def get_content(self, coordinate_list):
        time.sleep(1)
        # 到相关搜索停止滑动，即到达点赞位置上
        while True:
            self.driver.swipe(coordinate_list[0], coordinate_list[1], coordinate_list[2], coordinate_list[3])
            time.sleep(6)
            try:
                if self.driver.find_element_by_id(self.find_like_id):
                    print(self.driver.find_element_by_id(self.find_like_id).get_attribute("text"))
                    print("--------------")
                    break
                else:
                    continue
            except:
                pass

        # 获取文本，文章内容、相关搜索
        if self.driver.find_elements_by_class_name(self.find_content_class):
            a = self.driver.find_elements_by_class_name(self.find_content_class)
            content = []
            relate_search = []
            change_put = False
            for i in range(len(a)):
                title = a[i].get_attribute("name")
                if '相关搜索' in title:
                    change_put = True
                if change_put:
                    relate_search.append(title)
                else:
                    content.append(title)
            content_plus = ''.join(content)
            relate_search = [x for x in relate_search if x != '']  #
            print(relate_search)
            print("文章内容：" + content_plus)

            # 存储
            pass

    def run_entry(self):
        # 广告 点击跳过
        try:
            if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_xpath(self.find_ad_xpath)):
                self.driver.find_element_by_xpath(self.find_ad_xpath).click()
        except:
            pass
        time.sleep(6)
        # 检测到更新 点击 以后再说
        try:
            if WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(self.find_update_xpath)):
                self.driver.tap([(314, 865), (406, 897)])
        except:
            pass
        if WebDriverWait(self.driver, 5).until(lambda x: x.find_elements_by_class_name(self.find_homepage_title_list_class)):
            a = self.driver.find_elements_by_class_name(self.find_homepage_title_list_class)
            for i in range(len(a)-6):
                title = a[i].get_attribute("text")
                if len(title) > 4:
                    print(title)
            title = self.driver.find_elements_by_class_name(self.find_homepage_title_list_class)[2].get_attribute("text")
            self.driver.find_elements_by_class_name(self.find_homepage_title_list_class)[2].click()
            print("------点击------" + title)
        self.get_content(self.get_coordinate())


if __name__ == '__main__':
    ScrapeContent().run_entry()
