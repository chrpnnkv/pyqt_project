import sqlite3
import sys
import re

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QHeaderView, QMessageBox
from PyQt5.QtGui import QColor, QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt, QDate, QTime
from PIL import Image

from ui_main_window import Ui_MainWindow
from ui_create_event import Ui_CreateEvent
from ui_more import Ui_More
from ui_create_newplace import Ui_CreateNewPlace
from ui_create_newtype import Ui_CreateNewType
from ui_event_search import Ui_SearchEvent

from datetime import date

DB = "leisure.db"


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(620, 420)
        self.setWindowTitle('МероприЯтность')
        self.setWindowIcon(QIcon('icon.ico'))

        self.pixmap1 = QPixmap('decor/main1.png')
        self.picture1.setScaledContents(True)
        self.picture1.setPixmap(self.pixmap1)

        self.pixmap2 = QPixmap('decor/main2.png')
        self.picture2.setScaledContents(True)
        self.picture2.setPixmap(self.pixmap2)

        current_date = date.today()
        self.findButton.clicked.connect(lambda: self.search(current_date))
        self.createButton.clicked.connect(lambda: self.create(current_date))
        self.update_database(current_date)

    def search(self, date):
        self.add_form = SearchWindow(self, date)
        self.add_form.show()

    def create(self, date):
        self.add_form = CreateWindow(self, date)
        self.add_form.show()

    def update_database(self, current_date):
        self.con = sqlite3.connect(DB)
        database = self.con.cursor().execute("""SELECT id, date from events""").fetchall()
        for i in database:
            if date(int(i[1][-4:]), int(i[1][3:5]), int(i[1][:2])) < current_date:
                self.con.cursor().execute(f"""DELETE from events where id = {i[0]}""")
        self.con.commit()


class SearchWindow(QMainWindow, Ui_SearchEvent):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1320, 670)
        self.setWindowTitle('Поиск мероприятий')
        self.setWindowIcon(QIcon('icon.ico'))
        self.con = sqlite3.connect(DB)
        self.date = args[1]

        self.pixmap = QPixmap('decor/search.png')
        self.picture.setScaledContents(True)
        self.picture.setPixmap(self.pixmap)

        self.types = list(map(lambda x: x[0], self.con.cursor().execute("""SELECT name FROM types""").fetchall()))
        self.types = sorted(self.types)
        self.typeBox.addItems(self.types)
        self.places = list(map(lambda x: x[0], self.con.cursor().execute("""SELECT name FROM places""").fetchall()))
        self.places = sorted(self.places)
        self.placeBox.addItems(self.places)

        self.loadTable()
        self.moreButton.clicked.connect(self.more_about)
        self.searchButton.clicked.connect(self.search)

        self.dateEdit.setMinimumDate(QDate(self.date.year, self.date.month, self.date.day))
        self.dateEdit.setDisplayFormat("dd.MM.yyyy")
        self.timeEdit.setDisplayFormat("hh:mm")
        self.anydate.setChecked(True)
        self.anytime.setChecked(True)

    def loadTable(self, *filters):
        res = self.con.cursor().execute("""SELECT e.id, e.name, t.name, pl.name, e.date, e.begin, e.end 
                                         FROM events e
                                         JOIN types t ON t.id = e.type
                                         JOIN places pl ON pl.id = e.place
                                         ORDER BY e.id""").fetchall()
        if any(map(lambda x: x is not None, filters)):
            if filters[0] is not None:
                res = list(filter(lambda x: x[2] == filters[0], res))
            if filters[1] is not None:
                res = list(filter(lambda x: x[3] == filters[1], res))
            if filters[2] is not None:
                res = list(filter(lambda x: x[4] == filters[2], res))
            if filters[3] is not None:
                res = list(filter(lambda x: x[5] == filters[3], res))

        title = ['ID', 'Название', 'Тип', 'Место', 'Дата', 'Начало', 'Окончание']
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setRowCount(1)
        if res:
            for k, elem in enumerate(title):
                self.tableWidget.setItem(0, k, QTableWidgetItem(str(elem)))
                self.tableWidget.item(0, k).setFlags(Qt.ItemIsEnabled)
                self.tableWidget.item(0, k).setBackground(QColor(169, 176, 143))

            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(elem)))
                    self.tableWidget.item(i + 1, j).setFlags(Qt.ItemIsEnabled)
            self.tableWidget.resizeColumnsToContents()
        else:
            self.error_message('Ничего не найдено')

    def more_about(self):
        id = self.more.text()
        if id:
            if id.isdigit():
                res = self.con.cursor().execute(f"""SELECT * FROM events
                                             WHERE id = {id}""").fetchone()
                if res:
                    self.add_form = MoreAboutWindow(self, res)
                    self.add_form.show()
                    self.more.setText('')
                else:
                    self.error_message('Нет мероприятия с таким ID')
            else:
                self.error_message('Нет мероприятия с таким ID')

    def search(self):
        type, place, date, time = None, None, None, None
        if self.typeBox.currentText() != 'Все':
            type = self.typeBox.currentText()
        if self.placeBox.currentText() != 'Все':
            place = self.placeBox.currentText()
        if not self.anydate.isChecked():
            date = self.dateEdit.date().toString('dd.MM.yyyy')
        if not self.anytime.isChecked():
            time = self.timeEdit.time().toString('hh:mm')
        self.loadTable(type, place, date, time)

    def error_message(self, text):
        msg = QMessageBox(self)
        font = QFont('Century Gothic', 9)
        msg.setWindowIcon(QIcon('icon.ico'))
        msg.setFont(font)
        msg.setWindowTitle('Ошибка')
        msg.setText(text)
        msg.setStyleSheet(
            "QPushButton {background-color: rgb(105, 109, 88); color: white; font: 10pt 'Century Gothic';}")
        msg.exec()


