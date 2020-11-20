from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout


class FileView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.addWidget(QLabel('이건 파일 뷰 입니다'))

        self.setLayout(layout)
