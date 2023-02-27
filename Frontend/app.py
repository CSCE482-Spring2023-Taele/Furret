import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Page')
        self.setGeometry(100, 100, 400, 200)

        # Create buttons to link to other pages
        self.settings_button = QPushButton('Settings', self)
        self.music_scanning_button = QPushButton('Music Scanning', self)
        self.music_learning_button = QPushButton('Music Learning & Accuracy', self)
        self.history_button = QPushButton('History', self)

        # Add buttons to a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.settings_button)
        layout.addWidget(self.music_scanning_button)
        layout.addWidget(self.music_learning_button)
        layout.addWidget(self.history_button)
        self.setLayout(layout)

        # Connect button clicks to page changes
        self.settings_button.clicked.connect(self.open_settings_page)
        self.music_scanning_button.clicked.connect(self.open_music_scanning_page)
        self.music_learning_button.clicked.connect(self.open_music_learning_page)
        self.history_button.clicked.connect(self.open_history_page)

    def open_settings_page(self):
        self.settings_page = SettingsPage()
        self.settings_page.show()
        self.hide()

    def open_music_scanning_page(self):
        self.music_scanning_page = MusicScanningPage()
        self.music_scanning_page.show()
        self.hide()

    def open_music_learning_page(self):
        self.music_learning_page = MusicLearningPage()
        self.music_learning_page.show()
        self.hide()

    def open_history_page(self):
        self.history_page = HistoryPage()
        self.history_page.show()
        self.hide()


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Settings Page')
        self.setGeometry(100, 100, 400, 200)

        # Add a label to the page
        label = QLabel('This is the settings page.', self)
        label.move(50, 50)

class MusicScanningPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Scanning Page')
        self.setGeometry(100, 100, 400, 200)

        # Add a label to the page
        label = QLabel('This is the music scanning page.', self)
        label.move(50, 50)

class MusicLearningPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Learning & Accuracy Page')
        self.setGeometry(100, 100, 400, 200)

        # Add a label to the page
        label = QLabel('This is the music learning & accuracy page.', self)
        label.move(50, 50)

class HistoryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('History Page')
        self.setGeometry(100, 100, 400, 200)

        # Add a label to the page
        label = QLabel('This is the history page.', self)
        label.move(50, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = MainPage()
    main_page.show()
    sys.exit(app.exec_())