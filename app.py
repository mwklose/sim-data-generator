import sys
from PyQt5.QtWidgets import QApplication
from src.gui import GraphApp


# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = GraphApp()
    main_window.show()
    sys.exit(app.exec_())
