# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retrieveportaldatawidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_RetrievePortalDataWidget(object):
    def setupUi(self, RetrievePortalDataWidget):
        if not RetrievePortalDataWidget.objectName():
            RetrievePortalDataWidget.setObjectName(u"RetrievePortalDataWidget")
        RetrievePortalDataWidget.resize(714, 584)
        self.gridLayout = QGridLayout(RetrievePortalDataWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.subgridLayout = QGridLayout()
        self.subgridLayout.setObjectName(u"subgridLayout")
        self.manifestGroupBox = QGroupBox(RetrievePortalDataWidget)
        self.manifestGroupBox.setObjectName(u"manifestGroupBox")
        self.manifestFormLayout = QFormLayout(self.manifestGroupBox)
        self.manifestFormLayout.setObjectName(u"manifestFormLayout")
        self.labelSearch = QLabel(self.manifestGroupBox)
        self.labelSearch.setObjectName(u"labelSearch")

        self.manifestFormLayout.setWidget(0, QFormLayout.LabelRole, self.labelSearch)

        self.lineEditSearch = QLineEdit(self.manifestGroupBox)
        self.lineEditSearch.setObjectName(u"lineEditSearch")

        self.manifestFormLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditSearch)

        self.labelDatasetID = QLabel(self.manifestGroupBox)
        self.labelDatasetID.setObjectName(u"labelDatasetID")

        self.manifestFormLayout.setWidget(1, QFormLayout.LabelRole, self.labelDatasetID)

        self.lineEditDatasetID = QLineEdit(self.manifestGroupBox)
        self.lineEditDatasetID.setObjectName(u"lineEditDatasetID")

        self.manifestFormLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditDatasetID)

        self.pushButtonSearch = QPushButton(self.manifestGroupBox)
        self.pushButtonSearch.setObjectName(u"pushButtonSearch")

        self.manifestFormLayout.setWidget(2, QFormLayout.FieldRole, self.pushButtonSearch)


        self.subgridLayout.addWidget(self.manifestGroupBox, 0, 0, 1, 1)

        self.tableViewSearchResult = QTableView(RetrievePortalDataWidget)
        self.tableViewSearchResult.setObjectName(u"tableViewSearchResult")

        self.subgridLayout.addWidget(self.tableViewSearchResult, 1, 0, 1, 1)

        self.pushButtonDownload = QPushButton(RetrievePortalDataWidget)
        self.pushButtonDownload.setObjectName(u"pushButtonDownload")

        self.subgridLayout.addWidget(self.pushButtonDownload, 2, 0, 1, 1)

        self.pushButtonExportVTK = QPushButton(RetrievePortalDataWidget)
        self.pushButtonExportVTK.setObjectName(u"pushButtonExportVTK")

        self.subgridLayout.addWidget(self.pushButtonExportVTK, 3, 0, 1, 1)

        self.pushButtonAnalyse = QPushButton(RetrievePortalDataWidget)
        self.pushButtonAnalyse.setObjectName(u"pushButtonAnalyse")

        self.subgridLayout.addWidget(self.pushButtonAnalyse, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.subgridLayout, 0, 0, 1, 1)


        self.retranslateUi(RetrievePortalDataWidget)

        QMetaObject.connectSlotsByName(RetrievePortalDataWidget)
    # setupUi

    def retranslateUi(self, RetrievePortalDataWidget):
        RetrievePortalDataWidget.setWindowTitle(QCoreApplication.translate("RetrievePortalDataWidget", u"Search tool", None))
        self.labelSearch.setText(QCoreApplication.translate("RetrievePortalDataWidget", u"Search file:  ", None))
        self.labelDatasetID.setText(QCoreApplication.translate("RetrievePortalDataWidget", u"Dataset ID:  ", None))
        self.pushButtonSearch.setText(QCoreApplication.translate("RetrievePortalDataWidget", u"Search", None))
        self.pushButtonDownload.setText(QCoreApplication.translate("RetrievePortalDataWidget", u"Download", None))
        self.pushButtonExportVTK.setText(QCoreApplication.translate("RetrievePortalDataWidget", u"Export VTK", None))
        self.pushButtonAnalyse.setText(QCoreApplication.translate("RetrievePortalDataWidget", u"Analyse", None))
    # retranslateUi

