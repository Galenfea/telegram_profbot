"""Телеграм-бот, проводит тест на проф. ориентацию.

Принимает стандартндые ответы в виде нажатий на клавиши <1> и <2>,
подсчитывает результат по методике академика Климова и сообщает
к какой сфере деятельности наиболее склонен респондент.
"""
# Импорт удобных библиотек для работы с ботом
from telegram import Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)
# Импорт утверждений, которые будут предлагаться в тесте
from statements import statements

# Токен, позволяющий осуществлять управление ботом.
BOT_TOKEN = '5304115149:AAHEuCXNEEeJqnKvTLrxyyhnLnCjaR13Yak'
# Экземпляр класса Bot, который будет
# использоваться для отправки сообщений
bot = Bot(token=BOT_TOKEN)
# Экземпляр класса Updater, который будет
# использоваться для принятия и обработки сообщений
updater = Updater(token=BOT_TOKEN, use_context=True)


def sum_response(pool_counter):
    """Подсчитай результаты тестирования и определи склонности респондента.

    Бланк с ответами пользователя pool_counter сравнивается с заранее заданными
    шаблонами в которых распределны ответы для каждой из профессиональных сфер
    и в случае совпадения нужной сфере добавляется очко.
    Введена проверка случая, когда сферы набирают одинаковое количество очков.
    Выводом функции является итерируемый объект, содержащий номера
    сфер-победительниц.
    """
    # Список из списков словарей, которые содержат информацию о том,
    # относится ли это утверждение к одной из профессиональных сфер.
    # Симулирует бумажный шаблон со строками вопросов и столбцами сфер,
    # в которых перечислены "верные" ответы, которые надо обвести кружками.
    # Формат {'1': 0, '2': 0}
    # где 0 - означает, что утверждение из этого вопроса не относится к
    # данной сфере, а 1 - означает, что утверждение из этого вопроса
    # добавляет очко данной сфере
    from statements import answers

    # Итоговый счётчик, сообщает сколько очков набрала та или иная сфера,
    # позиция числа определяет название сферы:
    # 0 - природа, 1 - техника, 2 - люди, 3 - знаки, 4 - искусство
    professional_areas = [0, 0, 0, 0, 0]
    # Номер вопроса (то есть пары утверждений)
    count = 0
    # Перебираем все вопросы, которые были заданы.
    # Используя новый метод enumerate(<итерируемый объект>),
    # получаем два значения: номер элемента и значение элемента.
    # Благодаря конструкции типа x, y = enumerate(Z) "распаковываем",
    # эти значения по переменным, первая из которых выполняет
    # роль счётчика.
    for count, statement in enumerate(pool_counter):
        # Условный номер профессиональной сферы
        # Обнуляется после выхода из вложенного цикла
        num_of_area = 0
        # Перебираем все профессиональные сферы
        for num_of_area, answer in enumerate(answers):
            # Если словарь с ответом statement из общего списка ответов
            # пользователя, соответствует словарю для вопроса под номером
            # count из шаблона пофессиональной сферы под номером
            # num_of_area, добавить очко в итоговый счётчик на позицию,
            # соответствующую сфере
            if statement == answer[count]:
                professional_areas[num_of_area] += 1
    # Вычисляем индекс той профессиональной сферы,
    # которая набрала больше всего очков.
    winning_area = professional_areas.index(max(professional_areas))
    # Выясняем, сколько очков набрала самая выигрышная сфера
    win_score = professional_areas[winning_area]
    # На тот случай, если столько же очков набрала какая-то другая сфера,
    # делаем проверку сколько раз в список professional_areas входит
    # победное количество очков win_score, если больше одного раза -
    # принимаем меры!
    if (professional_areas.count(win_score)) > 1:
        # Благодаря новому более компактному методу
        # генерируем список из условных номеров нескольких выгравших сфер,
        # если количество очков, которое они получили, одинаково.
        winning_areas = [
                         i for i, score in enumerate(professional_areas)
                         if score == win_score
                         ]
    # В противном случаем делаем кортеж из одного элемента,
    # чтобы соблюсти единообразие и выводить итерируемый объект
    # в любом из случаев. Это понадобится позже, при оглашении
    # результатов теста.
    else:
        winning_areas = (winning_area,)
    # Возвращаем перечисление выигравших сфер
    # (даже если она одна) вызвавшей функции.
    return winning_areas


