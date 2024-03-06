from PySide6 import QtGui, QtWidgets

from ui_retrieveportaldatawidget import Ui_RetrievePortalDataWidget

from sparc.client.services.pennsieve import PennsieveService
from sparc.client.zinchelper import ZincHelper


class RetrievePortalDataWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._model = None
        self._selection_model = None
        self._list_files = None
        self._ui = Ui_RetrievePortalDataWidget()
        self._ui.setupUi(self)

        self._pennsieve_service = PennsieveService(connect=False)
        self._zinc = ZincHelper()

        self._make_connections()
        self._update_ui()

    def _make_connections(self):
        self._ui.pushButtonSearch.clicked.connect(self._search_button_clicked)
        self._ui.pushButtonDownload.clicked.connect(self._download_button_clicked)
        self._ui.pushButtonExportVTK.clicked.connect(self._export_vtk_button_clicked)
        self._ui.pushButtonAnalyse.clicked.connect(self._analyse_button_clicked)

    def _update_ui(self):
        ready = len(self._selection_model.selectedRows()) > 0 if self._selection_model else False
        self._ui.pushButtonAnalyse.setEnabled(ready)
        self._ui.pushButtonDownload.setEnabled(ready)
        self._ui.pushButtonExportVTK.setEnabled(ready)

    def _set_table(self, file_list):
        self._model = QtGui.QStandardItemModel(4, 3)
        self._model.setHorizontalHeaderLabels(['Filename', 'Dataset ID', 'Dataset Version'])
        for row in range(len(file_list)):
            item = QtGui.QStandardItem("%s" % (file_list[row]["name"]))
            self._model.setItem(row, 0, item)
            item = QtGui.QStandardItem("%s" % (file_list[row]["datasetId"]))
            self._model.setItem(row, 1, item)
            item = QtGui.QStandardItem("%s" % (file_list[row]["datasetVersion"]))
            self._model.setItem(row, 2, item)

        self._ui.tableViewSearchResult.setModel(self._model)
        self._ui.tableViewSearchResult.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self._ui.tableViewSearchResult.horizontalHeader().setStretchLastSection(True)
        self._selection_model = self._ui.tableViewSearchResult.selectionModel()
        self._selection_model.selectionChanged.connect(self._update_ui)

    def _retrieve_data(self):
        # Get user’s input
        filename = self._ui.lineEditSearch.text()
        dataset_id = self._ui.lineEditDatasetID.text()
        # Use sparc.client to retrieve files
        self._list_files = self._pennsieve_service.list_files(
            limit=100,
            query=filename,
            dataset_id=dataset_id,
        )
        # Display the search result in a table view.
        self._set_table(self._list_files)

    def _search_button_clicked(self):
        self._retrieve_data()

    def _download_button_clicked(self):
        indexes = self._ui.tableViewSearchResult.selectionModel().selectedRows()
        for index in indexes:
            self._pennsieve_service.download_file(self._list_files[index.row()])

    def _export_vtk_button_clicked(self):
        indexes = self._ui.tableViewSearchResult.selectionModel().selectedRows()
        for index in indexes:
            self._zinc.get_mbf_vtk(self._list_files[index.row()]['datasetId'], self._list_files[index.row()]['name'])

    def _analyse_button_clicked(self):
        indexes = self._ui.tableViewSearchResult.selectionModel().selectedRows()
        for index in indexes:
            self._pennsieve_service.download_file(self._list_files[index.row()])
            try:
                organ = self._ui.comboBoxAnalyse.currentText()
                result = self._zinc.analyse(self._list_files[index.row()]['name'], organ)
            except ValueError:
                result = "Input file must be an MBF XML file"
                
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle("Analyse result")
            dlg.setText(result)
            dlg.exec_()
