import time
import unittest
from selenium.webdriver.common.by import By
from utils.config import Config ,DATA_PATH,REPORT_PATH # DRIVER_PATH,
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email
from test.page.baidu_result_page import BaiDuResultPage,BaiDuMainPage


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')


    def sub_setUp(self):
        #初始页面是main page,传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL,maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        #从表格中读取数据
        datas = ExcelReader(self.excel).data

        for d in datas:
            with self.subTest(data = d):
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page) #页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report_file = REPORT_PATH + '\\report.html'
    testsuite = unittest.TestSuite()

    #把测试用例集传入到testsuite中
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBaiDu))

    with open(report_file,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='测试报告测试',description='修改html报告')
        #runner.run(TestBaiDu('test_search'))
        runner.run(testsuite)
    e = Email(title='百度测试报告',
              message='这是今天的测试报告，请查收',
              receiver='664456154@qq.com',
              sender='1342388193@qq.com',
              password='zksyihyjdrrdggcd',
              path=report_file)
    e.send()
