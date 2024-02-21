from PySide6 import QtGui, QtWidgets

from ui_retrieveportaldatawidget import Ui_RetrievePortalDataWidget

from sparc.client.services.pennsieve import PennsieveService
from sparc.client.zinchelper import ZincHelper

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class RetrievePortalDataWidget(QtWidgets.QWidget):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._ui = Ui_RetrievePortalDataWidget()
        self._ui.setupUi(self)

        self._pennsieveService = PennsieveService(connect=False)
        self._zinc = ZincHelper()

        self._makeConnections()

    def _makeConnections(self):
        self._ui.pushButtonSearch.clicked.connect(self._searchButtonClicked)
        self._ui.pushButtonDownload.clicked.connect(self._downloadButtonClicked)
        self._ui.pushButtonExportVTK.clicked.connect(self._exportVTKButtonClicked)
        self._ui.pushButtonAnalyse.clicked.connect(self._analyseButtonClicked)

    def set_table(self, file_list):
        self.model = QtGui.QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['Filename', 'Dataset ID', 'Dataset Version'])
        for row in range(0, len(file_list)):
            item = QtGui.QStandardItem("%s" % (file_list[row]["name"]))
            self.model.setItem(row, 0, item)
            item = QtGui.QStandardItem("%s" % (file_list[row]["datasetId"]))
            self.model.setItem(row, 1, item)
            item = QtGui.QStandardItem("%s" % (file_list[row]["datasetVersion"]))
            self.model.setItem(row, 2, item)

        self._ui.tableViewSearchResult.setModel(self.model)
        self._ui.tableViewSearchResult.horizontalHeader().setStretchLastSection(True)
        self._ui.tableViewSearchResult.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def retrieve_data(self):
        # Get user’s input
        filename = self._ui.lineEditSearch.text()
        dataset_id = self._ui.lineEditDatasetID.text()
        # Use sparc.client to retrieve files
        self._list_files = self._pennsieveService.list_files(
            limit=100,
            query=filename,
            dataset_id=dataset_id,
        )
        print(self._list_files)
        # Display the search result in a table view.
        self.set_table(self._list_files)

    def _searchButtonClicked(self):
        self.retrieve_data()

    def _downloadButtonClicked(self):
        indexes = self._ui.tableViewSearchResult.selectionModel().selectedRows()
        for index in indexes:
            print('Row %d is selected' % index.row())
            self._pennsieveService.download_file(self._list_files[index.row()])

    def _exportVTKButtonClicked(self):
        indexes = self._ui.tableViewSearchResult.selectionModel().selectedRows()
        for index in indexes:
            self._zinc.get_mbf_vtk(self._list_files[index.row()]['datasetId'], self._list_files[index.row()]['name'])

    def _analyseButtonClicked(self):
        indexes = self._ui.tableViewSearchResult.selectionModel().selectedRows()
        for index in indexes:
            self._pennsieveService.download_file(self._list_files[index.row()])
            try:
                result = self._zinc.analyse(self._list_files[index.row()]['name'], "stomach")
            except ValueError:
                result = "Input file must be an MBF XML file"
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle("Analyse result")
            dlg.setText(result)
            dlg.exec_()
