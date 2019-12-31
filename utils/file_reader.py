import yaml
import os
from xlrd import open_workbook


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data

class SheetTypeError(object):
    pass

class ExcelReader():
    def __init__(self,excel,sheet=0,title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0) #首行为title。第一行的值
                for col in range(1,s.nrows): #row为行。col为列
                    self._data.append(dict(zip(title,s.row_values(col))))
            else:
                for col in range(0,s.nrows):
                    self._data.append(s.row_values(col))
        return self._data
# excel表格如下:
# | title1 | title2 |
# | value1 | value2 |
# | value3 | value4 |

# 如果title_line=True
#[{"title1": "value1", "title2": "value2"}, {"title1": "value3", "title2": "value4"}]

# 如果title_line=False
#[["title1", "title2"], ["value1", "value2"], ["value3", "value4"]]





if __name__ == '__main__':
    v = r'C:\Users\LUMI\PycharmProjects\Test_framework\config\config.yml'
    reader = YamlReader(v)
    print(reader.data)


    y = r'C:\Users\LUMI\PycharmProjects\Test_framework\config\baidu.xlsx'
    reader = ExcelReader(y,title_line=True)
    print(reader.data)

