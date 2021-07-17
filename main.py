import sys
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QFileDialog
import components
from image_processing import image_processing_functions
from dynaconf import settings as set



class dashboard_win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.tbl_data = []
        components.change_font_size(self, 16)
        size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.resize(size.width(), size.height())
        self.hei_part = size.height() // 20
        self.width = size.width()
        self.height = size.height()
        self.wid_part = self.width // 20

        self.header_frame = components.black_frame(self, 0, 0, self.width, self.hei_part)
        self.header = components.header(self.header_frame, "Image Restoration", self.hei_part)

        self.main_frame = components.frame_with(self, 10, self.hei_part + 10, self.width - 30,
                                                self.height - self.hei_part * 3)
        self.main_frame_design()
        self.hide_main()
        self.sub_frame = components.frame_with(self, 55, self.hei_part + 80, self.width - 150,
                                               self.height - self.hei_part * 6)
        self.lbl = components.add_lbl(self.sub_frame, self.wid_part * 5, self.hei_part * 5,
                                      "Please drop your image here!",
                                      width=500, height=40)
        components.change_font_size(self.lbl, 18)

        self.file_name = components.add_lbl(self.sub_frame, self.wid_part * 7, self.hei_part * 7, "",
                                            width=500, height=40)
        components.change_font_size(self.file_name, 16)

        self.select_btn = components.add_btn(self.sub_frame, self.wid_part * 10, self.hei_part * 5, "select File", 150,
                                             40)
        self.select_btn.clicked.connect(self.openFileNameExplorer)
        self.process_btn = components.add_btn(self.sub_frame, self.wid_part * 12, self.hei_part * 5, "Process Image",
                                              150, 40)
        self.process_btn.clicked.connect(self.show_main)

        # self.hide_sub()
        self.process_btn.hide()
        self.showNormal()

    def hide_main(self):
        self.main_frame.hide()

    def show_main(self):
        self.hide_sub()
        self.main_frame.show()

    def show_sub(self):
        self.sub_frame.show()

    def hide_sub(self):
        self.sub_frame.hide()

    def openFileNameExplorer(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Please select image file", "",
                                                  "Image Files (*.jpg)", options=options)
        if fileName:
            self.file_name.setText(str(self.fileName))
            components.set_image(self, str(self.file_name.text()), self.ori_image)
            self.process_btn.show()

    def main_frame_design(self):
        self.l_frame = components.frame_with(self.main_frame, 0, 0, 600,
                                             self.height - self.hei_part * 3)

        self.lbl = components.add_lbl(self.l_frame, 150, 20, "Please Select your operation",
                                      width=400, height=40)
        components.change_font_size(self.lbl, 16)
        self.lst_box = components.add_listbox(self.l_frame, 100, 80, width=400)
        components.change_font_size(self.lst_box, 14)
        self.lst_box.addItem("Colorization")
        self.lst_box.addItem("Denoising")
        self.lst_box.addItem("Super Resolution")
        self.lst_box.addItem("Image in painting")
        self.lst_box.addItem("all")
        self.lst_box.activated.connect(self.process_image)
        self.ori_image = components.add_lbl(self.main_frame, 650, 150, " ",
                                            self.hei_part * 9, self.hei_part * 9)

        self.ori_image_lbl = components.add_lbl(self.main_frame, 750, 650, "Input / Original Image",
                                                self.hei_part * 6, self.hei_part * 2)
        components.change_font_size(self.ori_image_lbl, 18)

        self.res_image = components.add_lbl(self.main_frame, 1350, 150, " ",
                                            self.hei_part * 9, self.hei_part * 9)
        # components.set_image(self, "C:/Users/Admin/Pictures/a.jpg", self.res_image)

        self.res_image_lbl = components.add_lbl(self.main_frame, 1050, 650, "Output / Processed Image",
                                                self.hei_part * 6, self.hei_part * 2)
        components.change_font_size(self.res_image_lbl, 18)

    def process_image(self):
        img_process = image_processing_functions()
        img_process.convert_img(self.fileName)
        image = img_process.convert_img(self.fileName)
        if self.lst_box.currentText() == "Colorization":
            img_process.colorization(image)
        elif self.lst_box.currentText() == "Denoising":
            img_process.denoising(image)
        elif self.lst_box.currentText() == "Super Resolution":
            img_process.pixalate_image(image)
        elif self.lst_box.currentText() == "Image in painting":
            img_process.inpainting(image)
        elif self.lst_box.currentText() == "all":
            img_process.colorization(image)

        self.res_image.components.set_image(self, "output.png", self.res_image)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = dashboard_win()
    sys.exit(app.exec_())
