#coding:utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class mytable(QDialog):
    def __init__(self, list_dialog=None):
        QDialog.__init__(self)
        self.list_dialog = list_dialog
        print '执行mytable初始化函数'
        self.setWindowTitle = ('人员信息')
        self.setWindowIcon (QIcon('1.png'))
        self.resize = (600,800)
        self.setMaximumSize(800,800)
        self.setMinimumSize(560,250)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.model = QStandardItemModel(len(list_dialog),5)
        self.model.setHorizontalHeaderLabels(['id','姓名','性别','年龄','手机号'])
        for x in xrange(len(list_dialog)):
            tuple_1 = list_dialog[x]
            for y in xrange(0,5):
                item = QStandardItem('%s'%tuple_1[y])
                item.setTextAlignment(Qt.AlignCenter)
                self.model.setItem(x,y,item)
        self.tableView = QTableView()        
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.tableView)
        self.setLayout(layout_1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    list12 = []
    mytable_1 = mytable(list12)
    mytable_1.show()
    sys.exit(app.exec_())