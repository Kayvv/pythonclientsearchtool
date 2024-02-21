# This is a sample Python script.
import sys

from PySide6.QtWidgets import QApplication

from retrieveportaldatawidget import RetrievePortalDataWidget


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = RetrievePortalDataWidget()
    widget.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
