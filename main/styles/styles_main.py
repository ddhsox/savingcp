apply_styles_setStyleSheet = """
            QMainWindow {
                background-color: #282C34;
                color: #ABB2BF;
            }

            QTextEdit {
                background-color: #1A1A1D;
                color: #ABB2BF;
                border: 1px solid #3E4451;
                padding: 10px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #1A1A1D;
                color: #ABB2BF;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2F2F34;
            }
            QPushButton:pressed {
                background-color: #3E4451;
            }
        """
clear_palette_setStyleSheet = """
            QMessageBox {
                background-color: #282C34;
                color: #ABB2BF;
                border: 1px solid #3E4451;
            }
            QMessageBox QLabel {
                color: #D8DEE9;
                font-size: 14px;
            }
            QMessageBox QPushButton {
                background-color: #1A1A1D;
                color: #ABB2BF;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 12px;
            }
            QMessageBox QPushButton:hover {
                background-color: #3E4451;
            }
            QMessageBox QPushButton:pressed {
                background-color: #26262a;
            }
        """
edit_color_setStyleSheet = """
            QWidget {
                background-color: #21252B;  /* Цвет фона для всего окна */
                color: #ABB2BF;  /* Цвет текста по умолчанию */
                border-radius: 5px;
                padding: 5px;
            }

            QLabel {
                font-size: 12px;  /* Размер текста для лейблов */
                color: #D8DEE9;  /* Цвет текста для лейблов */
            }

            QLineEdit {
                background-color: #3E4451;  /* Цвет фона для полей ввода */
                color: #ABB2BF;  /* Цвет текста для полей ввода */
                border: 1px solid #fff;  /* Рамка полей ввода */
                padding: 5px;  /* Внутренний отступ */
                border-radius: 3px;  /* Скругление углов */
            }
        """
select_new_color_setStyleSheet = """
            QColorDialog {
                background-color: #21252B;  /* Цвет фона */
                color: #fff;  /* Цвет текста */
                border-radius: 5px;
            }
            
            QColorDialog QSpinBox{
                background-color:#3e4451;
                color:#fff;
                width:30px;
                height:20px;
            }
            
            QColorDialog QLineEdit {
                background-color: #3E4451;
                color: #ABB2BF;
                border: 1px solid #fff;
                padding: 5px;
                border-radius: 3px;
            }
            
            QColorDialog QPushButton {
                background-color: #1A1A1D;  /* Темный фон для всех кнопок */
                color: #ABB2BF;
                width:200px;
                margin-right:20px;
                border-radius: 5px;
                padding: 5px;
                border: none;
            }

            QColorDialog QPushButton:hover {
                background-color: #1f1f23;
            }

            QColorDialog QPushButton:pressed {
                background-color: #26262a;
            }
            
            QDialogButtonBox QAbstractButton {
                background-color: #1A1A1D;  /* Темный фон для всех кнопок */
                color: #ABB2BF;
                width:200px;
                margin-right:20px;
                border-radius: 5px;
                padding: 5px;
                border: none;
            }

            QDialogButtonBox QAbstractButton:hover {
                background-color: #1f1f23;
            }

            QDialogButtonBox QAbstractButton:pressed {
                background-color: #26262a;
            }
            
        """
add_color_dialog_setStyleSheet = """
            QColorDialog {
                background-color: #21252B;  /* Цвет фона */
                color: #fff;  /* Цвет текста */
                border-radius: 5px;
            }

            QColorDialog QSpinBox {
                background-color: #3e4451;
                color: #fff;
                width: 30px;
                height: 20px;
            }

            QColorDialog QLineEdit {
                background-color: #3E4451;
                color: #ABB2BF;
                border: 1px solid #fff;
                padding: 5px;
                border-radius: 3px;
            }

            QColorDialog QPushButton {
                background-color: #1A1A1D;  /* Темный фон для всех кнопок */
                color: #ABB2BF;
                width: 200px;
                margin-right: 20px;
                border-radius: 5px;
                padding: 5px;
                border: none;
            }

            QColorDialog QPushButton:hover {
                background-color: #1f1f23;
            }

            QColorDialog QPushButton:pressed {
                background-color: #26262a;
            }

            QDialogButtonBox QAbstractButton {
                background-color: #1A1A1D;  /* Темный фон для всех кнопок */
                color: #ABB2BF;
                width: 200px;
                margin-right: 20px;
                border-radius: 5px;
                padding: 5px;
                border: none;
            }

            QDialogButtonBox QAbstractButton:hover {
                background-color: #1f1f23;
            }

            QDialogButtonBox QAbstractButton:pressed {
                background-color: #26262a;
            }
        """
button_style_return_setStyleSheet = """
        QPushButton {
            background-color: #1A1A1D;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #2f2f34;
        }
        QPushButton:pressed {
            background-color: #2b2b3b;
        }
        """
apply_styles_main_setStyleSheet = """
            QMainWindow {
                background-color: #282C34;
                color: #ABB2BF;
            }
            QLabel {
                font-size: 12px;
                color: #D8DEE9;
            }
            
            
            
            QMenuBar {
                background-color: #21252B;
                color: #ABB2BF;
            }
            QMenu {
                background-color: #21252B;
                color: #ABB2BF;
            }
            QMenu::item:selected {
                background-color: #3E4451;
            }
            
            QDialogButtonBox QAbstractButton {
                background-color: #1A1A1D;  /* Темный фон для всех кнопок */
                color: #ABB2BF;
                width:200px;
                margin-right:20px;
                border-radius: 5px;
                padding: 5px;
                border: none;
            }

            QDialogButtonBox QAbstractButton:hover {
                background-color: #1f1f23;
            }

            QDialogButtonBox QAbstractButton:pressed {
                background-color: #26262a;
            }
            
            
        """