class CreateWindow(QMainWindow, Ui_CreateEvent):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(835, 745)
        self.setWindowTitle('Редактор мероприятий')
        self.setWindowIcon(QIcon('icon.ico'))
        self.con = sqlite3.connect(DB)

        self.add_placeButton.clicked.connect(self.add_place)
        self.add_typeButton.clicked.connect(self.add_type)
        self.imgButton.clicked.connect(self.add_img)
        self.createButton.clicked.connect(self.create)
        self.changeButton.clicked.connect(self.update_data)

        self.pixmap1 = QPixmap('decor/create1.png')
        self.picture1.setScaledContents(True)
        self.picture1.setPixmap(self.pixmap1)

        self.pixmap2 = QPixmap('decor/create2.png')
        self.picture2.setScaledContents(True)
        self.picture2.setPixmap(self.pixmap2)

        self.types = list(map(lambda x: x[0], self.con.cursor().execute("""SELECT name FROM types""").fetchall()))
        self.types = sorted(self.types)
        self.typeBox.addItems(self.types)
        self.places = list(map(lambda x: x[0], self.con.cursor().execute("""SELECT name FROM places""").fetchall()))
        self.places = sorted(self.places)
        self.placeBox.addItems(self.places)
        self.error_label.setText('')
        self.syntax_label.setText('')

        self.date = args[1]
        self.dateEdit.setMinimumDate(QDate(self.date.year, self.date.month, self.date.day))
        self.dateEdit.setDisplayFormat("dd.MM.yyyy")
        self.begintimeEdit.setDisplayFormat("hh:mm")
        self.endtimeEdit.setDisplayFormat("hh:mm")

        self.loadTable()

        self.image = None
        self.descript = None

    def loadTable(self):
        res = self.con.cursor().execute("""SELECT e.id, e.name, t.name, pl.name, e.date, e.begin, e.end 
                                                 FROM events e
                                                 JOIN types t ON t.id = e.type
                                                 JOIN places pl ON pl.id = e.place
                                                 ORDER BY e.id""").fetchall()
        title = ['ID', 'Название', 'Тип', 'Место', 'Дата', 'Начало', 'Окончание']
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setRowCount(1)
        if res:
            for k, elem in enumerate(title):
                self.tableWidget.setItem(
                    0, k, QTableWidgetItem(str(elem)))
                self.tableWidget.item(0, k).setFlags(Qt.ItemIsEnabled)
                self.tableWidget.item(0, k).setBackground(QColor(169, 176, 143))

            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(elem)))
                self.tableWidget.item(i + 1, 0).setFlags(Qt.ItemIsEnabled)
        self.tableWidget.resizeColumnsToContents()

    def add_type(self):
        self.add_form = TypeWindow(self)
        self.add_form.show()
        if self.add_form.error_label.text() == 'Успешно!':
            self.update_box('types')

    def add_place(self):
        self.add_form = PlaceWindow(self)
        self.add_form.show()
        if self.add_form.error_label.text() == 'Успешно!':
            self.update_box('places')

    def add_img(self):
        self.image = QFileDialog.getOpenFileName(self, 'Выбрать афишу', '', 'Картинка (*.jpg);;Картинка (*.png)')[0]

    def create(self):
        if self.name.text():
            name = self.name.text()
            if self.typeBox.currentText() != 'Все':
                type = self.con.cursor().execute(
                    f"""select id from types where name = '{self.typeBox.currentText()}'""").fetchone()[0]
                if self.placeBox.currentText() != 'Все':
                    place = self.con.cursor().execute(
                        f"""select id from places where name = '{self.placeBox.currentText()}'""").fetchone()[0]
                    date = self.dateEdit.date().toString('dd.MM.yyyy')
                    begin = self.begintimeEdit.time().toString('hh:mm')
                    end = self.endtimeEdit.time().toString('hh:mm')
                    if self.check_time([None, place, date, begin, end]):
                        self.error_label.setText('')
                        event_id = len(self.con.cursor().execute(f"""select id from events""").fetchall()) + 1
                        if self.image is not None:
                            im = Image.open(self.image)
                            im.save(f'images/{event_id}.{self.image.split("/")[-1].split(".")[-1]}')
                            self.image = f'images/{event_id}.{self.image.split("/")[-1].split(".")[-1]}'
                        else:
                            self.image = 'images/null.png'
                        if self.description.toPlainText():
                            self.descript = f'description/{event_id}.txt'
                            with open(self.descript, 'w', encoding='utf-8') as f:
                                print(self.description.toPlainText(), file=f)
                        else:
                            self.descript = 'description/null.txt'
                        self.con.cursor().execute(
                            """INSERT INTO events(name, type, place, date, begin, end, description, image) 
                            VALUES('{}', {}, {}, '{}', '{}', '{}', '{}', '{}')""".format(name, type, place, date,
                                                                                         begin, end, self.descript,
                                                                                         self.image))
                        self.save(name, self.typeBox.currentText(), self.placeBox.currentText(), date, begin, end)
                        self.image, self.descript = None, None
                    else:
                        self.time_error()
                else:
                    self.error_label.setText('Укажите место проведения')
            else:
                self.error_label.setText('Укажите тип мероприятия')
        else:
            self.error_label.setText('Укажите название мероприятия')

    def save(self, *args):
        dlg = QMessageBox(self)
        uic.loadUi('ui/dialog.ui', dlg)
        dlg.setFixedSize(400, 300)
        dlg.setWindowTitle('Создание')
        dlg.setWindowIcon(QIcon('icon.ico'))
        text = '''Название: {}
Тип: {}
Место проведения: {}
Мероприятие будет проходить {} с {} до {}'''.format(*args)
        dlg.setText(text)
        dlg.setStyleSheet("background-color: rgb(234, 241, 210); color: black; font: 9pt 'Century Gothic';")
        button = dlg.exec()

        self.error_label.setText('')
        self.name.setText('')
        self.typeBox.setCurrentText('Все')
        self.placeBox.setCurrentText('Все')
        self.dateEdit.setDate(QDate(self.date.year, self.date.month, self.date.day))
        self.begintimeEdit.setTime(QTime(0, 0))
        self.endtimeEdit.setTime(QTime(0, 0))
        self.description.setPlainText('')

        self.con.commit()
        self.loadTable()

    def update_box(self, arg):
        if arg == 'types':
            self.types = list(map(lambda x: x[0], self.con.cursor().execute("""SELECT name FROM types""").fetchall()))
            self.types = sorted(self.types)
            self.typeBox.clear()
            self.typeBox.addItem('Все')
            self.typeBox.addItems(self.types)
        else:
            self.places = list(map(lambda x: x[0], self.con.cursor().execute("""SELECT name FROM places""").fetchall()))
            self.places = sorted(self.places)
            self.placeBox.clear()
            self.placeBox.addItem('Все')
            self.placeBox.addItems(self.places)

    def generate_new_row(self, data):
        cur = self.con.cursor()
        self.syntax_label.setText('')
        f = True
        old_data = list(cur.execute(f"""Select * from events where id = {data[0]}""").fetchone())
        new_data = old_data[:]
        if data[1] == 2:
            if data[2] in self.types:
                self.syntax_label.setText('')
                new_type = cur.execute(f"""Select id from types where name = '{data[2]}'""").fetchone()
                new_data[2] = new_type[0]
            else:
                self.syntax_label.setText('Такого типа не существует')
                f = False
        elif data[1] == 3:
            if data[2] in self.places:
                self.syntax_label.setText('')
                new_place = cur.execute(f"""Select id from places where name = '{data[2]}'""").fetchone()
                new_data[3] = new_place[0]
            else:
                self.syntax_label.setText('Такого места не существует')
                f = False
        elif data[1] == 4:
            if re.fullmatch('\d\d.\d\d.\d\d\d\d', data[2]):
                if int(data[2][6:]) > 2023:
                    month = int(data[2][3:5])
                    day = int(data[2][:2])
                    if month in (1, 3, 5, 7, 8, 10, 12):
                        if 0 < day < 32:
                            self.syntax_label.setText('')
                            new_data[4] = data[2]
                        else:
                            self.syntax_label.setText('Неверный формат')
                            f = False
                    elif month in (4, 6, 9, 11):
                        if 0 < day < 31:
                            self.syntax_label.setText('')
                            new_data[4] = data[2]
                        else:
                            self.syntax_label.setText('Неверный формат')
                            f = False
                    elif month == 2:
                        if 0 < day < 29:
                            self.syntax_label.setText('')
                            new_data[4] = data[2]
                        else:
                            self.syntax_label.setText('Неверный формат')
                            f = False
                    else:
                        self.syntax_label.setText('Неверный формат')
                        f = False
                else:
                    self.syntax_label.setText('Неверный формат')
                    f = False
            else:
                self.syntax_label.setText('Неверный формат')
                f = False
        elif data[1] in (5, 6):
            if re.fullmatch('\d\d:\d\d', data[2]):
                if int(data[2][:2]) < 24 and int(data[2][3:]) < 60:
                    place, date = cur.execute(f"""SELECT place, date FROM events WHERE id = {data[0]}""").fetchone()
                    if self.check_time([int(data[0]), place, date, data[2] if data[1] == 5 else old_data[5],
                                        data[2] if data[1] == 6 else old_data[6]]):
                        self.syntax_label.setText('')
                        new_data[data[1]] = data[2]
                    else:
                        self.time_error()
                        f = False
                else:
                    self.syntax_label.setText('Неверный формат')
                    f = False
            else:
                self.syntax_label.setText('Неверный формат')
                f = False
        else:
            new_data[data[1]] = data[2]
        if f:
            cur.execute(f"""delete from events where id = {data[0]}""")
            cur.execute(f"""insert into events values (?, ?, ?, ?, ?, ?, ?, ?, ?)""", new_data)
            self.con.commit()
            self.syntax_label.setText('Изменения успешно сохранены')
        self.loadTable()

    def update_data(self):
        data = list(map(lambda x: (self.tableWidget.item(x.row(), 0).text(), x.column(), x.text()),
                        self.tableWidget.selectedItems()))
        if data[0][2]:
            self.generate_new_row(data[0])
        else:
            self.syntax_label.setText('Введите значение')

    def check_time(self, data):
        if data[4] < data[3]:
            data[4] = f'{int(data[4][:2]) + 24}:{data[4][3:]}'
        open_time, close_time = self.con.cursor().execute(
            f"""SELECT opening, closing FROM places WHERE id = {data[1]}""").fetchone()
        if close_time < open_time:
            close_time = f'{int(close_time[:2]) + 24}:{close_time[3:]}'
        if open_time <= data[3] < close_time and open_time < data[4] <= close_time:
            all_events = self.con.cursor().execute(
                f"""SELECT id, begin, end FROM events WHERE place = {data[1]} and date = '{data[2]}'""").fetchall()
            all_events = sorted(all_events, key=lambda x: (x[0], x[1]))
            for i in all_events:
                f = True
                if data[0] is not None:
                    if i[0] == data[0]:
                        f = False
                if (i[1] >= data[4] or i[2] <= data[3]) and f:
                    return True
                if (i[1] < data[4] < i[2] or i[1] < data[3] < i[2]) and f:
                    return False
            return True
        return False

    def time_error(self):
        msg = QMessageBox(self)
        font = QFont('Century Gothic', 9)
        msg.setWindowIcon(QIcon('icon.ico'))
        msg.setFont(font)
        msg.setWindowTitle('Ошибка')
        msg.setText('Мероприятие не может быть проведено в это время')
        msg.setStyleSheet(
            "QPushButton {background-color: rgb(105, 109, 88); color: white; font: 10pt 'Century Gothic';}")
        msg.exec()


