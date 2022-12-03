

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_graph_bokeh:
    def setupUi(self, graph_bokeh):
        graph_bokeh.setObjectName("graph_matplotlib")
        graph_bokeh.resize(912, 717)
        self.label = QtWidgets.QLabel(graph_bokeh)
        self.label.setGeometry(QtCore.QRect(60, 50, 811, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(graph_bokeh)
        self.label_2.setGeometry(QtCore.QRect(130, 180, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(graph_bokeh)
        self.label_3.setGeometry(QtCore.QRect(130, 250, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_plot_btn = QtWidgets.QPushButton(graph_bokeh)
        self.line_plot_btn.setGeometry(QtCore.QRect(600, 170, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_plot_btn.setFont(font)
        self.line_plot_btn.setObjectName("simple_plot_btn")
        self.scatter_plot_btn = QtWidgets.QPushButton(graph_bokeh)
        self.scatter_plot_btn.setGeometry(QtCore.QRect(600, 230, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.scatter_plot_btn.setFont(font)
        self.scatter_plot_btn.setObjectName("scatter_plot_btn")
        self.bar_btn = QtWidgets.QPushButton(graph_bokeh)
        self.bar_btn.setGeometry(QtCore.QRect(600, 280, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bar_btn.setFont(font)
        self.bar_btn.setObjectName("bar_btn")

        self.ui_X_column = QtWidgets.QLineEdit(graph_bokeh)
        self.ui_X_column.setGeometry(QtCore.QRect(300, 180, 113, 22))
        self.ui_X_column.setObjectName("ui_X_column")
        self.ui_Y_column = QtWidgets.QLineEdit(graph_bokeh)
        self.ui_Y_column.setGeometry(QtCore.QRect(300, 250, 113, 22))
        self.ui_Y_column.setObjectName("ui_Y_column")
        self.step_btn = QtWidgets.QPushButton(graph_bokeh)
        self.step_btn.setGeometry(QtCore.QRect(600, 390, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.step_btn.setFont(font)
        self.step_btn.setObjectName("step_btn")

        self.retranslateUi(graph_bokeh)
        QtCore.QMetaObject.connectSlotsByName(graph_bokeh)

    def retranslateUi(self, graph_bokeh):
        _translate = QtCore.QCoreApplication.translate
        graph_bokeh.setWindowTitle(_translate("graph_matplotlib", "Bokeh Graph"))
        self.label.setText(_translate("graph_matplotlib", "GRAPHICAL VISUALIZATION OF DATA WITH BOKEH"))
        self.label_2.setText(_translate("graph_matplotlib", "X column name"))
        self.label_3.setText(_translate("graph_matplotlib", "Y column name"))
        self.line_plot_btn.setText(_translate("graph_matplotlib", "Line plot"))
        self.scatter_plot_btn.setText(_translate("graph_matplotlib", "Scatter plot"))
        self.bar_btn.setText(_translate("graph_matplotlib", "Bar plot"))
        self.step_btn.setText(_translate("graph_matplotlib", "Step plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graph_with_bokeh = QtWidgets.QDialog()
    ui = Ui_graph_bokeh()
    ui.setupUi(graph_with_bokeh)
    graph_with_bokeh.show()
    sys.exit(app.exec_())
