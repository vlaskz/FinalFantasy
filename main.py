import sys
import os
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QWidget

import mainlib as m


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Photon by Eletron"
        self.left = 10
        self.top = 10
        self.width = 1024
        self.height = 768
        self.initUI()
        sys.exit()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        path = self.openFileNameDialog()
        path = os.path.normpath(path)
        im2 = m.openImage(path, False)
        im2 = m.get_concat_tile_repeat(im2, 4, 2)
        im2.show()
        im2.save(self.saveFileDialog())



    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Selecione arquivo para conversão",
                                                  "",
                                                  "Arquivos de Imagem(*.bmp | *.png);;Qualquer formato (*)",
                                                  options=options)
        if filename:
            return filename

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filenames, _ = QFileDialog.getOpenFileNames(self,
                                                    "QFileDialog.getOpenFileNames()",
                                                    "",
                                                    "All Files(*);;PDF Files (*.py)",
                                                    options=options)
        if filenames:
            return filenames

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self,
                                                  "Salvar como",
                                                  "",
                                                  "PDF(*.pdf)",
                                                  options=options)
        if '.' not in filename:
            return filename+'.pdf'
        else:
            return filename


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
