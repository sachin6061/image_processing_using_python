import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dynaconf import settings as set


def header(frame, text, height, width=None):
    logo_wid = set.WID_PER * 12

    logo = QtWidgets.QLabel(frame)
    logo.setGeometry(QtCore.QRect(10, 3, logo_wid, height))

    if width is not None:
        label = QtWidgets.QLabel(text, frame)
        label.setGeometry(QtCore.QRect(1, 1, width, height))
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("background-color:#000000;color:rgb(255, 255, 255)")
        change_font_size(label, 16)
    else:
        label = QtWidgets.QLabel(text, frame)
        label.setGeometry(QtCore.QRect(logo_wid, 3, set.SCREEN_WIDTH - logo_wid * 2, height))
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color:rgb(255, 255, 255)")
        change_font_size(label, 16)


def screen_size(self):
    size = QtWidgets.QDesktopWidget().screenGeometry(-1)
    h = size.height()
    w = size.width()
    return w, h


def change_font_size(text, size=12):
    font = QtGui.QFont()
    font.setPointSize(size)
    text.setFont(font)


def add_btn(frame, x, y, text, width, height):
    btn = QtWidgets.QPushButton(text, frame)
    btn.setGeometry(QtCore.QRect(x, y, width, height))
    change_font_size(btn, 9)
    btn.setStyleSheet(set.BTN_BORDER)
    return btn


def add_messagebox(frame):
    msg_box = QMessageBox(frame)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg_box.hide()

    font = QtGui.QFont()
    font.setPointSize(15)
    msg_box.setFont(font)
    return msg_box


def add_lbl(frame, x, y, text, width=150, height=30):
    lbl = QtWidgets.QLabel(text, frame)
    lbl.setGeometry(QtCore.QRect(x, y, width, height))
    lbl.setStyleSheet(set.NONE_BORDER)
    change_font_size(lbl, 10)
    return lbl


def border_frame(parent, x, y, width, height):
    frame = QtWidgets.QFrame(parent)
    frame.setGeometry(QtCore.QRect(x, y, width, height))
    frame.setFrameShape(QtWidgets.QFrame.Box)
    frame.setStyleSheet(set.BLACK_BORDER)
    return frame


def black_frame(frame, x, y, width, height):
    frame = QtWidgets.QFrame(frame)
    frame.setGeometry(QtCore.QRect(x, y, width, height))
    frame.setStyleSheet("background-color:rgb(0, 0, 0)")
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    return frame


def add_textbox(frame, x, y, width=300, height=30):
    textbox = QtWidgets.QLineEdit(frame)
    textbox.setGeometry(QtCore.QRect(x, y, width, height))
    change_font_size(textbox, 10)
    textbox.setStyleSheet(set.BLACK_BORDER)
    return textbox


def add_label(frame, x, y, text, width, height=30):
    lbl = QtWidgets.QLabel(text, frame)
    lbl.setGeometry(QtCore.QRect(x, y, width, height))
    lbl.setAlignment(QtCore.Qt.AlignCenter)
    lbl.setStyleSheet(set.NONE_BORDER)
    # change_font_size(lbl, set.FONT_SIZE)
    return lbl


def add_btn_size(frame, text, x, y, width, height=50):
    btn = QtWidgets.QPushButton(text, frame)
    btn.setGeometry(QtCore.QRect(x, y, width, height))
    change_font_size(btn, 18)
    btn.setStyleSheet(set.BTN_BORDER)
    return btn


def add_listbox(frame, x, y, width=100, height=40):
    textbox = QtWidgets.QComboBox(frame)
    textbox.setGeometry(QtCore.QRect(x, y, width, height))
    # textbox.setStyleSheet(set.BLACK_BORDER)
    return textbox


def add_textarea(frame, x, y, width=300, height=50):
    textbox = QtWidgets.QPlainTextEdit(frame)
    textbox.setGeometry(QtCore.QRect(x, y, width, height))
    change_font_size(textbox, 10)
    textbox.setStyleSheet(set.BLACK_BORDER)
    return textbox


def _frame(parent, x, y, width, height):
    frame = QtWidgets.QFrame(parent)
    frame.setGeometry(QtCore.QRect(x, y, width, height))
    frame.setFrameShape(QtWidgets.QFrame.Box)
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setLineWidth(1)
    return frame


def frame_with(parent, x, y, width, height):
    frame = QtWidgets.QFrame(parent)
    frame.setGeometry(QtCore.QRect(x, y, width, height))
    frame.setFrameShape(QtWidgets.QFrame.Box)
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setLineWidth(1)
    return frame


def set_image(self, path, lbl):
    pixmap = QtGui.QPixmap()
    pixmap.load(path)
    pixmap = pixmap.scaledToWidth(self.hei_part * 5, QtCore.Qt.SmoothTransformation)
    pixmap = pixmap.scaledToHeight(self.hei_part * 9, QtCore.Qt.SmoothTransformation)
    lbl.setPixmap(pixmap)
