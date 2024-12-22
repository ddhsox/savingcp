# -*- coding: utf-8 -*-

import sys
import configparser
import os
import pyperclip
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QVBoxLayout, QWidget, QPushButton, QLabel, QGridLayout, QLineEdit, QMenu, QAction, QFileDialog, QMenuBar
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import colorsys
import xml.etree.ElementTree as ET
import resources_rc
from parametrs import MAX_COLORS
from function_transmute import *
from save_load import *
from data.license import ru_en
from styles.styles_main import *
from PyQt5.QtWidgets import (
    QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QDialog, QHBoxLayout, QWidget
)

class LicenseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("License Agreement")
        self.setGeometry(200, 200, 800, 600)

        # Флаг для отслеживания состояния соглашения
        self.license_accepted = False

        # Основной виджет
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Тексты лицензионного соглашения
        self.license_texts = ru_en
        self.current_language = "ru"  # Язык по умолчанию

        # Создаем текстовое поле с соглашением
        self.license_text = QTextEdit(self)
        self.license_text.setReadOnly(True)
        self.license_text.setText(self.license_texts[self.current_language])

        # Кнопки
        self.accept_button = QPushButton("Принять" if self.current_language == "ru" else "Accept")
        self.decline_button = QPushButton("Отклонить" if self.current_language == "ru" else "Decline")
        self.language_button = QPushButton("English" if self.current_language == "ru" else "Русский")

        # Подключение кнопок
        self.accept_button.clicked.connect(self.accept_license)
        self.decline_button.clicked.connect(self.decline_license)
        self.language_button.clicked.connect(self.switch_language)

        # Компоновка
        layout = QVBoxLayout()
        layout.addWidget(self.license_text)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.language_button)
        button_layout.addStretch(1)
        button_layout.addWidget(self.accept_button)
        button_layout.addWidget(self.decline_button)

        layout.addLayout(button_layout)
        self.central_widget.setLayout(layout)

        # Применяем стили
        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet(apply_styles_setStyleSheet)

    def accept_license(self):
        self.license_accepted = True  # Устанавливаем флаг
        self.close()  # Закрываем окно соглашения

    def decline_license(self):
        self.license_accepted = False  # Флаг для отказа
        self.close()  # Закрываем окно соглашения

    def switch_language(self):
        # Переключение между языками
        if self.current_language == "ru":
            self.current_language = "en"
        else:
            self.current_language = "ru"

        # Обновляем текст соглашения и кнопок
        self.license_text.setText(self.license_texts[self.current_language])
        self.accept_button.setText("Принять" if self.current_language == "ru" else "Accept")
        self.decline_button.setText("Отклонить" if self.current_language == "ru" else "Decline")
        self.language_button.setText("English" if self.current_language == "ru" else "Русский")


class ColorPaletteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Saving-CP")

        self.setWindowIcon(QIcon(":multi.ico"))
        self.setGeometry(100, 100, 800, 600)

        try:
            self.palette = load_palette_from_xml()
        except ValueError as e:
            QMessageBox.warning(self, "Load Error", str(e))
            self.palette = []

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout(self.central_widget)

        # Панель с цветами
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.refresh_palette()

        # Добавление кнопки для добавления цвета
        self.add_color_button = QPushButton("Add Color", self)
        self.add_color_button.clicked.connect(self.add_color_dialog)
        self.add_color_button.setStyleSheet(self.button_style())
        self.layout.addWidget(self.add_color_button)

        # Добавляем меню
        self.create_menus()
        self.apply_styles()

    def create_menus(self):
        menu_bar = self.menuBar()

        # Меню "Файл"
        file_menu = menu_bar.addMenu("File")

        # Кнопки для загрузки и сохранения
        load_action = QAction("Load Palette", self)
        load_action.triggered.connect(self.load_palette_dialog)
        file_menu.addAction(load_action)

        save_action = QAction("Save Palette", self)
        save_action.triggered.connect(self.save_palette_dialog)
        file_menu.addAction(save_action)

        # Кнопка для очистки палитры
        clear_action = QAction("Clear All", self)
        clear_action.triggered.connect(self.clear_palette_with_confirmation)
        file_menu.addAction(clear_action)

    def clear_palette_with_confirmation(self):
        # Создаем окно подтверждения
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Confirm Clear All")
        msg_box.setText("Are you sure you want to clear all colors from the palette?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        # Применяем стиль
        msg_box.setStyleSheet(clear_palette_setStyleSheet)

        # Показываем окно и получаем ответ
        reply = msg_box.exec_()

        if reply == QMessageBox.Yes:
            self.palette.clear()  # Очищаем палитру
            self.refresh_palette()  # Обновляем интерфейс
            save_palette_to_xml(self.palette)  # Сохраняем пустую палитру

    def refresh_palette(self):
        # Очищаем старые цвета
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Добавляем новые цвета
        for i, color in enumerate(self.palette):
            label = QLabel(self)
            label.setStyleSheet(f"""background-color: {color};
                border: 2px solid #fff;
                width: 60px;
                height: 60px;""")
            label.setAlignment(Qt.AlignCenter)
            label.mousePressEvent = lambda event, idx=i: self.handle_color_click(event, idx)  # Изменили событие
            label.setContextMenuPolicy(Qt.CustomContextMenu)
            label.customContextMenuRequested.connect(lambda event, idx=i: self.show_context_menu(event, idx))
            self.grid_layout.addWidget(label, i // 5, i % 5)

    def handle_color_click(self, event, idx):
        # Проверяем, была ли нажата правая кнопка мыши
        if event.button() == Qt.RightButton:
            return  # Если правая кнопка, не открываем окно редактирования
        # Если левая кнопка мыши, открываем окно редактирования
        self.edit_color(idx)

    def edit_color(self, idx):
        color = self.palette[idx]
        hex_color, rgb_color, hsl_color = convert_color(color)

        # Окно редактирования
        self.edit_window = QWidget()
        self.edit_window.setWindowTitle(f"Editing Color {idx + 1}")
        self.edit_window.setGeometry(300, 300, 300, 250)

        # Настройка стиля всплывающего окна
        self.edit_window.setStyleSheet(edit_color_setStyleSheet)

        layout = QVBoxLayout(self.edit_window)

        current_color_display = QLabel()
        current_color_display.setStyleSheet(f"background-color: {hex_color}; font-size: 12px; color: #fff; width: 40px; height: 40px; border: 2px solid #fff;")
        layout.addWidget(current_color_display)

        # HEX
        self.hex_edit = QLineEdit(hex_color, self)
        layout.addWidget(QLabel("HEX:"))
        layout.addWidget(self.hex_edit)

        # RGB
        rgb_str = f"RGB: {rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]}"
        self.rgb_edit = QLineEdit(rgb_str, self)
        layout.addWidget(QLabel("RGB:"))
        layout.addWidget(self.rgb_edit)

        # HSL
        hsl_str = f"HSL: {round(hsl_color[0] * 360)}, {round(hsl_color[1] * 100)}%, {round(hsl_color[2] * 100)}%"
        self.hsl_edit = QLineEdit(hsl_str, self)
        layout.addWidget(QLabel("HSL:"))
        layout.addWidget(self.hsl_edit)

        # Сохранить изменения
        self.save_edit_button = QPushButton("Save", self)
        self.save_edit_button.clicked.connect(lambda: self.save_edited_color(idx))
        self.save_edit_button.setStyleSheet(self.button_style())
        layout.addWidget(self.save_edit_button)

        # Кнопка для удаления цвета
        self.remove_button = QPushButton("Delete", self)
        self.remove_button.clicked.connect(lambda: self.remove_color(idx))
        self.remove_button.setStyleSheet(self.button_style())
        layout.addWidget(self.remove_button)

        # Графический выбор цвета
        self.color_picker_button = QPushButton("Pick new color", self)
        self.color_picker_button.clicked.connect(lambda: self.select_new_color(idx))
        self.color_picker_button.setStyleSheet(self.button_style())
        layout.addWidget(self.color_picker_button)

        self.edit_window.setLayout(layout)
        self.edit_window.show()

    def save_edited_color(self, idx):
        # Сохранить изменения в палитре
        hex_color = self.hex_edit.text()
        if hex_color.startswith("#"):
            self.palette[idx] = hex_color
            self.refresh_palette()
            save_palette_to_xml(self.palette)
            self.edit_window.close()

    def select_new_color(self, idx):
        # Создаем кастомный QColorDialog
        color_dialog = QColorDialog(self)
        #color_dialog.setOption(QColorDialog.ShowAlphaChannel, on=True)

        # Применяем стиль к всему диалогу
        color_dialog.setStyleSheet(select_new_color_setStyleSheet)

        # Устанавливаем текущий цвет, если нужно
        color_dialog.setCurrentColor(QColor(self.palette[idx]))

        # Показываем диалог
        if color_dialog.exec_() == QColorDialog.Accepted:
            selected_color = color_dialog.selectedColor()
            hex_color = selected_color.name()

            # Обновляем палитру
            self.palette[idx] = hex_color
            self.refresh_palette()
            save_palette_to_xml(self.palette)

            # Закрываем окно редактирования
            self.edit_window.close()

    def add_color_dialog(self):  # add color
        if len(self.palette) >= MAX_COLORS:
            QMessageBox.warning(self, "Limit Exceeded", f"Maximum of {MAX_COLORS} colors reached.")
            return

        color_dialog = QColorDialog(self)
        color_dialog.setStyleSheet(add_color_dialog_setStyleSheet)

        if color_dialog.exec_() == QColorDialog.Accepted:
            selected_color = color_dialog.selectedColor()
            if selected_color.isValid():
                hex_color = selected_color.name()
                self.palette.append(hex_color)
                self.refresh_palette()
                save_palette_to_xml(self.palette)

    def remove_color(self, idx):
        # Удаление цвета
        self.palette.pop(idx)
        self.refresh_palette()
        save_palette_to_xml(self.palette)
        self.edit_window.close()

    def save_palette(self):
        save_palette_to_xml(self.palette)
        self.statusBar().showMessage("Palette saved to XML!")

    def save_palette_dialog(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save palette", "", "XML Files (*.xml);;All Files (*)",
                                                  options=options)
        if filename:
            save_palette_to_xml(self.palette, filename)
            self.statusBar().showMessage(f"Palette saved in {filename}!")

    def load_palette_dialog(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Load palette", "", "XML Files (*.xml);;All Files (*)",
                                                  options=options)

        if filename:
            try:
                new_palette = load_palette_from_xml(filename)
                self.palette = new_palette
                self.refresh_palette()
                self.statusBar().showMessage(f"Palette loaded from {filename}!")
            except ValueError as e:
                QMessageBox.warning(self, "Load Error", str(e))

    def show_context_menu(self, point, idx):
        # Создаем контекстное меню
        context_menu = QMenu(self)

        # Добавляем действия в контекстное меню
        hex_action = QAction("Copy HEX", self)
        hex_action.triggered.connect(lambda: self.copy_color_to_clipboard(self.palette[idx], 'hex'))
        context_menu.addAction(hex_action)

        rgb_action = QAction("Copy RGB", self)
        rgb_action.triggered.connect(lambda: self.copy_color_to_clipboard(self.palette[idx], 'rgb'))
        context_menu.addAction(rgb_action)

        hsl_action = QAction("Copy HSL", self)
        hsl_action.triggered.connect(lambda: self.copy_color_to_clipboard(self.palette[idx], 'hsl'))
        context_menu.addAction(hsl_action)

        # Отображаем контекстное меню в месте курсора
        global_point = self.mapToGlobal(point)  # Преобразуем локальные координаты в глобальные
        context_menu.exec_(global_point)  # Показываем меню в глобальной точке

    def copy_color_to_clipboard(self, color, color_type):
        hex_color, rgb_color, hsl_color = convert_color(color)
        if color_type == 'hex':
            pyperclip.copy(hex_color)
        elif color_type == 'rgb':
            pyperclip.copy(f"RGB: {rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]}")
        elif color_type == 'hsl':
            pyperclip.copy(f"HSL: {round(hsl_color[0] * 360)}, {round(hsl_color[1] * 100)}%, {round(hsl_color[2] * 100)}%")

    def button_style(self):
        return button_style_return_setStyleSheet

    def apply_styles(self):
        self.setStyleSheet(apply_styles_main_setStyleSheet)

def main():
    app = QApplication(sys.argv)

    # Окно с лицензионным соглашением
    lic = LicenseWindow()
    lic.show()

    # Ждем завершения окна лицензионного соглашения
    app.exec_()

    # Проверяем, принял ли пользователь соглашение
    if lic.license_accepted:
        ex = ColorPaletteApp()
        ex.show()
        sys.exit(app.exec_())
    else:
        sys.exit()


if __name__ == '__main__':
    main()
