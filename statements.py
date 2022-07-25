"""Файл содержит шаблоны с которыми сравниваются ответы тестируемых.

А также сами вопросы с утверждениями и описания профессиональных сфер
деятельности.
"""

# Словарь откуда беруться описания профессиональных сфер
# при выводе результатов.
result_dic = {
    '0': ('человек — природа.\n'
          'Cюда входят профессии, в которых человек имеет дело с различными\n'
          'явлениями неживой и живой природы, например биолог, географ,\n'
          'геолог, математик, физик, химик и другие профессии, относящиеся\n'
          'к разряду естественных наук'
          ),
    '1': ('человек — техника.\n'
          'В эту группу профессий включены различные виды трудовой\n'
          'деятельности, в которых человек имеет дело с техникой,\n'
          'её использованием или конструированием, например профессия\n'
          'инженера, оператора, машиниста, механизатора, сварщика и т.п.'
          ),
    '2': ('человек — человек.\n'
          'Сюда включены все виды профессий, предполагающих\n'
          'взаимодействие людей, например политика, религия,\n'
          'педагогика, психология, медицина, торговля, право.'
          ),
    '3': ('человек — знаковая система.\n'
          'В эту группу включены профессии, касающиеся создания,\n'
          'изучения и использования различных знаковых систем,\n'
          'например лингвистика, языки математического программирования,\n'
          'способы графического представления результатов наблюдений и т.п.'
          ),
    '4': ('человек — художественный образ.\n'
          'Эта группа профессий представляет собой различные виды\n'
          'художественно-творческого труда, например литература,\n'
          'музыка, театр, изобразительное искусство.'
          ),
}

# Утверждения из которых респондент будет делать выбор.
# Позиция словаря в списке = номер вопроса (начиная с нуля).
statements = [
    {
        '1': 'Ухаживать за животными.',
        '2': 'Обслуживать машины, приборы (следить, регулировать).'
    },
    {
        '1': 'Помогать больным людям, лечить их.',
        '2': 'Составлять таблицы, схемы, программы вычислительных машин.'
    },
    {
        '1': 'Следить за качеством книжных иллюстраций, плакатов'
        ', художественных открыток, грампластинок.',
        '2': 'Следить за состоянием, развитием растений.'
    },
    {
        '1': 'Обрабатывать материалы (дерево, ткань, пластмассу и т.д.).',
        '2': 'Доводить товары до потребителя (рекламировать, продавать).'
    },
    {
        '1': 'Обсуждать научно-популярные книги, статьи.',
        '2': 'Обсуждать художественные книги.'
    },
    {
        '1': 'Выращивать молодняк животных какой-либо породы.',
        '2': 'Тренировать сверстников (или младших) в выполнении каких-либо '
        'действий (трудовых, учебных, спортивных).'
    },
    {
        '1': 'Копировать рисунки, изображения, настраивать музыкальные '
        'инструменты',
        '2': 'Управлять каким-либо грузовым, подъёмным, транс­ портным '
        'средством (подъёмным краном, машиной и т.п.)'
    },
    {
        '1': 'Сообщать, разъяснять людям нужные для них сведения в справочном'
        ' бюро, во время экскурсии и т.д.',
        '2': 'Художественно оформлять выставки, витрины, участвовать в '
        'подготовке концертов, пьес и т.п.'
    },
    {
        '1': 'Ремонтировать изделия, вещи (одежду, технику), жилище.',
        '2': 'Искать и исправлять ошибки в текстах, таблицах, рисунках.'
    },
    {
        '1': 'Лечить животных.',
        '2': 'Выполнять расчёты, вычисления.'
    },
    {
        '1': 'Выводить новые сорта растений.',
        '2': 'Конструировать новые виды промышленных изделий (машины,'
        ' одежду, дома и т.д.)'
    },
    {
        '1': 'Разбирать споры, ссоры между людьми, убеждать, разъяснять,'
        ' поощрять, наказывать.',
        '2': 'Разбираться в чертежах, схемах, таблицах (проверять,'
        ' уточнять, приводить в порядок).'
    },
    {
        '1': 'Наблюдать, изучать работу кружков художественной'
        ' самодеятельности.',
        '2': 'Наблюдать, изучать жизнь микробов'
    },
    {
        '1': 'Обслуживать, налаживать медицинские приборы и'
        ' аппараты.',
        '2': 'Оказывать людям медицинскую помощь при ранениях,'
        ' ушибах, ожогах и т.п.'
    },
    {
        '1': 'Составлять точные описания, отчёты о наблюдаемых явлениях,'
        ' событиях, измеряемых объектах и др.',
        '2': 'Художественно описывать, изображать события наблюдаемые'
        ' или представляемые.'
    },
    {
        '1': 'Делать лабораторные анализы в больнице.',
        '2': 'Принимать, осматривать больных, беседовать с ними,'
        ' назначать лечение.'
    },
    {
        '1': 'Красить или расписывать стены помещений, поверхность'
        ' изделий.',
        '2': 'Осуществлять монтаж здания или сборку машин, приборов.'
    },
    {
        '1': 'Организовывать культ­ походы людей в театры, музеи, на'
        ' экскурсии, в туристические путешествия и т.п.',
        '2': 'Играть на сцене, принимать участие в концертах.'
    },
    {
        '1': 'Изготовлять по чертежам детали, изделия (машины, одежду),'
        ' строить здания.',
        '2': 'Заниматься черчением, копировать карты, чертежи.'
    },
    {
        '1': 'Вести борьбу с болезнями растений, с вредителями леса, сада.',
        '2': 'Работать на машинах (пишущая машина, компьютер, телетайп,'
        ' телефакс)'
    }
]