def carer(update, context):
    """Задавай вопросы в цикле и записивай ответы.

    Функция записывает в контекстные данные ответ пользователя,
    данный на предыдущем этапе диалога и задаёт новый вопрос.
    Какой вопрос задавать определяется при помощи записываемой
    в контекст словарной переменной question_number.
    """
    # Получаем контекстные данные
    user_data = context.user_data
    # Выясняем какой вопрос надо задавать на данном этапе диалога
    question_number = user_data['question_number']
    # Формируем ключ для контекстного словаря,
    # под которым будут храниться данные,
    # переданные пользователем на предыдущем этапе диалога
    category = 'answer_number_' + str(question_number)
    # Получаем текст, введённый пользователем на предыдущем этапе
    text = update.message.text
    # Формируем словарь с ответом пользователя,
    # чтобы в будущем сравнить его с шаблоном
    if text == '1':
        current_answer = {'1': 1, '2': 0}
    elif text == '2':
        current_answer = {'1': 0, '2': 1}
    # Эта ситуация невозможна,
    # но прописана для облегчения отладки
    else:
        current_answer = {'1': 0, '2': 0}
    # Записываем ответ пользователя в виде словаря,
    # в словарь контекста под соответствующим ключом
    user_data[category] = current_answer
    # Изменяем номер вопроса, чтобы воспользоваться
    # им на следующем этапе диалога
    question_number += 1
    # Записываем новый номер вопроса в контекстный словарь
    user_data['question_number'] = question_number
    # Формируем сообщение с парами утверждения для пользователя
    msg = (
            f'\nПара утверждений номер {question_number+1}, '
            f'осталось ещё {19-question_number}\n'
            'Я предпочитаю:\n'
            f'1) {statements[question_number]["1"]}\n'
            f' 2) {statements[question_number]["2"]}\n'
            'Выберите 1 или 2\n'
            )
    # Внимание! Сложно условие с or. Добавляет живости в диалог.
    if question_number == 9 or question_number == 14:
        msg = msg + '\nТак держать, осталось не так уж и много!\n'
    # Формируем кнопки для ленивых пользователей
    reply_keyboard = [['1', '2'], ['/cancel', ]]
    # Отправляем сообщение с вопросом и клавиатуру,
    update.message.reply_text(
        msg,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            resize_keyboard=True,
            # Подсказка что нажимать
            input_field_placeholder='1 или 2?'
        ),
    )
    # Возвращаем следующее состояние диалога
    return question_number


def start(update, context):
    """Приветствуй пользователя и запусти диалог.

    Функция обрабатывает точку входа в диалог и задаёт первый вопрос.
    """
    # Часть стартового сообщения
    text = ('Привет, давайте же узнаем, '
            'к чему у Вас лежит душа!\n'
            'Предлагаем вам 20 пар утверждений.\n'
            'Внимательно прочитав оба утверждения, выберите то,'
            ' которое больше соответствует вашему желанию.\n'
            'Выбор нужно сделать в каждой паре утверждений.\n\n'
            'Если бот не сразу вам отвечает, наберитесь терпения.\n'
            'Ему нужно подумать до 20 секунд.\n'
            )
    # Получаем данные из контекста
    user_data = context.user_data
    # Забираем номер вопроса из контекста,
    # если его нет в словре, назначаем равным 0
    question_number = user_data.get('question_number', 0)
    # Добавляем к стартовому сообщению первую пару утверждений
    msg = (text +
           f'\nПара утверждений номер {question_number+1}, '
           f'осталось ещё {19-question_number}\n'
           'Я предпочитаю:\n'
           f'1) {statements[0]["1"]}\n'
           f' 2) {statements[0]["2"]}\n'
           'Выберите 1 или 2\n'
           )
    reply_keyboard = [['1', '2'], ['/cancel', ]]
    update.message.reply_text(
        msg,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            resize_keyboard=True,
            input_field_placeholder='1 или 2?'
        ),
    )
    # Записываем номер вопроса в контекстный словарь
    # под соответствующим ключом
    user_data['question_number'] = question_number
    # Возвращаем следующее состояние диалога
    return 0


