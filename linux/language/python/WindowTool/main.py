
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from login import Ui_Form
from video_download import Ui_videodownload
from m4s import Bilibili

# 调试代码 ###########################
def my_excepthook(exc_type, exc_value, tb):
    msg = ' Traceback (most recent call last):\n'
    while tb:
        filename = tb.tb_frame.f_code.co_filename
        name = tb.tb_frame.f_code.co_name
        lineno = tb.tb_lineno
        msg += '   File "%.500s", line %d, in %.500s\n' % (filename, lineno, name)
        tb = tb.tb_next
    msg += ' %s: %s\n' %(exc_type.__name__, exc_value)
    print(msg)
sys.excepthook = my_excepthook
# 调试代码 ###########################

#验证
def loginButton():
    i=0
    user_pass_dict = {'1': '11'}
    #利用text()函数获取控件对象的值
    username = ui.username.text()
    password = ui.password.text()
    if username == '' or password == '':
        # 输出框
        msgBox = QMessageBox()
        msgBox.setWindowTitle('警告')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText('你没输入用户名或密码')
        msgBox.setInformativeText('是否返回继续尝试')
        # 消息框按钮
        turnback = msgBox.addButton('重新尝试', QMessageBox.AcceptRole)
        exit = msgBox.addButton('直接退出', QMessageBox.RejectRole)
        # 默认按钮
        msgBox.setDefaultButton(turnback)
        # 执行自定义的消息框
        reply = msgBox.exec()
        if reply == QMessageBox.RejectRole:
           loginwindow.close()

    elif not user_pass_dict.get(username) or (user_pass_dict[username] != password):
         msg = '身份验证失败'
         msgBox = QMessageBox()
         msgBox.setWindowTitle('警告')
         msgBox.setIcon(QMessageBox.Warning)
         msgBox.setText(msg)
         msgBox.setInformativeText('是否返回继续尝试')
         turnback = msgBox.addButton('重新尝试', QMessageBox.AcceptRole)
         exit = msgBox.addButton('直接退出', QMessageBox.RejectRole)
         msgBox.setDefaultButton(turnback)
         reply = msgBox.exec()
         if reply == QMessageBox.RejectRole:
             loginwindow.close()
         elif reply == QMessageBox.AcceptRole:
             if i == 2:
                 QMessageBox.information(loginwindow, '错误', '失败次数过多', QMessageBox.Ok)
                 loginwindow.close()
             else:
                 i = i + 1
                 msg = '失败次数: ' + str(i) + '次'
                 ui.failnum.setText(msg)
                 ui.username.clear()
                 ui.password.clear()
    else:
        msg = '恭喜你验证成功'
        QMessageBox.information(loginwindow, '成功', msg, QMessageBox.Ok, QMessageBox.Ok)
        # 关闭一个窗口，打开另一个窗口
        loginwindow.close()
        downloadwindow.show()

# 选择目录
def funcopendir():
    get_directory_path = QFileDialog.getExistingDirectory(downloadwindow,"选取指定文件夹","C:/Users/bang/Desktop")
    ui1.storagedir.setText(str(get_directory_path))

# 多线程
class WorkThread(QThread):
    trigger = pyqtSignal(str)
    def __int__(self):
        super(WorkThread, self).__init__()
    # 线程执行调用run方法
    def run(self):
        self.trigger.emit(str('####下载开始+++++'))
        index_url = ui1.videolink.text()
        storage_dir = ui1.storagedir.text() + '/'
        start = ui1.starnum.text()
        end = ui1.endnum.text()
        if index_url == '' or storage_dir == '' or start == '' or end == '':
            msg = '你有必要信息没填'
            self.trigger.emit(str(msg))
        else:
            start = int(start) - 1
            end = int(end)
            udnum_list = []
            for i in range(start, end):
                udnum_list.append(i)
            bilibili = Bilibili(index_url, storage_dir)
            name_list = bilibili.get_name()
            for i in udnum_list:
                xiazai =  '正在下载\n' + name_list[i]
                wancheng = '下载完成\n'
            info = bilibili.getVideoUrl(name_list)
            self.trigger.emit(str(xiazai))
            bilibili.GetBiliVideo(info, udnum_list)
            self.trigger.emit(str(wancheng))
            QMessageBox.information(loginwindow, '提示', '下载完成', QMessageBox.Ok)
            downloadwindow.close()
def execute():
    # 调用线程的run方法
    work.start()
    # 线程自定义的信号
    work.trigger.connect(display)

def display(str):
    ui1.processlog.addItem(str)



if __name__ == '__main__':
    #打开一个应用
    app = QtWidgets.QApplication([])

    # 创建一个窗口
    loginwindow = QtWidgets.QTableWidget()
    #实例化ui类
    ui = Ui_Form()
    #将ui类的实例放到窗口中运行
    ui.setupUi(loginwindow)
    ui.verification.clicked.connect(loginButton)  # 设置登陆界面按钮点击事件
    ui.exit.clicked.connect(loginwindow.close)

    downloadwindow = QtWidgets.QTableWidget()
    ui1 = Ui_videodownload()
    ui1.setupUi(downloadwindow)  # 启动运行
    # 必须在这里实例化，不能在execute中实例化
    work = WorkThread()
    ui1.downloadButton.clicked.connect(execute)  # 设置调试界面按钮点击事件
    ui1.opendir.clicked.connect(funcopendir)
    ui1.outButton.clicked.connect(downloadwindow.close)

    loginwindow.show()    #  显示登陆界面
    # downloadwindow.show()

    sys.exit(app.exec())

