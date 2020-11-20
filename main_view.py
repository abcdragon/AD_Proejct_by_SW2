from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QListView   # widget class
from PyQt5.QtWidgets import QGridLayout   # layout class

from tab import Tab

from file_view import FileView
from online_view import OnlineView


class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stack = QStackedWidget()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        tab = Tab(self.change_view)
        layout.addWidget(tab, 0, 0)

        self.stack.addWidget(FileView())
        self.stack.addWidget(OnlineView())

        layout.addWidget(self.stack, 0, 1)
        self.setLayout(layout)

        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowTitle('Make Subtitle')
        self.setFixedSize(800, 400)

    def change_view(self, index):
        self.stack.setCurrentIndex(index)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_view = MainView()
    main_view.show()
    sys.exit(app.exec_())