from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGroupBox, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup)
from random import shuffle
from random import randint

class QQuestion():
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    Pbutton.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    Pbutton.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbutton1.setChecked(False)
    rbutton2.setChecked(False)
    rbutton3.setChecked(False)
    rbutton4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_corect(res):
    lbR.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_corect('Правильно!')
        w.score += 1
        print('Статистика\n-вопросов:', w.total, 'n/-Правильных ответов:', w.score)
        print('Рейтинг:', (w.score/w.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_corect('Неверно!')
        

def ask(q: QQuestion):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question.setText(q.question1)
    lbC.setText(q.right_answer)
    show_question()


def click_OK():
    if Pbutton.text() == 'Ответить':
        check_answer()
    else:
        next_question()

question_list = []
question_list.append(QQuestion('Какие цвета на флаге России?','Белый, Синий, Красный', 'Белый, Красный', 'Синий, Жёлтый',  'Черный, Белый, Красный'))
question_list.append(QQuestion('Человек это', 'Человек', 'Животное', 'Типичный игрок в Доту', 'Свободный индивид общества'))
question_list.append(QQuestion('Когда придумали интернет?', '1969', '1945', '2007', '1998'))
question_list.append(QQuestion('Кто такой Эйнштейн', 'Физик', 'Хз', 'Умный чел', 'Мужик с модной прической'))
question_list.append(QQuestion('Кто такой Жак Фреско', 'Инжинер и футуролог', 'Тот самый чел из мема', 'ладно', 'Чел с загадками и вопросами'))
question_list.append(QQuestion('Когда появился первый мем', '1921', '1943', '1679', '2001'))
question_list.append(QQuestion('Когда придумали первое пианино', '1800', '1883', '1902', '1789'))
question_list.append(QQuestion('Когда придумали VPN', '1996', '860', '1396', '2008'))
question_list.append(QQuestion('День рождения бутерброда', '14 марта', '33 сентября', 'Не знаю, но бутер я съем', '5 января'))
question_list.append(QQuestion('Самый популярный покемон в России', 'Мью', 'Пикачу', 'хз не шарю', 'чармандер'))
app = QApplication([])

RadioGroupBox = QGroupBox('Варианты ответов')

Pbutton = QPushButton('Ответить')
question = QLabel('Самый сложный вопрос в мире!')

Pbutton.clicked.connect(click_OK)

rbutton1 = QRadioButton('Вариант 1')
rbutton2 = QRadioButton('Вариант 2')
rbutton3 = QRadioButton('Вариант 3')
rbutton4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbutton1)
RadioGroup.addButton(rbutton2)
RadioGroup.addButton(rbutton3)
RadioGroup.addButton(rbutton4)

layoutHH = QHBoxLayout()
lm1 = QVBoxLayout()
lm = QVBoxLayout()

lm.addWidget(rbutton1)
lm.addWidget(rbutton2)
lm1.addWidget(rbutton3)
lm1.addWidget(rbutton4)

layoutHH1 = QHBoxLayout()
layoutH1 = QHBoxLayout()

layoutH1.addLayout(lm)
layoutH1.addLayout(lm1)

RadioGroupBox.setLayout(layoutH1)
layoutHH1.addWidget(Pbutton)
lmm = QVBoxLayout()
lmm.addLayout(layoutHH)
lmm.addWidget(RadioGroupBox)
lmm.addLayout(layoutHH1)
layoutHH.addWidget(question)

AnsGroupBox = QGroupBox('Результат теста')
lbR = QLabel('прав ты или нет?')
lbC = QLabel('ответ будет тут!')

lr = QVBoxLayout()
lr.addWidget(lbR, alignment=(Qt.AlignLeft | Qt.AlignTop))
lr.addWidget(lbC, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(lr)

ll1 = QHBoxLayout()
ll2 = QHBoxLayout()
ll3 = QHBoxLayout()

ll1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

ll2.addWidget(RadioGroupBox)
ll2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

ll3.addStretch(1)
ll3.addWidget(Pbutton, stretch=2)
ll3.addStretch(1)

lcard = QVBoxLayout()

lcard.addLayout(ll1, stretch=2)
lcard.addLayout(ll2, stretch=8)
lcard.addStretch(1)
lcard.addLayout(ll3, stretch=1)
lcard.addStretch(1)
lcard.setSpacing(5)

answer = [rbutton1, rbutton2, rbutton3, rbutton4]


Pbutton.clicked.connect(check_answer)

#q1 = QQuestion()

w = QWidget()
w.setLayout(lcard)
w.setWindowTitle('Memory Card')
w.resize(500, 200)

def next_question():
    cur_question = randint(0, len(question_list) - 1)
    if cur_question >= len(question_list):
        cur_question = 0
    q = question_list[cur_question]
    ask(q)
    w.total += 1
    print('Статистика\n-вопросов:', w.total, 'n/-Правильных ответов:', w.score)
w.total = 0

w.score = 0

next_question()
w.move(100, 100)
w.show()
app.exec_()


