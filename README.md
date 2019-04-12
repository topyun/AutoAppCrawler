# AutoAppCrawler
对内容分发APP模拟操作，对内容自行识别并爬取


## 进度

现阶段
>代码将陆续上传

1.实现单个模拟器中app(今日头条)自动滑动点击操作与内容获取

2.实现多个模拟器并行工作

。。。

## 说明

1.目前是通过appium来控制APP操作及其内容的获取，以下版本为本人现行使用版本

2.下载代码 相应的脚本代码在部署完环境后可直接于pycharm中运行
>git clone https://github.com/topyun/AutoAppCrawler.git

3.操作系统
>目前在windows上操作，正逐步将环境迁到linux中，未来将全部在上面运行


一、环境工具
>1.目前在windows10系统下，JDK8，夜神Android模拟器（V android4.4）/魅族手机（V android7.0）（进入开发者模式，打开USB调试）,今日头条app（V 7.1.3）

>2.appium(1.10，自动化测试工具)，Android SDK（V r24.4.1,主要用adb(连接手机),uiautomatorviewer(APP界面的定位控件,增强版带xpath)）

>3.脚本开发使用python3，其IDE pycharm


二、环境部署(版本尽量统一)
>1、Appium安装 可去官网下载(server端)：http://appium.io/  Appium是一个自动化测试开源工具,支持iOS和android平台上的移动原生应用、移动Web应用和混合应用。appium封装了标准的selenium类库

>2、Android SDK安装 下载地址：http://tools.android-studio.org/ 【安装前请确保已经存在JDK8(下载地址：https://www.oracle.com/technetwork/java/javase/downloads/index.html) 】 软件开发工具包,用于为特定的软件包、软件框架、硬件平台、操作系统等建立应用软件的开发工具的集合

>3、Python3.7 官网地址 https://www.python.org/downloads/windows/ 大家可先学习一下python基础，目前也还用不到多么深入的python知识

>4、Pycharm 官网地址 http://www.jetbrains.com/pycharm/download/#section=windows 下载专业版之后进行破解

>5、Android模拟器 夜神模拟器官网 https://www.yeshen.com/ 并在里面安装今日头条app

>6、JDK 官网地址 https://www.oracle.com/technetwork/java/javase/downloads/index.html 这里版本统一为jdk8
