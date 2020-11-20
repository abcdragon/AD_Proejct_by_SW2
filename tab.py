from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QIcon


class IconLabel(QWidget):
    clicked = pyqtSignal()

    def __init__(self, icon_path, name):
        super().__init__()
        self.init_ui(icon_path, name)

    def init_ui(self, pixel_map, name):
        layout = QHBoxLayout()

        icon = QLabel()
        icon.setPixmap(QIcon(pixel_map).pixmap(QSize(32, 32)))
        layout.addWidget(icon)
        layout.addWidget(QLabel(name))

        self.setLayout(layout)
        self.setAutoFillBackground(True)

        self.setContentsMargins(0, 0, 0, 0)

    def change_color(self, target_widget, color):
        pal = target_widget.palette()
        pal.setColor(target_widget.backgroundRole(), color)
        self.setPalette(pal)

    def enterEvent(self, event):
        self.change_color(self, Qt.lightGray)
        # print('Enter') # Debug

    def leaveEvent(self, event):
        self.change_color(self, Qt.transparent)
        # print('Leave') # Debug

    def mousePressEvent(self, event):
        self.clicked.emit()


class Tab(QWidget):
    def __init__(self, click_func):
        super().__init__()

        self.file = IconLabel('./icon/file_icon.png', '파일')
        self.file.clicked.connect(lambda: click_func(0))

        self.online = IconLabel('./icon/online_icon.png', '온라인')
        self.online.clicked.connect(lambda: click_func(1))

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.file)
        layout.addWidget(self.online)
        layout.addStretch(1)
        self.setLayout(layout)


# test code
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    tab = Tab(lambda x: print(x))
    tab.show()
    sys.exit(app.exec_())

