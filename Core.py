from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from decimal import Decimal
import sys

MainUI,_ = loadUiType('Scheduler.ui')

class Main(QMainWindow , MainUI):

    g_scale = 10

    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('CPU Scheduler')
        self.setWindowIcon(QtGui.QIcon("CPU2.png"))
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)
        self.Handle_events()
        self.AutoResize_Tables()
        self.lineEdit_13.setText('   5')

    def Handle_events(self):
        self.pushButton_14.clicked.connect(self.Back)
        self.pushButton_17.clicked.connect(self.Back)
        self.pushButton_20.clicked.connect(self.Back)
        self.pushButton_23.clicked.connect(self.Back)
        self.pushButton_26.clicked.connect(self.Back)
        self.pushButton_29.clicked.connect(self.Back)
        self.pushButton_14.clicked.connect(self.Back)
        self.pushButton_7.clicked.connect(self.Back)
        self.pushButton_11.clicked.connect(self.Back)
        self.pushButton_3.clicked.connect(self.Open_FCFS_Tab)
        self.pushButton_2.clicked.connect(self.Show_info_Table_FCFS)
        self.pushButton_4.clicked.connect(self.Open_RR_Tab)
        self.pushButton_5.clicked.connect(self.Open_SJF_Choices_Tab)
        self.pushButton_6.clicked.connect(self.Open_Priority_Choices_Tab)
        self.pushButton_13.clicked.connect(self.Open_SJF_NP_Tab)
        self.pushButton_12.clicked.connect(self.Open_SJF_P_Tab)
        self.pushButton_22.clicked.connect(self.Open_Priority_NP_Tab)
        self.pushButton_21.clicked.connect(self.Open_Priority_P_Tab)
        self.pushButton_8.clicked.connect(self.FCSF_Algorithm)
        self.pushButton_15.clicked.connect(self.Show_Info_Table_SJF_NP)
        self.pushButton_16.clicked.connect(self.SJF_NP_Algorithm)
        self.pushButton_24.clicked.connect(self.Show_Info_Table_Priority_NP)
        self.pushButton_25.clicked.connect(self.Priority_NP_Algorithm)
        self.pushButton_9.clicked.connect(self.Show_Info_Table_RR)
        self.pushButton_10.clicked.connect(self.RR_Algorithm)
        self.pushButton_18.clicked.connect(self.Show_Info_Table_SJF_P)
        self.pushButton_19.clicked.connect(self.SJF_P_Algorithm)
        self.pushButton_32.clicked.connect(self.SJF_P_Zoom_In)
        self.pushButton_31.clicked.connect(self.SJF_P_Zoom_Out)
        self.pushButton_33.clicked.connect(self.FCFS_Zoom_In)
        self.pushButton_34.clicked.connect(self.FCFS_Zoom_Out)
        self.pushButton_35.clicked.connect(self.RR_Zoom_In)
        self.pushButton_36.clicked.connect(self.RR_Zoom_Out)
        self.pushButton_37.clicked.connect(self.SJF_NP_Zoom_In)
        self.pushButton_38.clicked.connect(self.SJF_NP_Zoom_Out)
        self.pushButton_39.clicked.connect(self.Priority_NP_Zoom_In)
        self.pushButton_40.clicked.connect(self.Priority_NP_Zoom_Out)
        self.pushButton_27.clicked.connect(self.Show_info_Table_Priority_P)
        self.pushButton_28.clicked.connect(self.Priority_P_Algorithm)
        self.pushButton_41.clicked.connect(self.Priority_P_Zoom_In)
        self.pushButton_42.clicked.connect(self.Priority_P_Zoom_Out)



    def SJF_P_Zoom_In(self):
        Main.g_scale += 10
        self.SJF_P_Algorithm()

    def SJF_P_Zoom_Out(self):
        if Main.g_scale != 10:
            Main.g_scale -= 10
            self.SJF_P_Algorithm()

    def FCFS_Zoom_In(self):
        Main.g_scale += 10
        self.FCSF_Algorithm()

    def FCFS_Zoom_Out(self):
        if Main.g_scale != 10:
            Main.g_scale -= 10
            self.FCSF_Algorithm()

    def RR_Zoom_In(self):
        Main.g_scale += 10
        self.RR_Algorithm()

    def RR_Zoom_Out(self):
        if Main.g_scale != 10:
            Main.g_scale -= 10
            self.RR_Algorithm()

    def SJF_NP_Zoom_In(self):
        Main.g_scale += 10
        self.SJF_NP_Algorithm()

    def SJF_NP_Zoom_Out(self):
        if Main.g_scale != 10:
            Main.g_scale -= 10
            self.SJF_NP_Algorithm()

    def Priority_NP_Zoom_In(self):
        Main.g_scale += 10
        self.Priority_NP_Algorithm()

    def Priority_NP_Zoom_Out(self):
        if Main.g_scale != 10:
            Main.g_scale -= 10
            self.Priority_NP_Algorithm()

    def Priority_P_Zoom_In(self):
        Main.g_scale += 10
        self.Priority_P_Algorithm()

    def Priority_P_Zoom_Out(self):
        if Main.g_scale != 10:
            Main.g_scale -= 10
            self.Priority_P_Algorithm()



    def AutoResize_Tables(self):
        header = self.tableWidget_3.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_1 = self.tableWidget_5.horizontalHeader()
        header_1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_1.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_2 = self.tableWidget_7.horizontalHeader()
        header_2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_3 = self.tableWidget_9.horizontalHeader()
        header_3.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_3.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_3 = self.tableWidget_6.horizontalHeader()
        header_3.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_3.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_4 = self.tableWidget_8.horizontalHeader()
        header_4.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_4.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)


    def Open_FCFS_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_RR_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Back(self):
        while self.tableWidget_3.rowCount() > 0:
            self.tableWidget_3.removeRow(0)
        self.lineEdit.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        self.lineEdit_2.clear()

        while self.tableWidget_9.rowCount() > 0:
            self.tableWidget_9.removeRow(0)
        self.lineEdit_3.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_2.setScene(scene)
        self.lineEdit_4.clear()

        while self.tableWidget_5.rowCount() > 0:
            self.tableWidget_5.removeRow(0)
        self.lineEdit_5.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_3.setScene(scene)
        self.lineEdit_6.clear()

        while self.tableWidget_6.rowCount() > 0:
            self.tableWidget_6.removeRow(0)
        self.lineEdit_7.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_4.setScene(scene)
        self.lineEdit_8.clear()

        while self.tableWidget_7.rowCount() > 0:
            self.tableWidget_7.removeRow(0)
        self.lineEdit_9.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_5.setScene(scene)
        self.lineEdit_10.clear()

        while self.tableWidget_8.rowCount() > 0:
            self.tableWidget_8.removeRow(0)
        self.lineEdit_11.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_6.setScene(scene)
        self.lineEdit_12.clear()

        self.tabWidget.setCurrentIndex(0)


    def Open_SJF_Choices_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Priority_Choices_Tab(self):
        self.tabWidget.setCurrentIndex(6)

    def Open_SJF_NP_Tab(self):
        self.tabWidget.setCurrentIndex(4)

    def Open_SJF_P_Tab(self):
        self.tabWidget.setCurrentIndex(5)

    def Open_Priority_NP_Tab(self):
        self.tabWidget.setCurrentIndex(7)

    def Open_Priority_P_Tab(self):
        self.tabWidget.setCurrentIndex(8)

    def Show_info_Table_FCFS(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(scene)
            self.lineEdit_2.clear()
            number_str = self.lineEdit.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_3.setRowCount(i)
                        self.tableWidget_3.insertRow(i)
                        self.tableWidget_3.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
            else:
                QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
        except:
            QMessageBox.information(self, "Warning", "Invalid input, make sure  processes number is not float or empty!")

    def FCSF_Algorithm(self):
        try:
            n = int(self.lineEdit.text())
            processes = []
            burst_time = []
            arrival_time = []
            arr = []   # time_line
            arr2 = []  # strings
            timer = Decimal('0.00')
            s = 0
            for i in range(n):
                if self.tableWidget_3.item(i, 0).text() not in processes:
                    processes.append(self.tableWidget_3.item(i, 0).text())
                else:
                    QMessageBox.information(self, "Warning", "Repeated processes are not allowed !")
                    return
                if Decimal(self.tableWidget_3.item(i, 1).text()) >= 0:
                    arrival_time.append(Decimal(self.tableWidget_3.item(i, 1).text()))

                else:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter positive 'Arrival Time' !")
                    return
                if Decimal(self.tableWidget_3.item(i, 2).text()) > 0:
                    burst_time.append(Decimal(self.tableWidget_3.item(i, 2).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, 'Burst Time' must be higher than '0' !")
                    return

            for i in range(n):
                for j in range(0, n - i - 1):
                    if arrival_time[j] > arrival_time[j + 1]:
                        arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                        burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]
                        processes[j], processes[j + 1] = processes[j + 1], processes[j]
            for i in range(n):
                if timer >= arrival_time[i]:
                    arr2.append(processes[i])
                    arr.append(burst_time[i] + timer)
                    s += Decimal(timer - arrival_time[i])
                    timer += Decimal(burst_time[i])
                else:
                    arr2.append('IDLE' + '  ')
                    arr.append(arrival_time[i])
                    timer = Decimal(arrival_time[i])
                    arr2.append(processes[i])
                    arr.append(burst_time[i] + timer)
                    s += Decimal(timer - arrival_time[i])
                    timer += Decimal(burst_time[i])

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(scene)
            scale = Main.g_scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            for i in range(len(arr)):
                if i == 0:
                    mytext2 = QGraphicsSimpleTextItem('0')
                    scene.addItem(mytext2)
                    mytext2.setPos(0, 85)
                    mytext2.setScale(1.3)
                    mytext2 = QGraphicsSimpleTextItem(str(arr[0]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[0] * scale, 85)
                    mytext2.setScale(1.3)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[0] * scale, 80))
                    scene.addRect(r, pen)
                    mytext1 = QGraphicsSimpleTextItem(str(arr2[0]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[0] + 0) / 2, 30)
                    mytext1.setScale(1.5)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[i] * scale, 80))
                    scene.addRect(r, pen)

                    mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[i] + arr[i - 1]) / 2, 30)
                    mytext1.setScale(1.5)

                    mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[i] * scale, 85)
                    mytext2.setScale(1.3)

            self.lineEdit_2.setText('  '+str("%.2f" % (s/n))+' '+'ms')
        except:
            QMessageBox.information(self, "Warning", "Nothing to simulate, Please enter valid information")


    def Show_Info_Table_SJF_NP(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_3.setScene(scene)
            self.lineEdit_6.clear()
            number_str = self.lineEdit_5.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_5.setRowCount(i)
                        self.tableWidget_5.insertRow(i)
                        self.tableWidget_5.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
            else:
                QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
        except:
            QMessageBox.information(self, "Warning", "Invalid input, make sure  processes number is not float or empty!")



    def SJF_NP_Algorithm(self):
        try:
            n = int(self.lineEdit_5.text())
            processes = []
            arrival_time = []
            burst_time = []
            arr = []  # time_line
            arr2 = []  # strings
            counter = 0
            timer = Decimal('0.00')
            s = 0
            for i in range(n):
                if self.tableWidget_5.item(i, 0).text() not in processes:
                    processes.append(self.tableWidget_5.item(i, 0).text())
                else:
                    QMessageBox.information(self, "Warning", "Repeated processes are not allowed !")
                    return
                if Decimal(self.tableWidget_5.item(i, 1).text()) >= 0:
                    arrival_time.append(Decimal(self.tableWidget_5.item(i, 1).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter positive 'Arrival Time' !")
                    return
                if Decimal(self.tableWidget_5.item(i, 2).text()) > 0:
                    burst_time.append(Decimal(self.tableWidget_5.item(i, 2).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, 'Burst Time' must be higher than '0' !")
                    return

            for i in range(n):
                for j in range(0, n - i - 1):
                    if arrival_time[j] > arrival_time[j + 1]:
                        arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                        processes[j], processes[j + 1] = processes[j + 1], processes[j]
                        burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]

            flag = False
            idle_flag = False
            while counter != len(arrival_time):
                available_t = []
                available_p = []
                for i in range(counter, len(arrival_time)):
                    if arrival_time[i] <= timer:
                        if idle_flag:
                            arr.append(timer)
                            arr2.append('IDLE')
                            idle_flag = False
                        available_t.append(burst_time[i])
                        available_p.append(processes[i])
                        flag = True

                if len(available_t) == 0:
                    timer += Decimal('0.01')
                    idle_flag = True

                if flag:
                    for i in range(len(available_t)):
                        for j in range(0, len(available_t) - i - 1):
                            if available_t[j] > available_t[j + 1]:
                                available_t[j], available_t[j + 1] = available_t[j + 1], available_t[j]
                                available_p[j], available_p[j + 1] = available_p[j + 1], available_p[j]

                    for i in range(len(available_t)):
                        arr2.append(available_p[i])
                        arr.append(timer + available_t[i])
                        index = processes.index(available_p[i])
                        s += Decimal(timer - arrival_time[index])
                        timer += Decimal(available_t[i])
                        counter += 1
                    flag = False

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_3.setScene(scene)
            scale = Main.g_scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            for i in range(len(arr)):
                if i == 0:
                    mytext2 = QGraphicsSimpleTextItem('0')
                    scene.addItem(mytext2)
                    mytext2.setPos(0, 85)
                    mytext2.setScale(1.3)
                    mytext2 = QGraphicsSimpleTextItem(str(arr[0]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[0] * scale, 85)
                    mytext2.setScale(1.3)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[0] * scale, 80))
                    scene.addRect(r, pen)
                    mytext1 = QGraphicsSimpleTextItem(str(arr2[0]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[0] + 0) / 2, 30)
                    mytext1.setScale(1.5)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[i] * scale, 80))
                    scene.addRect(r, pen)

                    mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[i] + arr[i - 1]) / 2, 30)
                    mytext1.setScale(1.5)

                    mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[i] * scale, 85)
                    mytext2.setScale(1.3)

            self.lineEdit_6.setText('  ' + str("%.2f" % (s/n)) + ' ' + 'ms')
        except:
            QMessageBox.information(self, "Warning", "Nothing to simulate, Please enter valid information")


    def Show_Info_Table_Priority_NP(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_5.setScene(scene)
            self.lineEdit_10.clear()
            number_str = self.lineEdit_9.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_7.setRowCount(i)
                        self.tableWidget_7.insertRow(i)
                        self.tableWidget_7.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
            else:
                QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
        except:
            QMessageBox.information(self, "Warning", "Invalid input, make sure  processes number is not float or empty!")

    def Priority_NP_Algorithm(self):
        try:
            n = int(self.lineEdit_9.text())
            processes = []
            arrival_time = []
            burst_time = []
            priority = []
            arr = []  # time_line
            arr2 = []  # strings
            counter = 0
            timer = Decimal('0.00')
            s = 0
            for i in range(n):
                if self.tableWidget_7.item(i, 0).text() not in processes:
                    processes.append(self.tableWidget_7.item(i, 0).text())
                else:
                    QMessageBox.information(self, "Warning", "Repeated processes are not allowed !")
                    return
                if Decimal(self.tableWidget_7.item(i, 1).text()) >= 0:
                    arrival_time.append(Decimal(self.tableWidget_7.item(i, 1).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter positive 'Arrival Time' !")
                    return
                if Decimal(self.tableWidget_7.item(i, 2).text()) > 0:
                    burst_time.append(Decimal(self.tableWidget_7.item(i, 2).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, 'Burst Time' must be higher than '0' !")
                    return
                if Decimal(self.tableWidget_7.item(i, 3).text()) > 0:
                    priority.append(Decimal(self.tableWidget_7.item(i, 3).text()))
                else:
                    QMessageBox.information(self, "Warning", " Invalid input, 'Burst time' and 'Priority' must be higher than '0' !")
                    return


            for i in range(n):
                for j in range(0, n - i - 1):
                    if arrival_time[j] > arrival_time[j + 1]:
                        arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                        processes[j], processes[j + 1] = processes[j + 1], processes[j]
                        burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]
                        priority[j], priority[j + 1] = priority[j + 1], priority[j]

            flag = False
            idle_flag = False
            while counter != len(arrival_time):
                available_t = []
                available_p = []
                available_priority = []
                for i in range(counter, len(arrival_time)):
                    if arrival_time[i] <= timer:
                        if idle_flag:
                            arr.append(timer)
                            arr2.append('IDLE')
                            idle_flag = False
                        available_t.append(burst_time[i])
                        available_p.append(processes[i])
                        available_priority.append(priority[i])
                        flag = True
                if len(available_t) == 0:
                    timer += Decimal('0.01')

                    idle_flag = True

                if flag:
                    for i in range(len(available_t)):
                        for j in range(0, len(available_t) - i - 1):
                            if available_priority[j] > available_priority[j + 1]:
                                available_priority[j], available_priority[j + 1] = available_priority[j + 1], available_priority[j]
                                available_t[j], available_t[j + 1] = available_t[j + 1], available_t[j]
                                available_p[j], available_p[j + 1] = available_p[j + 1], available_p[j]

                    for i in range(len(available_t)):
                        arr2.append(available_p[i])
                        arr.append(timer + available_t[i])
                        index = processes.index(available_p[i])
                        s += Decimal(timer - arrival_time[index])
                        timer += Decimal(available_t[i])
                        counter += 1
                    flag = False

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_5.setScene(scene)
            scale = Main.g_scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            for i in range(len(arr)):
                if i == 0:
                    mytext2 = QGraphicsSimpleTextItem('0')
                    scene.addItem(mytext2)
                    mytext2.setPos(0, 85)
                    mytext2.setScale(1.3)
                    mytext2 = QGraphicsSimpleTextItem(str(arr[0]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[0] * scale, 85)
                    mytext2.setScale(1.3)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[0] * scale, 80))
                    scene.addRect(r, pen)
                    mytext1 = QGraphicsSimpleTextItem(str(arr2[0]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[0] + 0) / 2, 30)
                    mytext1.setScale(1.5)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[i] * scale, 80))
                    scene.addRect(r, pen)

                    mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[i] + arr[i - 1]) / 2, 30)
                    mytext1.setScale(1.5)

                    mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[i] * scale, 85)
                    mytext2.setScale(1.3)

            self.lineEdit_10.setText('  ' + str("%.2f" % (s/n)) + ' ' + 'ms')
        except:
            QMessageBox.information(self, "Warning", "Nothing to simulate, Please enter valid information")



    def Show_Info_Table_RR(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_2.setScene(scene)
            self.lineEdit_4.clear()
            number_str = self.lineEdit_3.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_9.setRowCount(i)
                        self.tableWidget_9.insertRow(i)
                        self.tableWidget_9.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
            else:
                QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
        except:
            QMessageBox.information(self, "Warning", "Invalid input, make sure  processes number is not float or empty!")



    def RR_Algorithm(self):
        try:
            n = int(self.lineEdit_3.text())
            if Decimal(self.lineEdit_13.text()) > 0:
                q = Decimal(self.lineEdit_13.text())
            else:
                QMessageBox.information(self, "Warning", "Invalid Input, Time Quantum must be higher than '0' !")
                return
            processes = []
            arrival_time = []
            burst_time = []
            arr = []  # time_line
            arr2 = []  # strings
            timer = Decimal('0.00')
            s = 0
            for i in range(n):
                if self.tableWidget_9.item(i, 0).text() not in processes:
                    processes.append(self.tableWidget_9.item(i, 0).text())
                else:
                    QMessageBox.information(self, "Warning", "Repeated processes are not allowed !")
                    return
                if Decimal(self.tableWidget_9.item(i, 1).text()) >= 0:
                    arrival_time.append(Decimal(self.tableWidget_9.item(i, 1).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter positive 'Arrival Time' !")
                    return

                if Decimal(self.tableWidget_9.item(i, 2).text()) > 0:
                    burst_time.append(Decimal(self.tableWidget_9.item(i, 2).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, 'Burst Time' must be higher than '0' !")
                    return

            for i in range(n):
                for j in range(0, n - i - 1):
                    if arrival_time[j] > arrival_time[j + 1]:
                        arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                        processes[j], processes[j + 1] = processes[j + 1], processes[j]
                        burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]

            idle_flag = False
            while not all(v == 0 for v in burst_time):
                exe_flag = True
                for i in range(len(burst_time)):
                    if arrival_time[i] <= timer and burst_time[i] != 0:
                        exe_flag = False
                        if idle_flag:
                            arr.append(timer)
                            arr2.append('IDLE')
                            idle_flag = False

                        if burst_time[i] >= q:
                            arr2.append(processes[i])
                            arr.append(timer + q)
                            timer += q
                            burst_time[i] -= q
                        else:
                            arr2.append(processes[i])
                            arr.append(timer + burst_time[i])
                            timer += burst_time[i]
                            burst_time[i] = 0

                if exe_flag:
                    timer += Decimal('0.01')
                    idle_flag = True

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_2.setScene(scene)
            scale = Main.g_scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            for i in range(len(arr)):
                if i == 0:
                    mytext2 = QGraphicsSimpleTextItem('0')
                    scene.addItem(mytext2)
                    mytext2.setPos(0, 85)
                    mytext2.setScale(1.3)
                    mytext2 = QGraphicsSimpleTextItem(str(arr[0]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[0] * scale, 85)
                    mytext2.setScale(1.3)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[0] * scale, 80))
                    scene.addRect(r, pen)
                    mytext1 = QGraphicsSimpleTextItem(str(arr2[0]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[0] + 0) / 2, 30)
                    mytext1.setScale(1.5)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[i] * scale, 80))
                    scene.addRect(r, pen)

                    mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[i] + arr[i - 1]) / 2, 30)
                    mytext1.setScale(1.5)

                    mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[i] * scale, 85)
                    mytext2.setScale(1.3)

            hits = [Decimal('0.00')]
            for i in range(len(arr)):
                hits.append(arr[i])
            for i in range(len(processes)):
                s += Decimal(hits[arr2.index(processes[i])] - arrival_time[i])
            self.lineEdit_4.setText('  ' + str("%.2f" % (s/n)) + ' ' + 'ms')

        except:
            QMessageBox.information(self, "Warning", "Nothing to simulate, Please enter valid information")



    def Show_Info_Table_SJF_P(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_4.setScene(scene)
            self.lineEdit_8.clear()
            number_str = self.lineEdit_7.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_6.setRowCount(i)
                        self.tableWidget_6.insertRow(i)
                        self.tableWidget_6.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
            else:
                QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
        except:
            QMessageBox.information(self, "Warning", "Invalid input, make sure  processes number is not float or empty!")



    def SJF_P_Algorithm(self):
        try:
            n = int(self.lineEdit_7.text())
            processes = []
            arrival_time = []
            burst_time = []
            arr = []  # time_line
            arr2 = []  # strings
            timer = Decimal('0.00')
            s = 0
            for i in range(n):
                if self.tableWidget_6.item(i, 0).text() not in processes:
                    processes.append(self.tableWidget_6.item(i, 0).text())
                else:
                    QMessageBox.information(self, "Warning", "Repeated processes are not allowed !")
                    return
                if Decimal(self.tableWidget_6.item(i, 1).text()) >= 0:
                    arrival_time.append(Decimal(self.tableWidget_6.item(i, 1).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter positive 'Arrival Time' !")
                    return
                if Decimal(self.tableWidget_6.item(i, 2).text()) > 0:
                    burst_time.append(Decimal(self.tableWidget_6.item(i, 2).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, 'Burst Time' must be higher than '0' !")
                    return

            for i in range(n):
                for j in range(0, n - i - 1):
                    if arrival_time[j] > arrival_time[j + 1]:
                        arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                        processes[j], processes[j + 1] = processes[j + 1], processes[j]
                        burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]

            idle_flag = False
            while not all(v == 0 for v in burst_time):
                available_p = []
                available_t = []
                for i in range(len(burst_time)):
                    if arrival_time[i] <= timer and burst_time[i] != 0:
                        if idle_flag:
                            arr.append(timer)
                            arr2.append('IDLE')
                            idle_flag = False
                        available_p.append(processes[i])
                        available_t.append(burst_time[i])

                if len(available_t) == 0:
                    idle_flag = True

                if len(available_t):
                    if len(arr2):
                        if arr2[len(arr2)-1] != available_p[available_t.index(min(available_t))]:
                            arr2.append(available_p[available_t.index(min(available_t))])
                            arr.append(timer + Decimal('0.01'))
                            x = processes.index(str(available_p[available_t.index(min(available_t))]))
                            burst_time[x] -= Decimal('0.01')

                        else:
                            x = processes.index(str(available_p[available_t.index(min(available_t))]))
                            burst_time[x] -= Decimal('0.01')
                            arr[len(arr)-1] += Decimal('0.01')

                    else:
                        arr2.append(available_p[available_t.index(min(available_t))])
                        arr.append(timer + Decimal('0.01'))
                        x = processes.index(str(available_p[available_t.index(min(available_t))]))
                        burst_time[x] -= Decimal('0.01')

                timer += Decimal('0.01')

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_4.setScene(scene)
            scale = Main.g_scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            for i in range(len(arr)):
                if i == 0:
                    mytext2 = QGraphicsSimpleTextItem('0')
                    scene.addItem(mytext2)
                    mytext2.setPos(0, 85)
                    mytext2.setScale(1.3)
                    mytext2 = QGraphicsSimpleTextItem(str(arr[0]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[0] * scale, 85)
                    mytext2.setScale(1.3)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[0] * scale, 80))
                    scene.addRect(r, pen)
                    mytext1 = QGraphicsSimpleTextItem(str(arr2[0]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[0] + 0) / 2, 30)
                    mytext1.setScale(1.5)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[i] * scale, 80))
                    scene.addRect(r, pen)

                    mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[i] + arr[i - 1]) / 2, 30)
                    mytext1.setScale(1.5)

                    mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[i] * scale, 85)
                    mytext2.setScale(1.3)

            hits = [Decimal('0.00')]
            for i in range(len(arr)):
                hits.append(arr[i])
            for i in range(len(processes)):
                p = processes[i]
                arrival = arrival_time[i]
                for j in range(len(arr2)):
                    if arr2[j] == p:
                        s += Decimal(hits[j] - arrival)
                        arrival = hits[j+1]

            self.lineEdit_8.setText('  ' + str("%.2f" % (s/n)) + ' ' + 'ms')

        except:
            QMessageBox.information(self, "Warning", "Nothing to simulate, Please enter valid information")



    def Show_info_Table_Priority_P(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_6.setScene(scene)
            self.lineEdit_12.clear()
            number_str = self.lineEdit_11.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_8.setRowCount(i)
                        self.tableWidget_8.insertRow(i)
                        self.tableWidget_8.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
            else:
                QMessageBox.information(self, "Warning", "Invalid input, Please enter number of processes")
        except:
            QMessageBox.information(self, "Warning", "Invalid input, make sure  processes number is not float or empty!")


    def Priority_P_Algorithm(self):
        try:
            n = int(self.lineEdit_11.text())
            processes = []
            arrival_time = []
            burst_time = []
            priority = []
            arr = []  # time_line
            arr2 = []  # strings
            timer = Decimal('0.00')
            s = 0
            for i in range(n):
                if self.tableWidget_8.item(i, 0).text() not in processes:
                    processes.append(self.tableWidget_8.item(i, 0).text())
                else:
                    QMessageBox.information(self, "Warning", "Repeated processes are not allowed !")
                    return
                if Decimal(self.tableWidget_8.item(i, 1).text()) >= 0:
                    arrival_time.append(Decimal(self.tableWidget_8.item(i, 1).text()))
                else:
                    QMessageBox.information(self, "Warning", "Invalid input, Please enter positive 'Arrival Time' !")
                    return

                if Decimal(self.tableWidget_8.item(i, 2).text()) > 0:
                    burst_time.append(Decimal(self.tableWidget_8.item(i, 2).text()))
                    priority.append(Decimal(self.tableWidget_8.item(i, 3).text()))
                else:
                    QMessageBox.information(self, "Warning", " Invalid input, 'Burst time' and 'Priority' must be higher than '0' !")
                    return

            for i in range(n):
                for j in range(0, n - i - 1):
                    if arrival_time[j] > arrival_time[j + 1]:
                        arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                        processes[j], processes[j + 1] = processes[j + 1], processes[j]
                        burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]
                        priority[j], priority[j + 1] = priority[j + 1], priority[j]

            idle_flag = False
            while not all(v == 0 for v in burst_time):
                available_p = []
                available_t = []
                available_priority = []
                for i in range(len(burst_time)):
                    if arrival_time[i] <= timer and burst_time[i] != 0:
                        if idle_flag:
                            arr.append(timer)
                            arr2.append('IDLE')
                            idle_flag = False
                        available_p.append(processes[i])
                        available_t.append(burst_time[i])
                        available_priority.append(priority[i])

                if len(available_t) == 0:
                    idle_flag = True

                if len(available_t):
                    if len(arr2):
                        if arr2[len(arr2)-1] != available_p[available_priority.index(min(available_priority))]:
                            arr2.append(available_p[available_priority.index(min(available_priority))])
                            arr.append(timer + Decimal('0.01'))
                            x = processes.index(str(available_p[available_priority.index(min(available_priority))]))
                            burst_time[x] -= Decimal('0.01')

                        else:
                            x = processes.index(str(available_p[available_priority.index(min(available_priority))]))
                            burst_time[x] -= Decimal('0.01')
                            arr[len(arr)-1] += Decimal('0.01')

                    else:
                        arr2.append(available_p[available_priority.index(min(available_priority))])
                        arr.append(timer + Decimal('0.01'))
                        x = processes.index(str(available_p[available_priority.index(min(available_priority))]))
                        burst_time[x] -= Decimal('0.01')

                timer += Decimal('0.01')

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_6.setScene(scene)
            scale = Main.g_scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            for i in range(len(arr)):
                if i == 0:
                    mytext2 = QGraphicsSimpleTextItem('0')
                    scene.addItem(mytext2)
                    mytext2.setPos(0, 85)
                    mytext2.setScale(1.3)
                    mytext2 = QGraphicsSimpleTextItem(str(arr[0]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[0] * scale, 85)
                    mytext2.setScale(1.3)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[0] * scale, 80))
                    scene.addRect(r, pen)
                    mytext1 = QGraphicsSimpleTextItem(str(arr2[0]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[0] + 0) / 2, 30)
                    mytext1.setScale(1.5)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(arr[i] * scale, 80))
                    scene.addRect(r, pen)

                    mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                    scene.addItem(mytext1)
                    mytext1.setPos(scale * (arr[i] + arr[i - 1]) / 2, 30)
                    mytext1.setScale(1.5)

                    mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                    scene.addItem(mytext2)
                    mytext2.setPos(arr[i] * scale, 85)
                    mytext2.setScale(1.3)

            hits = [Decimal('0.00')]
            for i in range(len(arr)):
                hits.append(arr[i])
            for i in range(len(processes)):
                p = processes[i]
                arrival = arrival_time[i]
                for j in range(len(arr2)):
                    if arr2[j] == p:
                        s += (hits[j] - arrival)
                        arrival = hits[j+1]

            self.lineEdit_12.setText('  ' + str("%.2f" % (s/n)) + ' ' + 'ms')

        except:
            QMessageBox.information(self, "Warning", "Nothing to simulate, Please enter valid information")



def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

