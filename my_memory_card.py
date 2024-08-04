from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QButtonGroup,
    QMessageBox
)
from random import shuffle, randint

class Question():
    def __init__(self, question, cor, w1, w2, w3):
        self.question = question
        self.cor = cor 
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

questions_list = []
questions_list.append(Question('Who is your python teacher?', 'Natt', 'Thida', 'Apireak', 'Chenda'))
questions_list.append(Question('Which class are you learning at?', 'Orange', 'Purple', 'Yellow', 'Pink'))
questions_list.append(Question('What school are you learning at?', 'Algorithmics', 'Build Bright', 'Hight bright', 'Panhasasra'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")

lb_question = QLabel("Which nationality does not exist?")
gr_answer = QGroupBox("Answer options")
r1 = QRadioButton("Enets")
r2 = QRadioButton("Smurfs")
r3 = QRadioButton("Chulyms")
r4 = QRadioButton("Aleuts")
btn = QPushButton("Answer")

radioBtnGroup = QButtonGroup()
radioBtnGroup.addButton(r1)
radioBtnGroup.addButton(r2)
radioBtnGroup.addButton(r3)
radioBtnGroup.addButton(r4)

gr_layout = QHBoxLayout()
gr_layout.setSpacing(30)
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(r1)
col1.addWidget(r2)
col2.addWidget(r3)
col2.addWidget(r4)
gr_layout.addLayout(col1)
gr_layout.addLayout(col2)
gr_answer.setLayout(gr_layout)

group_result = QGroupBox("Result")
lb_is_correct = QLabel("If correct or not")
lb_correct = QLabel("The correct answer")
group_result_layout = QVBoxLayout()
group_result_layout.addWidget(lb_is_correct, alignment=Qt.AlignLeft | Qt.AlignTop)
group_result_layout.addWidget(lb_correct, alignment=Qt.AlignCenter)
group_result.setLayout(group_result_layout)

main_layout = QVBoxLayout()
main_layout.setSpacing(50)

main_layout.addWidget(lb_question)
main_layout.addWidget(gr_answer)
main_layout.addWidget(group_result)
group_result.hide()
main_layout.addWidget(btn)

def show_result():
    gr_answer.hide()
    group_result.show()
    btn.setText("Next question")

def show_question():
    group_result.hide()
    gr_answer.show()
    btn.setText("Answer")

    radioBtnGroup.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    radioBtnGroup.setExclusive(True)


def show_correct(respone):
    lb_is_correct.setText(respone)
    show_result()

def check_answer():
    if btn_list[0].isChecked():
        show_correct('Corrected!')
        main_win.score += 1
    else:
        if btn_list[1].isChecked() or btn_list[2].isChecked() or btn_list[3].isChecked():
            show_correct('Incorrected!')
    
    rating = main_win.score / main_win.total * 100
    print(f"Rating: {rating:.2f}")
    print("-"*20)

btn_list = [r1,r2,r3,r4]

def ask(q: Question): # create instance q
    shuffle(btn_list)
    lb_question.setText(q.question)
    btn_list[0].setText(q.cor)
    btn_list[1].setText(q.w1)
    btn_list[2].setText(q.w2)
    btn_list[3].setText(q.w3)

    lb_correct.setText(q.cor)

    show_question()

main_win.total = 0
main_win.score = 0

def next_question():
    curr = randint(0, len(questions_list) - 1)
    q = questions_list[curr]
    ask(q)
    main_win.total += 1
    print(f"Question #{main_win.total}")

def click_ok():
    btn_statuses = [b.isChecked() for b in btn_list]
    if btn.text() == 'Answer' and any(btn_statuses):
        check_answer()
    elif btn.text() == "Next question":
        next_question()
    else:
        m = QMessageBox()
        m.setText("Please Choose one option!")
        m.show()
        m.exec()

btn.clicked.connect(click_ok)
next_question()




main_win.setLayout(main_layout)
main_win.show()
app.exec_()