def result(update, context):
    """Возьми данные ответов из контекста и пошли итоги в телеграм.

    Функция принимает последний ответ пользователя, добавляет его
    в данные контекста, затем берёт данные контекста, формирует список
    ответов pool_counter, передаёт его в функцию sum_response и принимает
    из неё список профессиональных сфер с наибольшим количеством очков,
    после чего выводит эту информацию в телеграм.
    """
    # Импорт в функцию  словаря, в котором содержится
    # условный номер и описание профессиональной сферы.
    from statements import result_dic
    user_data = context.user_data

    # Получаем и сохраняем в контекстный словарь последний
    # ответ пользователя на предыдущий вопрос.
    question_number = user_data['question_number']
    category = 'answer_number_' + str(question_number)
    text = update.message.text
    if text == '1':
        current_answer = {'1': 1, '2': 0}
    elif text == '2':
        current_answer = {'1': 0, '2': 1}
    else:
        current_answer = {'1': 0, '2': 0}
    user_data[category] = current_answer

    # Удаляем из контекстного словаря номер вопроса
    del user_data['question_number']
    # С помощью генератора списков формируем чистый бланк
    # для ответов пользователя из контекстного словаря
    pool_counter = [{'1': 0, '2': 0} for i in range(20)]
    count = 0
    # Переносим данные из контекстного словаря в бланк с ответами
    for count in range(20):
        category = 'answer_number_' + str(count)
        pool_counter[count] = user_data[category]
        # Удаляем все данные из контекста
        del user_data[category]
    # Передаём бланк с ответам в функцию подсчета сфер-победительниц
    # и получаем список профессиональных сфер, наиболее интересующих
    # пользователя
    winning_areas = sum_response(pool_counter)
    msg_many = ''
    # Если сфер-победительниц больше одной, делаем комплимент пользователю
    if len(winning_areas) > 1:
        msg_many = ('Вы разносторонняя личность,'
                    '\nвам подходит несколько профессиональных сфер\n'
                    )
    msg = ''
    # Записываем в сообщение информацию о всех сферах-победительницах
    for area in winning_areas:
        msg = (msg +
               '\nВам подходит следующая сфера деятельности: ' +
               result_dic[str(area)] + '\n'
               )
    msg = msg_many + msg
    # Отправляем сообщение и убираем клавиатуру
    update.message.reply_text(msg, reply_markup=ReplyKeyboardRemove())
    # Возвращаем состояние конца диалога
    return ConversationHandler.END


def cancel(update, context):
    """Выйди из диалога, убери клавиатуру, очисти контекстные данные."""
    # Прощаемся с пользователем, убираем клавиаутуру.
    update.message.reply_text('Будет приятно пообщаться с Вами вновь!',
                              reply_markup=ReplyKeyboardRemove())
    # Очищаем контекстный словарь, чтобы не было проблем при следующем диалоге
    context.user_data.clear()
    return ConversationHandler.END


def wrong_answer(update, context):
    """Запроси ответ снова, верни следующей состояние диалога."""
    # Получаем данные из контекста
    user_data = context.user_data
    # Получаем номер вопроса
    question_number = user_data.get('question_number', 0)
    # Сообщаем пользователю, что не поняли его ответа и просим повторить ввод
    msg = ('Кажется, мы друг друга не поняли. Выберите 1 или 2.'
           'Давайте ещё раз.'
           )
    reply_keyboard = [['1', '2'], ['/cancel', ]]
    update.message.reply_text(
        msg,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            resize_keyboard=True,
            input_field_placeholder='1 или 2?'
        ),
    )
    # Возвращаем то состояние диалога, которое было бы,
    # если бы пользователь дал ответ в необходимом формате
    return question_number


def main():
    """Создай диалоговый обработчик и запусти опрос телеграма.

    Функция создаёт экземпляр диспетчера, регистрирует в нём
    диалоговый обработчик и запускает опрос с интервалом 15 секунд
    (не меньше, чтобы телеграм не забанил сервер бота).
    """
    # Создаём экземпляр диспетчера
    dp = updater.dispatcher
    # Формирует список состояний диалога при помощи генератора словарей.
    states = {x: [MessageHandler(Filters.regex('^(1|2)$'), carer)]
              for x in range(20)
              }
    # Добавляем в список итоговую функцию, которая завершит диалог.
    states[19] = [MessageHandler(Filters.text, result)]
    # Задаём обработчику диалогу точку входа в диалог и состояния диалога.
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states=states,
        fallbacks=[CommandHandler('cancel', cancel), MessageHandler(
            Filters.regex('^[a-z^12]*'), wrong_answer
            )
        ]
    )
    # Диспетчер регистрирует обработчик диалога
    dp.add_handler(conv_handler)
    print(
          '\n ДЕМО-версия телеграм бота.\n'
          ' Для полноценного и стабильного релиза\n'
          ' требуется платный интернет хостинг.\n'
          ' Демоверсия использует в качестве хостинга ваш компьютер.\n'
          '\n ВНИМАНИЕ: не закрывайте программу, пока не пройдёте тест.\n'
          ' Бот не работает без запущенной программы.\n'
          '\n Название телеграм бота: Career Orientation TestBot\n'
          '\n Имя бота для поиска: @CareerTestBot\n'
          '\n Для остановки бота закройте программу\n'
          ' или нажмите ctrl+c и подождите 20 секунд.\n'
          )
    updater.start_polling(poll_interval=15)
    updater.idle()


main()
