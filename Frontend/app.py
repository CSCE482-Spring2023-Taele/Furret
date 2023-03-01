import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Page')
        # self.setGeometry(200, 100, 400, 200)
        # self.showMaximized() # makes the window maximized

        # Create buttons to link to other pages
        self.settings_button = QPushButton('Settings', self)
        self.music_scanning_button = QPushButton('Music Scanning', self)
        self.music_learning_button = QPushButton('Music Learning & Accuracy', self)
        self.history_button = QPushButton('History', self)

        # Creating title of landing page
        title = QLabel('Welcome to Virtualoso', self)
        title.setAlignment(QtCore.Qt.AlignCenter)

        # Creating layout for title
        title_layout = QVBoxLayout()
        title_layout.addWidget(title)
        title_layout.setAlignment(QtCore.Qt.AlignTop)

        # Creating layout for buttons
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.settings_button)
        buttons_layout.addWidget(self.music_scanning_button)
        buttons_layout.addWidget(self.music_learning_button)
        buttons_layout.addWidget(self.history_button)

        # Adding the title layout and button layout to main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        # main_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

        # Connect button clicks to page changes
        self.settings_button.clicked.connect(self.open_settings_page)
        self.music_scanning_button.clicked.connect(self.open_music_scanning_page)
        self.music_learning_button.clicked.connect(self.open_music_learning_page)
        self.history_button.clicked.connect(self.open_history_page)

    def open_settings_page(self):
        # self.settings_page = SettingsPage()
        # self.settings_page.show()
        # self.hide()
        widget.setCurrentIndex(1)

    def open_music_scanning_page(self):
        # self.music_scanning_page = MusicScanningPage()
        # self.music_scanning_page.show()
        # self.hide()
        widget.setCurrentIndex(2)

    def open_music_learning_page(self):
        # self.music_learning_page = MusicLearningPage()
        # self.music_learning_page.show()
        # self.hide()
        widget.setCurrentIndex(3)

    def open_history_page(self):
        # self.history_page = HistoryPage()
        # self.history_page.show()
        # self.hide()
        widget.setCurrentIndex(4)


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Settings Page')
        # self.setGeometry(100, 100, 400, 200)

        # Add a label to the page
        label = QLabel('This is the settings page.', self)
        label.move(50, 50)

class MusicScanningPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Scanning Page')
        # self.setGeometry(100, 100, 400, 200)

        # Add a label to the page
        label = QLabel('This is the music scanning page.', self)
        label.move(50, 50)

class MusicLearningPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Learning & Accuracy Page')
        # self.setGeometry(100, 100, 400, 200)

        # Add a label to the page
        label = QLabel('This is the music learning & accuracy page.', self)
        label.move(50, 50)

class HistoryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('History Page')
        # self.setGeometry(100, 100, 400, 200)

        # Add a label to the page
        label = QLabel('This is the history page.', self)
        label.move(50, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main_page = MainPage()
    settings_page = SettingsPage()
    music_scanning_page = MusicScanningPage()
    music_learning_page = MusicLearningPage()
    history_page = HistoryPage()
    widget.addWidget(main_page)
    widget.addWidget(settings_page)
    widget.addWidget(music_scanning_page)
    widget.addWidget(music_learning_page)
    widget.addWidget(history_page)
    # main_page.show()
    widget.showMaximized()
    sys.exit(app.exec_())