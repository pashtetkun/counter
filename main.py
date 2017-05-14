# coding=utf-8

from ui import main_window
import dbmanager.dbmanager as db


if __name__ == "__main__":
    db.initialize()
    main_window.MainWindow(1000, 500)