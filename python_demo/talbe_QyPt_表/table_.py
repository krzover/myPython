#coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
class MyTable(QDialog):
    """docstring for ClassName"""
    def __init__(self, list_arg=None):
        QDialog.__init__(self)
        self.list_arg = list_arg
        self.setWindowTitle('人员信息表')
        self.setWindowIcon(QIcon('1.png'))
        self.resize(1100,600)
        self.setMaximumSize(650,210)
        self.setMinimumSize(650,210)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.model=QStandardItemModel(5,5)
        self.model.setHorizontalHeaderLabels(['编号','姓名','年龄','性别','出生日期','手机号'])
        for  x in xrange(0,5):
            for y in xrange(0,6):
                item = QStandardItem('%d行%d列'%(x,y))
                self.model.setItem(x,y,item)
        self.tabletView=QTableView()
        self.tabletView.setModel(self.model)
        self.tabletView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        Iayout=QVBoxLayout()
        Iayout.addWidget(self.tabletView)
        self.setLayout(Iayout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    my_table=MyTable()
    my_table.show()
    sys.exit(app.exec_())