# Шаблоны, в соответствии с которыми определяются сферы
# профессиональной деятельности, к которым склонен респондент.
nature = [
    # 1
    {
        '1': 1,
        '2': 0
    },
    # 2
    {
        '1': 0,
        '2': 0
    },
    # 3
    {
        '1': 0,
        '2': 1
    },
    # 4
    {
        '1': 0,
        '2': 0
    },
    # 5
    {
        '1': 0,
        '2': 0
    },
    # 6
    {
        '1': 1,
        '2': 0
    },
    # 7
    {
        '1': 0,
        '2': 0
    },
    # 8
    {
        '1': 0,
        '2': 0
    },
    # 9
    {
        '1': 0,
        '2': 0
    },
    # 10
    {
        '1': 1,
        '2': 0
    },
    # 11
    {
        '1': 1,
        '2': 0
    },
    # 12
    {
        '1': 0,
        '2': 0
    },
    # 13
    {
        '1': 0,
        '2': 1
    },
    # 14
    {
        '1': 0,
        '2': 0
    },
    # 15
    {
        '1': 0,
        '2': 0
    },
    # 16
    {
        '1': 1,
        '2': 0
    },
    # 17
    {
        '1': 0,
        '2': 0
    },
    # 18
    {
        '1': 0,
        '2': 0
    },
    # 19
    {
        '1': 0,
        '2': 0
    },
    # 20
    {
        '1': 1,
        '2': 0
    }
]

technics = [
    # 1
    {
        '1': 0,
        '2': 1
    },
    # 2
    {
        '1': 0,
        '2': 0
    },
    # 3
    {
        '1': 0,
        '2': 0
    },
    # 4
    {
        '1': 1,
        '2': 0
    },
    # 5
    {
        '1': 0,
        '2': 0
    },
    # 6
    {
        '1': 0,
        '2': 0
    },
    # 7
    {
        '1': 0,
        '2': 1
    },
    # 8
    {
        '1': 0,
        '2': 0
    },
    # 9
    {
        '1': 1,
        '2': 0
    },
    # 10
    {
        '1': 0,
        '2': 0
    },
    # 11
    {
        '1': 0,
        '2': 1
    },
    # 12
    {
        '1': 0,
        '2': 0
    },
    # 13
    {
        '1': 0,
        '2': 0
    },
    # 14
    {
        '1': 1,
        '2': 0
    },
    # 15
    {
        '1': 0,
        '2': 0
    },
    # 16
    {
        '1': 0,
        '2': 0
    },
    # 17
    {
        '1': 0,
        '2': 1
    },
    # 18
    {
        '1': 0,
        '2': 0
    },
    # 19
    {
        '1': 1,
        '2': 0
    },
    # 20
    {
        '1': 0,
        '2': 0
    }
]