class TypeWindow(QMainWindow, Ui_CreateNewType):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(310, 190)
        self.setWindowTitle('Добавить тип')
        self.setWindowIcon(QIcon('icon.ico'))
        self.createButton.clicked.connect(self.create)
        self.con = sqlite3.connect(DB)
        self.parent_widget = args[0]

    def create(self):
        txt = self.typeEdit.text()
        if txt:
            data = list(map(lambda x: x[0], self.con.cursor().execute(f"""select name from types""").fetchall()))
            if txt not in data:
                self.con.cursor().execute(f"""INSERT INTO types(name) VALUES('{txt}')""")
                self.error_label.setText('Успешно!')
                self.con.commit()
                self.parent_widget.update_box('types')
            else:
                self.error_label.setText('Такой тип уже существует')
        else:
            self.error_label.setText('Введите тип')


class PlaceWindow(QMainWindow, Ui_CreateNewPlace):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(345, 370)
        self.setWindowTitle('Добавить место')
        self.setWindowIcon(QIcon('icon.ico'))
        self.createButton.clicked.connect(self.create)
        self.con = sqlite3.connect(DB)
        self.parent_widget = args[0]
        self.opentimeEdit.setDisplayFormat("hh:mm")
        self.closetimeEdit.setDisplayFormat("hh:mm")

    def create(self):
        name = self.nameEdit.text()
        if name:
            address = self.addressEdit.text()
            if address:
                data = list(map(lambda x: (x[0], x[1]),
                                self.con.cursor().execute(f"""select name, address from places""").fetchall()))
                if (name, address) not in data:
                    open = self.opentimeEdit.time().toString('hh:mm')
                    close = self.closetimeEdit.time().toString('hh:mm')
                    if open == '00:00' and close == '00:00':
                        self.error_label.setText('Измените часы работы')
                    else:
                        new_data = [name, address, open, close]
                        self.con.cursor().execute(
                            """INSERT INTO places(name, address, opening, closing) VALUES(?, ?, ?, ?)""", new_data)
                        self.error_label.setText('Успешно!')
                        self.con.commit()
                        self.parent_widget.update_box('places')
                else:
                    self.error_label.setText('Такое место уже существует')
            else:
                self.error_label.setText('Введите адрес')
        else:
            self.error_label.setText('Введите название')


class MoreAboutWindow(QWidget, Ui_More):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(715, 470)
        self.setWindowTitle('Детали')
        self.setWindowIcon(QIcon('icon.ico'))
        self.description.setReadOnly(True)
        self.con = sqlite3.connect(DB)

        data = args[1]
        filename = data[7]
        image = data[8]

        data = [data[1], *self.con.cursor().execute(f"""select name from types where id = {data[2]}""").fetchone(),
                *self.con.cursor().execute(f"""select name, address from places where id = {data[3]}""").fetchone(),
                data[4], data[5]]

        with open(filename, encoding='utf-8') as f:
            txt = '\n'.join(list(map(str.strip, f.readlines())))
            data.append(txt)

        text = '''Название: {}
        
Тип: {}

Место проведения: {} по адресу {}

Мероприятие будет проходить {} в {}

Дополнительное описание: {}'''.format(*data)

        self.description.setPlainText(text)
        self.pixmap = QPixmap(image)
        self.picture.setScaledContents(True)
        self.picture.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())
