import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from matplotlib import pyplot as plt
from windpowerlib import WindTurbine, ModelChain

class Ui_Form(object):

    # defining the global variables to make exportable
    dataframe = None
    input_temp_column = None
    input_temp_height = None
    input_pressure_column = None
    input_windspeed_column = None
    input_windspeed_height = None
    input_roughness_length = None
    input_start_date = None
    input_timezone = None
    input_turbine = None
    input_hub_height = None
    input_wind_speed_model = None
    input_density_model = None
    input_power_output_model = None
    input_density_correction = None
    input_obstacle_height = 0
    input_hellman_exp = 0
    input_hellman_z0 = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 634)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(500, 60, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 460, 901, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(30, 20, 941, 25))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_mc_parameters = QtWidgets.QLabel(Form)
        self.label_mc_parameters.setGeometry(QtCore.QRect(540, 70, 185, 18))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_mc_parameters.setFont(font)
        self.label_mc_parameters.setObjectName("label_mc_parameters")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 68, 441, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_weather = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_weather.setFont(font)
        self.label_weather.setObjectName("label_weather")
        self.horizontalLayout_15.addWidget(self.label_weather)
        self.pushButton_upload = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_upload.sizePolicy().hasHeightForWidth())
        self.pushButton_upload.setSizePolicy(sizePolicy)
        self.pushButton_upload.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setObjectName("pushButton_upload")

        # connection to pushbutton upload
        self.pushButton_upload.clicked.connect(self.upload_dataframe)

        self.horizontalLayout_15.addWidget(self.pushButton_upload)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_temp_col = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_temp_col.setFont(font)
        self.label_temp_col.setObjectName("label_temp_col")
        self.horizontalLayout_12.addWidget(self.label_temp_col)
        self.lineEdit_temp_col = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_temp_col.setFont(font)
        self.lineEdit_temp_col.setObjectName("lineEdit_temp_col")
        self.horizontalLayout_12.addWidget(self.lineEdit_temp_col)
        self.label_temp_height = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_temp_height.setFont(font)
        self.label_temp_height.setObjectName("label_temp_height")
        self.horizontalLayout_12.addWidget(self.label_temp_height)
        self.lineEdit_temp_height = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_temp_height.setFont(font)
        self.lineEdit_temp_height.setObjectName("lineEdit_temp_height")
        self.horizontalLayout_12.addWidget(self.lineEdit_temp_height)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_pressure_col = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_pressure_col.setFont(font)
        self.label_pressure_col.setObjectName("label_pressure_col")
        self.horizontalLayout_6.addWidget(self.label_pressure_col)
        self.lineEdit_pressure_col = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_pressure_col.sizePolicy().hasHeightForWidth())
        self.lineEdit_pressure_col.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_pressure_col.setFont(font)
        self.lineEdit_pressure_col.setObjectName("lineEdit_pressure_col")
        self.horizontalLayout_6.addWidget(self.lineEdit_pressure_col)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_windspeed_col = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_windspeed_col.setFont(font)
        self.label_windspeed_col.setObjectName("label_windspeed_col")
        self.horizontalLayout_5.addWidget(self.label_windspeed_col)
        self.lineEdit_windspeed_col = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_windspeed_col.setFont(font)
        self.lineEdit_windspeed_col.setObjectName("lineEdit_windspeed_col")
        self.horizontalLayout_5.addWidget(self.lineEdit_windspeed_col)
        self.label_windspeed_height = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_windspeed_height.setFont(font)
        self.label_windspeed_height.setObjectName("label_windspeed_height")
        self.horizontalLayout_5.addWidget(self.label_windspeed_height)
        self.lineEdit_windspeed_height = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_windspeed_height.setFont(font)
        self.lineEdit_windspeed_height.setObjectName("lineEdit_windspeed_height")
        self.horizontalLayout_5.addWidget(self.lineEdit_windspeed_height)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_surface_roughness = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_surface_roughness.setFont(font)
        self.label_surface_roughness.setObjectName("label_surface_roughness")
        self.horizontalLayout_4.addWidget(self.label_surface_roughness)
        self.lineEdit_roughness = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_roughness.sizePolicy().hasHeightForWidth())
        self.lineEdit_roughness.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_roughness.setFont(font)
        self.lineEdit_roughness.setObjectName("lineEdit_roughness")
        self.horizontalLayout_4.addWidget(self.lineEdit_roughness)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_startdate = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_startdate.setFont(font)
        self.label_startdate.setObjectName("label_startdate")
        self.horizontalLayout_2.addWidget(self.label_startdate)
        self.lineEdit_date = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_date.sizePolicy().hasHeightForWidth())
        self.lineEdit_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_date.setFont(font)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.horizontalLayout_2.addWidget(self.lineEdit_date)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_timezone = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_timezone.setFont(font)
        self.label_timezone.setObjectName("label_timezone")
        self.horizontalLayout_3.addWidget(self.label_timezone)
        self.lineEdit_timezone = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_timezone.sizePolicy().hasHeightForWidth())
        self.lineEdit_timezone.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_timezone.setFont(font)
        self.lineEdit_timezone.setObjectName("lineEdit_timezone")
        self.horizontalLayout_3.addWidget(self.lineEdit_timezone)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_turbine = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_turbine.setFont(font)
        self.label_turbine.setObjectName("label_turbine")
        self.horizontalLayout.addWidget(self.label_turbine)
        self.lineEdit_turbine = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_turbine.setFont(font)
        self.lineEdit_turbine.setObjectName("lineEdit_turbine")
        self.horizontalLayout.addWidget(self.lineEdit_turbine)
        self.label_hub = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_hub.setFont(font)
        self.label_hub.setObjectName("label_hub")
        self.horizontalLayout.addWidget(self.label_hub)
        self.lineEdit_hub = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_hub.setFont(font)
        self.lineEdit_hub.setObjectName("lineEdit_hub")
        self.horizontalLayout.addWidget(self.lineEdit_hub)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(540, 100, 379, 311))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_windspeed_model = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_windspeed_model.setFont(font)
        self.label_windspeed_model.setObjectName("label_windspeed_model")
        self.horizontalLayout_7.addWidget(self.label_windspeed_model)
        self.comboBox_windspeed_model = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_windspeed_model.setFont(font)
        self.comboBox_windspeed_model.setObjectName("comboBox_windspeed_model")
        self.comboBox_windspeed_model.addItem("")
        self.comboBox_windspeed_model.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_windspeed_model)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_density = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_density.setFont(font)
        self.label_density.setObjectName("label_density")
        self.horizontalLayout_8.addWidget(self.label_density)
        self.comboBox_density_model = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_density_model.setFont(font)
        self.comboBox_density_model.setObjectName("comboBox_density_model")
        self.comboBox_density_model.addItem("")
        self.comboBox_density_model.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_density_model)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_poweroutput_model = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_poweroutput_model.setFont(font)
        self.label_poweroutput_model.setObjectName("label_poweroutput_model")
        self.horizontalLayout_9.addWidget(self.label_poweroutput_model)
        self.comboBox_power_output_model = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_power_output_model.setFont(font)
        self.comboBox_power_output_model.setObjectName("comboBox_power_output_model")
        self.comboBox_power_output_model.addItem("")
        self.comboBox_power_output_model.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_power_output_model)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_density_correction = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_density_correction.setFont(font)
        self.label_density_correction.setObjectName("label_density_correction")
        self.horizontalLayout_10.addWidget(self.label_density_correction)
        self.comboBox_density_correction = QtWidgets.QComboBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_density_correction.sizePolicy().hasHeightForWidth())
        self.comboBox_density_correction.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_density_correction.setFont(font)
        self.comboBox_density_correction.setObjectName("comboBox_density_correction")
        self.comboBox_density_correction.addItem("")
        self.comboBox_density_correction.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_density_correction)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_obstacle = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_obstacle.setFont(font)
        self.label_obstacle.setObjectName("label_obstacle")
        self.horizontalLayout_11.addWidget(self.label_obstacle)
        self.lineEdit_obstacle = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_obstacle.setFont(font)
        self.lineEdit_obstacle.setObjectName("lineEdit_obstacle")
        self.horizontalLayout_11.addWidget(self.lineEdit_obstacle, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_hellman_exp = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_hellman_exp.setFont(font)
        self.label_hellman_exp.setObjectName("label_hellman_exp")
        self.horizontalLayout_13.addWidget(self.label_hellman_exp)
        self.lineEdit_hellman_exp = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_hellman_exp.setFont(font)
        self.lineEdit_hellman_exp.setObjectName("lineEdit_hellman_exp")
        self.horizontalLayout_13.addWidget(self.lineEdit_hellman_exp, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_hellman_z0 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_hellman_z0.setFont(font)
        self.label_hellman_z0.setObjectName("label_hellman_z0")
        self.horizontalLayout_14.addWidget(self.label_hellman_z0)
        self.lineEdit_hellman_z0 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_hellman_z0.setFont(font)
        self.lineEdit_hellman_z0.setObjectName("lineEdit_hellman_z0")
        self.horizontalLayout_14.addWidget(self.lineEdit_hellman_z0, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.label_hellman = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_hellman.setFont(font)
        self.label_hellman.setObjectName("label_hellman")
        self.verticalLayout.addWidget(self.label_hellman)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(340, 420, 331, 28))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_input = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_input.sizePolicy().hasHeightForWidth())
        self.pushButton_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_input.setFont(font)
        self.pushButton_input.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_input.setAutoFillBackground(False)
        self.pushButton_input.setAutoDefault(False)
        self.pushButton_input.setObjectName("pushButton_input")

        # connection to pushbutton_input
        self.pushButton_input.clicked.connect(self.temp_column)
        self.pushButton_input.clicked.connect(self.temp_height)
        self.pushButton_input.clicked.connect(self.pressure_column)
        self.pushButton_input.clicked.connect(self.windspeed_column)
        self.pushButton_input.clicked.connect(self.windspeed_height)
        self.pushButton_input.clicked.connect(self.roughness)
        self.pushButton_input.clicked.connect(self.start_date)
        self.pushButton_input.clicked.connect(self.timezone)
        self.pushButton_input.clicked.connect(self.turbine)
        self.pushButton_input.clicked.connect(self.hub_height)
        self.pushButton_input.clicked.connect(self.wind_speed_model)
        self.pushButton_input.clicked.connect(self.density_model)
        self.pushButton_input.clicked.connect(self.power_output_model)
        self.pushButton_input.clicked.connect(self.density_correction)
        self.pushButton_input.clicked.connect(self.obstacle)
        self.pushButton_input.clicked.connect(self.hellman_exp)
        self.pushButton_input.clicked.connect(self.hellman_z0)

        self.horizontalLayout_16.addWidget(self.pushButton_input)
        self.pushButton_simulate = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_simulate.sizePolicy().hasHeightForWidth())
        self.pushButton_simulate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_simulate.setFont(font)
        self.pushButton_simulate.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_simulate.setAutoFillBackground(False)
        self.pushButton_simulate.setAutoDefault(False)
        self.pushButton_simulate.setObjectName("pushButton_simulate")
        # connection to pushbutton simulate
        self.pushButton_simulate.clicked.connect(self.solve_mc)

        self.horizontalLayout_16.addWidget(self.pushButton_simulate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_19.setText(_translate("Form", "                                                                                  WindPowerLib                                                                                  "))
        self.label_mc_parameters.setText(_translate("Form", "ModelChain parameters:"))
        self.label_weather.setText(_translate("Form", "weather data file:"))
        self.pushButton_upload.setText(_translate("Form", "upload"))
        self.label_temp_col.setText(_translate("Form", "Temperature column:"))
        self.lineEdit_temp_col.setPlaceholderText(_translate("Form", "Ex: temperature"))
        self.label_temp_height.setText(_translate("Form", "Height:"))
        self.lineEdit_temp_height.setPlaceholderText(_translate("Form", "in m"))
        self.label_pressure_col.setText(_translate("Form", "Pressure column:"))
        self.lineEdit_pressure_col.setPlaceholderText(_translate("Form", "Ex: pressure"))
        self.label_windspeed_col.setText(_translate("Form", "Wind speed column:"))
        self.lineEdit_windspeed_col.setPlaceholderText(_translate("Form", "Ex: windspeed"))
        self.label_windspeed_height.setText(_translate("Form", "Height:"))
        self.lineEdit_windspeed_height.setPlaceholderText(_translate("Form", "in m"))
        self.label_surface_roughness.setText(_translate("Form", "Surface roughness length:"))
        self.lineEdit_roughness.setPlaceholderText(_translate("Form", "in m"))
        self.label_startdate.setText(_translate("Form", "Start date of data:"))
        self.lineEdit_date.setPlaceholderText(_translate("Form", "Ex: 2020-01-01"))
        self.label_timezone.setText(_translate("Form", "Time zone:"))
        self.lineEdit_timezone.setPlaceholderText(_translate("Form", "Ex: Europe/Berlin"))
        self.label_turbine.setText(_translate("Form", "Turbine type:"))
        self.lineEdit_turbine.setPlaceholderText(_translate("Form", "Ex: E-126/4200"))
        self.label_hub.setText(_translate("Form", "Hub height:"))
        self.lineEdit_hub.setPlaceholderText(_translate("Form", "in m"))
        self.label_windspeed_model.setText(_translate("Form", "Wind speed model:"))
        self.comboBox_windspeed_model.setItemText(0, _translate("Form", "logarithmic"))
        self.comboBox_windspeed_model.setItemText(1, _translate("Form", "hellman"))
        self.label_density.setText(_translate("Form", "Density model:"))
        self.comboBox_density_model.setItemText(0, _translate("Form", "barometric"))
        self.comboBox_density_model.setItemText(1, _translate("Form", "ideal gas"))
        self.label_poweroutput_model.setText(_translate("Form", "Power output model:"))
        self.comboBox_power_output_model.setItemText(0, _translate("Form", "power curve"))
        self.comboBox_power_output_model.setItemText(1, _translate("Form", "power coefficient curve"))
        self.label_density_correction.setText(_translate("Form", "Density correction:"))
        self.comboBox_density_correction.setItemText(0, _translate("Form", "False"))
        self.comboBox_density_correction.setItemText(1, _translate("Form", "True"))
        self.label_obstacle.setText(_translate("Form", "Obstacle Height:"))
        self.lineEdit_obstacle.setPlaceholderText(_translate("Form", "in m (default 0)"))
        self.label_hellman_exp.setText(_translate("Form", "Hellman exponent:"))
        self.lineEdit_hellman_exp.setPlaceholderText(_translate("Form", "default None"))
        self.label_hellman_z0.setText(_translate("Form", "Hellman z0:"))
        self.lineEdit_hellman_z0.setPlaceholderText(_translate("Form", "default None"))
        self.label_hellman.setText(_translate("Form", "Hellman exponent & Hellman z0 are only applicable \n"
"if wind speed model is Hellman"))
        self.pushButton_input.setText(_translate("Form", "Load Inputs"))
        self.pushButton_simulate.setText(_translate("Form", "Simulate"))


    # function for weather data
    def upload_dataframe(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)
        if file_name:
            # Read the CSV file into a DataFrame
            try:
                dataframe = pd.read_csv(file_name)
                self.dataframe = dataframe
                #print("weather data uploaded")
                self.plainTextEdit.appendPlainText("weather data uploaded")
                return dataframe
            except Exception as e:
                # self.result_text.setPlainText(f"Error loading DataFrame: {e}")
                #print("error uploading the selected file")
                self.plainTextEdit.appendPlainText("Error uploading the selected file")

    def temp_column(self):
        input_temp_column = self.lineEdit_temp_col.text()
        self.input_temp_column = input_temp_column
        #print(input_temp_column)
        self.plainTextEdit.appendPlainText(f"Temp column :{input_temp_column}")
        return input_temp_column

    def temp_height(self):
        input_temp_height = self.lineEdit_temp_height.text()
        try:
           self.input_temp_height = float(input_temp_height)
           #print(input_temp_height)
           self.plainTextEdit.appendPlainText(f"Temp measured height :{input_temp_height}")
           return input_temp_height
        except ValueError:
            #print("invalid value for height of temperature measured")
            self.plainTextEdit.appendPlainText("invalid value for height of temperature measured")

    def pressure_column(self):
        input_pressure_column = self.lineEdit_pressure_col.text()
        self.input_pressure_column = input_pressure_column
        #print(input_pressure_column)
        self.plainTextEdit.appendPlainText(f"Pressure column :{input_pressure_column}")
        return input_pressure_column

    def windspeed_column(self):
        input_windspeed_column = self.lineEdit_windspeed_col.text()
        self.input_windspeed_column = input_windspeed_column
        #print(input_windspeed_column)
        self.plainTextEdit.appendPlainText(f"Wind speed column :{input_windspeed_column}")
        return input_windspeed_column

    def windspeed_height(self):
        input_windspeed_height = self.lineEdit_windspeed_height.text()
        try:
           self.input_windspeed_height = float(input_windspeed_height)
           #print(input_windspeed_height)
           self.plainTextEdit.appendPlainText(f"Wind speed measured height :{input_windspeed_height}")
           return input_windspeed_height
        except ValueError:
            #print("invalid value for height of windspeed measured")
            self.plainTextEdit.appendPlainText("invalid value for height of windspeed measured")

    def roughness(self):
        input_roughness_length = self.lineEdit_roughness.text()
        try:
            self.input_roughness_length = float(input_roughness_length)
            #print(input_roughness_length)
            self.plainTextEdit.appendPlainText(f"Roughness length :{input_roughness_length}")
            return input_roughness_length
        except ValueError:
            #print("invalid value for Roughness length")
            self.plainTextEdit.appendPlainText("invalid value for Roughness length")

    def start_date(self):
        input_start_date = self.lineEdit_date.text()
        self.input_start_date = input_start_date
        #print(input_start_date)
        self.plainTextEdit.appendPlainText(f"Start date :{input_start_date}")
        return input_start_date

    def timezone(self):
        input_timezone = self.lineEdit_timezone.text()
        self.input_timezone = input_timezone
        #print(input_timezone)
        self.plainTextEdit.appendPlainText(f"Timeozne :{input_timezone}")
        return input_timezone

    def turbine(self):
        input_turbine = self.lineEdit_turbine.text()
        self.input_turbine = input_turbine
        #print(input_turbine)
        self.plainTextEdit.appendPlainText(f"Turbine :{input_turbine}")
        return input_turbine

    def hub_height(self):
        input_hub_height = self.lineEdit_hub.text()
        try:
            self.input_hub_height =float(input_hub_height)
            #print(input_hub_height)
            self.plainTextEdit.appendPlainText(f"Hub height :{input_hub_height}")
            return input_hub_height
        except ValueError:
            #print("invalid value for hub height")
            self.plainTextEdit.appendPlainText("invalid value for hub height")

    def wind_speed_model(self):
        input_wind_speed_model = self.comboBox_windspeed_model.currentText()
        self.input_wind_speed_model = input_wind_speed_model
        #print(input_wind_speed_model)
        self.plainTextEdit.appendPlainText(f"Wind speed model :{input_wind_speed_model}")
        return input_wind_speed_model

    def density_model(self):
        input_density_model = self.comboBox_density_model.currentText()
        if input_density_model == 'barometric':
            input_density_model = 'barometric'
        if input_density_model == 'ideal gas':
            input_density_model = 'ideal_gas'

        self.input_density_model = input_density_model
        #print(input_density_model)
        self.plainTextEdit.appendPlainText(f"Density model :{input_density_model}")
        return input_density_model

    def power_output_model(self):
        input_power_output_model = self.comboBox_power_output_model.currentText()

        if input_power_output_model == 'power curve':
            input_power_output_model = 'power_curve'
        if input_power_output_model == 'power coefficient curve':
            input_power_output_model = 'power_coefficient_curve'

        self.input_power_output_model = input_power_output_model
        #print(input_power_output_model)
        self.plainTextEdit.appendPlainText(f"Power output model :{input_power_output_model}")
        return input_power_output_model

    def density_correction(self):
        input_density_correction = self.comboBox_density_correction.currentText()
        if input_density_correction == 'False':
            input_density_correction = False
        if input_density_correction == 'True':
            input_density_correction = True

        self.input_density_correction = input_density_correction
        #print(input_density_correction)
        self.plainTextEdit.appendPlainText(f"Density correction :{input_density_correction}")
        return input_density_correction

    def obstacle(self):
        input_obstacle_height = self.lineEdit_obstacle.text()
        if input_obstacle_height:
            self.input_obstacle_height = float(input_obstacle_height)
            #print(input_obstacle_height)
            self.plainTextEdit.appendPlainText(f"Obstacle height :{input_obstacle_height}")
            return input_obstacle_height
        else:
            input_obstacle_height = 0
            #print(input_obstacle_height)
            return input_obstacle_height
    def hellman_exp(self):
        input_hellman_exp = self.lineEdit_hellman_exp.text()
        if input_hellman_exp:
            self.input_hellman_exp = float(input_hellman_exp)
            #print(input_hellman_exp)
            self.plainTextEdit.appendPlainText(f"Hellman exponent :{input_hellman_exp}")
            return input_hellman_exp
        else:
            input_hellman_exp = None
            #print(input_hellman_exp)
            return input_hellman_exp

    def hellman_z0(self):
        input_hellman_z0 = self.lineEdit_hellman_z0.text()
        if input_hellman_z0:
            self.input_hellman_z0 = float(input_hellman_z0)
            #print(input_hellman_z0)
            self.plainTextEdit.appendPlainText(f"Hellman Z0 :{input_hellman_z0}")
            return input_hellman_z0
        else:
            input_hellman_z0 = None
            #print(input_hellman_z0)
            return input_hellman_z0

    def solve_mc(self):

        weather_data = self.dataframe
        temp_column = self.input_temp_column
        temp_height = self.input_temp_height
        pressure_column = self.input_pressure_column
        windspeed_column = self.input_windspeed_column
        windspeed_height = self.input_windspeed_height
        roughness_length = self.input_roughness_length
        start_date = self.input_start_date
        timezone = self.input_timezone
        turbine = self.input_turbine
        hub_height = self.input_hub_height
        wind_speed_model = self.input_wind_speed_model
        density_model = self.input_density_model
        power_output_model = self.input_power_output_model
        density_correction = self.input_density_correction
        obstacle_height = self.input_obstacle_height
        hellman_exp = self.input_hellman_exp
        hellman_z0 = self.input_hellman_z0

        required_columns = [temp_column, pressure_column, windspeed_column]
        new_weather = weather_data[required_columns]

        # converting temp from C to K
        new_weather = new_weather.copy()
        new_weather.loc[:, 'temperature'] = new_weather[temp_column] + 273.15
        new_weather.drop(columns=[temp_column], inplace=True)

        # converting pressure from hPa to Pa
        new_weather.loc[:, 'pressure'] = new_weather[pressure_column] * 100
        new_weather.drop(columns=[pressure_column], inplace=True)

        # adding surface roughness length as an additional column
        new_weather['roughness_length'] = roughness_length  # surface roughness value in m

        new_weather.rename(columns={windspeed_column: 'wind_speed'}, inplace=True)

        # assigning height in m for data in the second row
        heights = [windspeed_height, temp_height, 0, 0]
        new_weather.columns = pd.MultiIndex.from_arrays([new_weather.columns, heights])

        # indexing with date and timezone
        new_weather.index = pd.date_range(start=start_date, periods=8760, freq='H', tz=timezone)

        # wind Turbine Data
        def initialize_wind_turbine():
            turbine_name = {
                "turbine_type": turbine,
                "hub_height": hub_height,
            }
            turbine_id = WindTurbine(**turbine_name)

            return turbine_id

        # calculating power
        def calculate_power_output(weather, turbine_id):
            modelchain_data = {"wind_speed_model": wind_speed_model,
                               "density_model": density_model,
                               "temperature_model": "linear_gradient",
                               "power_output_model": power_output_model,
                               "density_correction": density_correction,
                               "obstacle_height": obstacle_height,
                               "hellman_exp": hellman_exp,
                               "hellman_z0": hellman_z0,
                               }

            mc_turbine_id = ModelChain(turbine_id, **modelchain_data).run_model(weather)

            turbine_id.power_output = mc_turbine_id.power_output  # power output in watts
            turbine_id.power_output_KW = (turbine_id.power_output) / 1000
            turbine_id.scaled_data = (turbine_id.power_output_KW) / (turbine_id.power_output_KW.max())
            return

        # plotting the results
        def plot_or_print(turbine_id):
            if plt:
                turbine_id.scaled_data.plot(legend=True, label=turbine)
                plt.xlabel("Time")
                plt.ylabel("Normalised power")
                plt.show()
                #print(turbine_id.power_output_KW)
                #print(turbine_id.power_output_KW.sum())
                self.plainTextEdit.setPlainText(f"Annual power output :{turbine_id.power_output_KW.sum()}")
                self.plainTextEdit.appendPlainText(f"Annual power peak :{turbine_id.power_output_KW.max()}")

            else:
               pass


        def export(turbine_id):
            file_path = "normalised_wind_output.csv"
            turbine_id.scaled_data.to_csv(file_path, index=True)
            #print("turbine output is saved to current directory")
            self.plainTextEdit.appendPlainText("Turbine output is saved to current directory")

        def run():
            weather = new_weather
            turbine_id = initialize_wind_turbine()
            calculate_power_output(weather, turbine_id)
            plot_or_print(turbine_id)
            export(turbine_id)

        if __name__ == "__main__":
            run()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
