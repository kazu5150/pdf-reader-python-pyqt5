import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtCore import Qt
from pdfminer.high_level import extract_text

class PdfDropper(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setText("ここにPDFファイルをドラッグ＆ドロップしてください。")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith('.pdf'):
                self.read_pdf(file_path)

    def read_pdf(self, file_path):
        try:
            text = extract_text(file_path)
            self.setText(text)
        except:
            self.setText("読み取れませんでした。")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pdf_dropper = PdfDropper()
    pdf_dropper.show()
    sys.exit(app.exec_())
