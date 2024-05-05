# -*- coding: utf-8 -*-
#Web Expelor

def start():
    from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings
    from PyQt5.QtCore import Qt, QUrl
    from PyQt5.QtWidgets import QToolBar, QLineEdit, QMainWindow, QApplication, QTabWidget, QMenu, QAction, QMessageBox
    import sys

    class WebView(QWebEngineView):
        def __init__(self, parent):
            super().__init__(parent)
            QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
            self.cookies = {}  # 存放cookie字典

        def createWindow(self, webWindowType):
            return main_demo.browser

        def onCookieAdd(self, cookie):  # 处理cookie添加的事件
            name = cookie.name().data().decode('utf-8')  # 先获取cookie的名字，再把编码处理一下
            value = cookie.value().data().decode('utf-8')  # 先获取cookie值，再把编码处理一下
            self.cookies[name] = value  # 将cookie保存到字典里

        # 获取cookie
        def get_cookie(self):
            cookie_str = ''
            for key, value in self.cookies.items():  # 遍历字典
                cookie_str += (key + '=' + value)  # 将键值对拿出来拼接一下
            return cookie_str

    class MainDemo(QMainWindow):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.setWindowTitle('Web Expelor')
            self.resize(1024, 768)
            # 添加标签栏
            self.tabs = QTabWidget()
            self.tabs.setDocumentMode(True)
            # 添加URL地址栏
            self.urlbar = QLineEdit()
            # 让地址栏支持输入地址回车访
            self.urlbar.returnPressed.connect(self.navigate_to_url)
            # 添加标签栏
            self.tabs = QTabWidget()
            self.tabs.setDocumentMode(True)
            self.tabs.tabBarDoubleClicked.connect(self.tab_open)
            self.tabs.currentChanged.connect(self.current_tab_changed)
            # 允许关闭标签
            self.tabs.setTabsClosable(True)
            # 设置关闭按钮的槽
            self.tabs.tabCloseRequested.connect(self.close_current_tab)
            self.add_new_tab(QUrl('https://www.bing.com/'), 'Homepage')
            self.setCentralWidget(self.tabs)
            new_tab_action = QAction('New Page', self)
            new_tab_action.triggered.connect(self.add_new_tab)
            # 添加导航栏
            navigation_bar = QToolBar('Navigation')
            self.addToolBar(navigation_bar)
            # 添加前进、后退、停止加载和刷新的按钮
            back_button = QAction('Back', self)
            forward_button = QAction('Forward', self)
            stop_button = QAction('Stop', self)
            reload_button = QAction('Reload', self)
            back_button.triggered.connect(self.tabs.currentWidget().back)
            forward_button.triggered.connect(self.tabs.currentWidget().forward)
            stop_button.triggered.connect(self.tabs.currentWidget().stop)
            reload_button.triggered.connect(self.tabs.currentWidget().reload)
            # 将按钮添加到导航栏上
            navigation_bar.addAction(back_button)
            navigation_bar.addAction(forward_button)
            navigation_bar.addAction(stop_button)
            navigation_bar.addAction(reload_button)
            navigation_bar.addSeparator()
            navigation_bar.addWidget(self.urlbar)

            # 添加自定义菜单
            self.web_menu = WebMenu()

        # 添加新的标签页
        def add_new_tab(self, qurl=QUrl(''), label='https://bing.com'):
            # 设置浏览器
            self.browser = WebView(self)
            self.browser.page().load(qurl)

            # 添加右键菜单
            self.browser.setContextMenuPolicy(Qt.CustomContextMenu)
            self.browser.customContextMenuRequested.connect(self.MyBrowser_Menu)  # 将菜单的信号链接到自定义菜单槽函数

            # 添加标签
            i = self.tabs.addTab(self.browser, label)
            self.tabs.setCurrentIndex(i)
            self.browser.urlChanged.connect(lambda qurl, browser=self.browser: self.renew_urlbar(qurl, self.browser))

            # 将标签标题改为网页相关的标题
            self.browser.loadFinished.connect(
                lambda _, i=i, browser=self.browser: self.tabs.setTabText(i, self.browser.page().title()))

        # 响应回车按钮，将浏览器当前访问的URL设置为用户输入的URL
        def navigate_to_url(self):
            current_url = QUrl(self.urlbar.text())
            if current_url.scheme() == '':
                current_url.setScheme('http')
            self.tabs.currentWidget().load(current_url)

        # 将当前网页的链接更新到地址栏
        def renew_urlbar(self, url, browser=None):
            # 非当前窗口不更新URL
            if browser != self.tabs.currentWidget():
                return
            self.urlbar.setText(url.toString())
            self.urlbar.setCursorPosition(0)

        # 双击标签栏打开新页面
        def tab_open(self, i):
            if i == -1:
                self.add_new_tab()

        def current_tab_changed(self, i):
            qurl = self.tabs.currentWidget().url()
            self.renew_urlbar(qurl, self.tabs.currentWidget())

        def close_current_tab(self, i):
            # 若当前标签页只有一个则不关闭
            if self.tabs.count() < 2:
                return
            self.tabs.removeTab(i)

        # 创建自定义浏览器右键菜单
        def MyBrowser_Menu(self, pos):
            action = self.web_menu.exec_(self.browser.mapToGlobal(pos))
            if action == self.web_menu.save_act:
                self.save_slot()
            elif action == self.web_menu.reload_act:
                self.reload_slot()
            elif action == self.web_menu.run_js:
                self.run_js()

        # 保存cookie
        def save_slot(self):
            cookie = self.browser.get_cookie()
            with open('C:\\cmd\\cookie.txt', 'w', encoding='utf8') as f:
                f.write(cookie)

            QMessageBox.information(self, "Info", "Cookie is saved")

        # 重新加载页面
        def reload_slot(self):
            self.browser.reload()

        # 运行js
        def run_js(self):
            js_string = '''
            document.getElementsByClassName("s_ipt")[0].value = "666666"
            '''

            self.browser.page().runJavaScript(js_string)

    # 自定义的一个菜单类
    class WebMenu(QMenu):
        def __init__(self):
            super(WebMenu, self).__init__()
            # 定义一个浏览器右键菜单
            self.save_act = QAction("Save cookie")
            self.reload_act = QAction("Refresh page")
            self.run_js = QAction("Run JavaScript")
            self.addAction(self.save_act)
            self.addAction(self.reload_act)
            self.addAction(self.run_js)


    my_application = QApplication(sys.argv)  # 创建QApplication类的实例
    main_demo = MainDemo()
    main_demo.showMaximized()
    my_application.exec_()