human = [
    # 1
    {
        '1': 0,
        '2': 0
    },
    # 2
    {
        '1': 1,
        '2': 0
    },
    # 3
    {
        '1': 0,
        '2': 0
    },
    # 4
    {
        '1': 0,
        '2': 1
    },
    # 5
    {
        '1': 0,
        '2': 0
    },
    # 6
    {
        '1': 0,
        '2': 1
    },
    # 7
    {
        '1': 0,
        '2': 0
    },
    # 8
    {
        '1': 1,
        '2': 0
    },
    # 9
    {
        '1': 0,
        '2': 0
    },
    # 10
    {
        '1': 0,
        '2': 0
    },
    # 11
    {
        '1': 0,
        '2': 0
    },
    # 12
    {
        '1': 1,
        '2': 0
    },
    # 13
    {
        '1': 0,
        '2': 0
    },
    # 14
    {
        '1': 0,
        '2': 1
    },
    # 15
    {
        '1': 0,
        '2': 0
    },
    # 16
    {
        '1': 0,
        '2': 1
    },
    # 17
    {
        '1': 0,
        '2': 0
    },
    # 18
    {
        '1': 1,
        '2': 0
    },
    # 19
    {
        '1': 0,
        '2': 0
    },
    # 20
    {
        '1': 0,
        '2': 0
    }
]

sign = [
    # 1
    {
        '1': 0,
        '2': 0
    },
    # 2
    {
        '1': 0,
        '2': 1
    },
    # 3
    {
        '1': 0,
        '2': 0
    },
    # 4
    {
        '1': 0,
        '2': 0
    },
    # 5
    {
        '1': 1,
        '2': 0
    },
    # 6
    {
        '1': 0,
        '2': 0
    },
    # 7
    {
        '1': 0,
        '2': 0
    },
    # 8
    {
        '1': 0,
        '2': 0
    },
    # 9
    {
        '1': 0,
        '2': 1
    },
    # 10
    {
        '1': 0,
        '2': 1
    },
    # 11
    {
        '1': 0,
        '2': 0
    },
    # 12
    {
        '1': 0,
        '2': 1
    },
    # 13
    {
        '1': 0,
        '2': 0
    },
    # 14
    {
        '1': 0,
        '2': 0
    },
    # 15
    {
        '1': 1,
        '2': 0
    },
    # 16
    {
        '1': 0,
        '2': 0
    },
    # 17
    {
        '1': 0,
        '2': 0
    },
    # 18
    {
        '1': 0,
        '2': 0
    },
    # 19
    {
        '1': 0,
        '2': 1
    },
    # 20
    {
        '1': 0,
        '2': 1
    }
]

art = [
    # 1
    {
        '1': 0,
        '2': 0
    },
    # 2
    {
        '1': 0,
        '2': 0
    },
    # 3
    {
        '1': 1,
        '2': 0
    },
    # 4
    {
        '1': 0,
        '2': 0
    },
    # 5
    {
        '1': 0,
        '2': 1
    },
    # 6
    {
        '1': 0,
        '2': 0
    },
    # 7
    {
        '1': 1,
        '2': 0
    },
    # 8
    {
        '1': 0,
        '2': 1
    },
    # 9
    {
        '1': 0,
        '2': 0
    },
    # 10
    {
        '1': 0,
        '2': 0
    },
    # 11
    {
        '1': 0,
        '2': 0
    },
    # 12
    {
        '1': 0,
        '2': 0
    },
    # 13
    {
        '1': 1,
        '2': 0
    },
    # 14
    {
        '1': 0,
        '2': 0
    },
    # 15
    {
        '1': 0,
        '2': 1
    },
    # 16
    {
        '1': 0,
        '2': 0
    },
    # 17
    {
        '1': 1,
        '2': 0
    },
    # 18
    {
        '1': 0,
        '2': 1
    },
    # 19
    {
        '1': 0,
        '2': 0
    },
    # 20
    {
        '1': 0,
        '2': 0
    }
]
# Собрали все шаблоны в один список для перебора в программе.
answers = [nature, technics, human, sign, art]