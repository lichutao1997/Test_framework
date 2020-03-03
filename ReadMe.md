####测试框架——Test_framework:
######具体配置:

    config（配置文件）
    data（数据文件）
    drivers（驱动）
    log（日志）
    report（报告）
    test（测试用例）
    utils（公共方法）
######一、config配置

    config.yml                   #url,日志参数配置
    
######二、data目录 

    存放测试用例的数据
######三、drivers

    存放驱动
######四、log目录
    
    存放输出的日志
######五、report测试报告

    report.html                  #存放html格式的测试报告
######六、test目录

    存放测试用例
######七、utils

    #存放公关方法
    config.py                     #存放路径，读取config.yml方法
    file_reader.py                #读取data
    HTMLTestRunner.py             #用于输出测试报告
    log.py                        #日志配置文件
    mail.py                       #用于邮箱发送测试报告
    