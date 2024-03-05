# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retrieveportaldatawidget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_RetrievePortalDataWidget(object):
    def setupUi(self, RetrievePortalDataWidget):
        if not RetrievePortalDataWidget.objectName():
            RetrievePortalDataWidget.setObjectName(u"RetrievePortalDataWidget")
        RetrievePortalDataWidget.resize(714, 584)
        self.verticalLayout = QVBoxLayout(RetrievePortalDataWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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


        self.verticalLayout.addWidget(self.manifestGroupBox)

        self.tableViewSearchResult = QTableView(RetrievePortalDataWidget)
        self.tableViewSearchResult.setObjectName(u"tableViewSearchResult")

        self.verticalLayout.addWidget(self.tableViewSearchResult)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.pushButtonDownload = QPushButton(RetrievePortalDataWidget)
        self.pushButtonDownload.setObjectName(u"pushButtonDownload")

        self.horizontalLayout.addWidget(self.pushButtonDownload)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonExportVTK = QPushButton(RetrievePortalDataWidget)
        self.pushButtonExportVTK.setObjectName(u"pushButtonExportVTK")

        self.horizontalLayout.addWidget(self.pushButtonExportVTK)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButtonAnalyse = QPushButton(RetrievePortalDataWidget)
        self.pushButtonAnalyse.setObjectName(u"pushButtonAnalyse")

        self.horizontalLayout.addWidget(self.pushButtonAnalyse)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


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

