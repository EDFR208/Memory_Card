from PyQt5.QtCore import Qt #Подключаем Qt.Core для параметра aligment.
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)#Подключаем все нужные виджеты через запятую.
from random import randint, shuffle #Подключаем модуль рандом функцию shuffle
                           #shuffle - перемешивает последовательность (изменяется сама последовательность)
 
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        #все строки надо задать при создании объекта,они запоминаются в свойства.
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list=[]
questions_list.append(Question("Государственный язык Рыб" , 'Рыбий', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question("Национальная еда рыбок", 'Человечина', 'Шашлык', 'Шоколад', 'Рыба'))
questions_list.append(Question("Какой удочкой их ловить", 'Самая обычная удочка', 'Палка и нитка', 'Про-удочка', 'Итальянская удочка'))
questions_list.append(Question("Существуют ли РУСЛАНКИ", 'Да!', 'Это чушь!"', 'Скорее нет, чем да', 'НЕТ!'))
questions_list.append(Question("Сколько может жить среднестатистическая рыба", '25 лет', '1234 года', '2 года', '5 лет'))
questions_list.append(Question("Когда у рыб начинается пенсионный возвраст", '24-25 лет', '10 лет', '7-8 лет', '1-2 года'))
questions_list.append(Question("Зачем люди едят рыбу", 'Что-бы быть сытыми', 'Это их праздничная еда','Они их не едят', 'Им за это дают деньги'))
questions_list.append(Question("Сколько рыб в луже", '0', '1', '12', 'Много'))
questions_list.append(Question("Кто есть рыба для людей", 'Еда', 'Знак мира', 'За это они получают деньги', 'Не знаю'))
questions_list.append(Question("Сколько живет бойцовская рыба", '3-5 лет', 'как обычная рыба', '90-230 лет', '34-45'))
questions_list.append(Question("Какие предметы учат рыбы", 'Рыбий', 'Хинди', 'Японский', 'Итальянский'))
questions_list.append(Question("Сколько классов у рыб", '11 класс', '1 класс', 'они не учатся', '25 классов'))
questions_list.append(Question("Где живет больше всего рыб", 'В Китае', 'В Индонезии', 'В Греции', 'В Италии'))
questions_list.append(Question("Сколько живет акула", '10-20 лет', '3-5 года', '60-100 лет', '32-50 лет'))
questions_list.append(Question("Скорость акулы", '50 км/ч', '65 км/ч', '80 км/ч', 'Не знаю'))

app = QApplication([]) #Создаём приложение. 
btn_OK = QPushButton('Ответить') #Создаём виджет кнопку с надписью "Ответить"
lb_Question = QLabel('Сегодня мы узнаем насколько ты хороший рыболов') #Создаём виджет Текст "Самый сложный вопрос."
 
RadioGroupBox = QGroupBox("Варианты ответов") #Конструктор для создания группы радио кнопок.
                                             #Выделяется визуально!
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2') #Создаём 4 радиокнопки для вариантов ответа.
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() #Все переключатели объединяем в специальную группу.
RadioGroup.addButton(rbtn_1) #Теперь может быть выбран только один из них.
RadioGroup.addButton(rbtn_2)   
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   #Создаём горизантальную линию в группе.
layout_ans2 = QVBoxLayout()   #Создаём вертикальную линию в группе.
layout_ans3 = QVBoxLayout()   #Создаём вертикальную линию в группе.
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
 
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 
 
AnsGroupBox = QGroupBox("Результат теста") #Конструктор для создания группы ответа. Наше 2 окно!
lb_Result = QLabel('прав ты или нет?') #Создаём надпись Результата.
lb_Correct = QLabel('ответ будет тут!') #Создаём надпись Правильного ответа.
 
layout_res = QVBoxLayout()#cоздаём вертикальную линию.
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))#Метод, добавляющий виджет к линии 
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2) 
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() #создаём горизантальную линию  # вопрос
layout_line2 = QHBoxLayout() #создаём горизантальную линию  # варианты ответов или результат теста
layout_line3 = QHBoxLayout() #создаём горизантальную линию  # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) #Метод, добавляющий виджет к линии и располагающий по центру.
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()  # скроем панель с ответом, сначала должна быть видна панель вопросов
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # stretch Растянуть виджет (кнопку) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)# layout_card.setSpacing(5) # пробелы между содержимым
 
def show_result(): #Функция показывающая результат!(Функция-обработчик,отображающая форму ответа.)
    ''' показать панель ответов '''
    RadioGroupBox.hide() #команда hide скрывает наше 1 окно с вариантами ответа.
    AnsGroupBox.show()  #команда show показывает наше 2 окно с результатом ответа.
    btn_OK.setText('Следующий вопрос') #меняется надпись на кнопке "Ответить" на "Следующий вопрос"
 
def show_question(): #Функция показывающая наше 1 окно с вопросом и 4 ответами.(Функция-обработчик,отображающая форму вопроса.)
    ''' показать панель вопросов '''
    RadioGroupBox.show() #показываем наше 1 окно с вариантами ответов.
    AnsGroupBox.hide() #Скрываем наше 2 окно с результатом ответа.
    btn_OK.setText('Ответить') #Меняем текст на кнопке.
    RadioGroup.setExclusive(False) #Снимаем ограничения для сброса выбора.
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)#Снимаем выбор всех переключателей.
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #Возвращаем ограничения.
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] #Создадим список переключателей и перемешаем его элементы с помощью shuffle
 
def ask(q: Question): #функция, задающая (отображающая) указанный вопрос.
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) #Функция из модуля random с её помощью можно перемешать кнопки!
    answers[0].setText(q.right_answer) #Если нажат первый переключатель answer[0], то показать сообщение «Правильно!».
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)#Если нажат любой другой переключатель, то показать сообщение «Неправильно!»
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer)  # ответ 
    show_question() #Функция показывающая наше 1 окно с вопросом и 4 ответами.(Функция-обработчик,отображающая форму вопроса.)
 
def show_correct(res):#Отображаем форму ответа с правильным ответом и пометкой res («Правильно»/«Неправильно»).
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()#Показать функцию 
 
def check_answer():#Проверяем ответ. Если нажат переключатель answer[0], то ответ верный. Если любой другой –– неверный. Вызываем show_correct(), передавая строку с результатом
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():#Метод переключателя .isChecked() проверяет, нажат ли он.
        show_correct('Правильно!')#выводит слово Правильно!
        window.score+=1
        print('Статистика\n- Всего вопросов:', window.total , '\n правильных ответов', window.score)
        print('Рейтинг' ,(window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():#Если нажат любой другой переключатель, то показать сообщение «Неправильно!»
            show_correct('Неверно!')#Неверно!
            print('Рейтинг' ,(window.score/window.total*100), '%')
def next_question():
    '''Задаё следующий вопрос из списка'''
    window.total +=1 #прибавляем единицу.
    print('Статистика\n- Всего вопросов:', window.total , '\n правильных ответов', window.score)
    cur_question = randint(0, len(questions_list)-1)
    window.cur_question = 0 #если список вопросов закончился - идем сначала.
    q=questions_list[cur_question]#взяли вопрос.
    ask(q)

def click_OK():
    #определяет,надо ли показывать другой вопрос либо проверить ответ на этот
    if btn_OK.text() == "Ответить":
        check_answer()#Проверка ответа.
    else:
        next_question()#Следующий вопрос.

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(click_OK) # когда пользователь жмёт на кнопку срабатывает функция.
window.score=0
window.total=0
window.resize(300 , 400)
next_question()                                    
                                     

window.show()
app.exec() #Команда для работы программы пока пользователь не нажмет на крестик.