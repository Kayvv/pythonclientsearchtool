import sys

from PySide6.QtWidgets import QApplication

from retrieveportaldatawidget import RetrievePortalDataWidget


def main():
    app = QApplication(sys.argv)
    widget = RetrievePortalDataWidget()
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
