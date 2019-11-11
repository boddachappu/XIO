
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 251)
        Dialog.setWindowIcon(QtGui.QIcon('dell.png'))
        self.labelUser = QtWidgets.QLabel(Dialog)
        self.labelUser.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.labelUser.setObjectName("labelUser")
        self.labelPassword = QtWidgets.QLabel(Dialog)
        self.labelPassword.setGeometry(QtCore.QRect(30, 100, 47, 13))
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditUserName = QtWidgets.QLineEdit(Dialog)
        self.lineEditUserName.setGeometry(QtCore.QRect(120, 50, 231, 20))
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(120, 100, 231, 20))
        self.lineEditPassword.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.labelEmpty = QtWidgets.QLabel(Dialog)
        self.labelEmpty.setGeometry(QtCore.QRect(30, 169, 321, 21))
        self.labelEmpty.setText("")
        self.labelEmpty.setObjectName("labelEmpty")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(159, 200, 191, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DELL-Authentication"))
        self.labelUser.setText(_translate("Dialog", "UserName"))
        self.labelPassword.setText(_translate("Dialog", "Password"))

def main():
    app=QtWidgets.QApplication(sys.argv)
    #app.setWindowIcon(QtGui.QIcon('dell.png'))
    Dialog=QtWidgets.QDialog()
    uiDial = Ui_Dialog()
    uiDial.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()