"""
Создаёт все файлы проекта Таро. Полностью переписан общий расклад.
Запуск: python setup.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = {}

# ============ tarot_data.py ============
FILES["tarot_data.py"] = r'''
"""78 карт Таро + генератор глубоких уникальных толкований."""
import random
from collections import Counter

MAJOR = [
    {"name": "Шут", "num": "0", "symbol": "🃏",
     "description": "новое начало, спонтанность, прыжок в неизвестность",
     "love": "свежесть чувств, новые знакомства, лёгкость",
     "career": "начало нового пути, готовность рискнуть",
     "money": "нестабильность, но неожиданные возможности",
     "future": "впереди новое и неизвестное, потребуется доверие"},
    {"name": "Маг", "num": "I", "symbol": "🎩",
     "description": "воля, мастерство, проявление намерения в реальность",
     "love": "умение привлечь, активная позиция",
     "career": "успех через инициативу и таланты",
     "money": "предприимчивость, умение зарабатывать",
     "future": "вы способны управлять событиями"},
    {"name": "Верховная Жрица", "num": "II", "symbol": "🌙",
     "description": "интуиция, тайна, скрытые знания",
     "love": "глубокие, но скрытые чувства, недосказанность",
     "career": "не всё очевидно, доверьтесь интуиции",
     "money": "скрытые факторы, осторожность",
     "future": "многое пока скрыто — прислушайтесь к себе"},
    {"name": "Императрица", "num": "III", "symbol": "🌸",
     "description": "плодородие, творчество, забота, изобилие",
     "love": "тёплые, заботливые отношения, рост семьи",
     "career": "творческий рост, плодотворный период",
     "money": "изобилие, доходы растут",
     "future": "плодотворный период, воплощение задуманного"},
    {"name": "Император", "num": "IV", "symbol": "👑",
     "description": "структура, власть, порядок, авторитет",
     "love": "стабильные отношения, возможен контроль",
     "career": "успех через дисциплину и структуру",
     "money": "стабильность, финансовый контроль",
     "future": "порядок и стабильность, ситуация под контролем"},
    {"name": "Иерофант", "num": "V", "symbol": "📿",
     "description": "традиции, обучение, духовный наставник",
     "love": "традиционные отношения, серьёзные намерения",
     "career": "работа в структуре, обучение, наставник",
     "money": "традиционные методы, стабильность",
     "future": "уроки и обучение, опора на опыт"},
    {"name": "Влюблённые", "num": "VI", "symbol": "💕",
     "description": "выбор, любовь, гармония, союз",
     "love": "взаимные чувства, важный выбор, единство",
     "career": "удачное партнёрство, союз",
     "money": "совместные финансы, доход в паре",
     "future": "важный выбор и партнёрство"},
    {"name": "Колесница", "num": "VII", "symbol": "🏇",
     "description": "победа, движение, контроль над ситуацией",
     "love": "активное развитие, победа над препятствиями",
     "career": "успех через настойчивость",
     "money": "рост через действие, доход от активности",
     "future": "победа и движение вперёд"},
    {"name": "Сила", "num": "VIII", "symbol": "🦁",
     "description": "внутренняя сила, терпение, мягкая мощь",
     "love": "гармония через терпение, зрелые чувства",
     "career": "успех через выдержку",
     "money": "равновесие через терпение",
     "future": "вы справитесь, внутренней силы достаточно"},
    {"name": "Отшельник", "num": "IX", "symbol": "🕯️",
     "description": "уединение, поиск истины, внутренний свет",
     "love": "период осмысления отношений",
     "career": "время подумать, уединённая работа",
     "money": "скромность, экономия",
     "future": "время осмысления, ответ внутри вас"},
    {"name": "Колесо Фортуны", "num": "X", "symbol": "🎡",
     "description": "судьба, перемены, циклы, удача",
     "love": "перемены в отношениях, поворот судьбы",
     "career": "удачный поворот, неожиданное везение",
     "money": "возможно везение, но и перемены",
     "future": "судьба готовит перемены, колесо поворачивается"},
    {"name": "Справедливость", "num": "XI", "symbol": "⚖️",
     "description": "правда, баланс, закон, справедливость",
     "love": "честные, равные отношения, ясность",
     "career": "признание по заслугам",
     "money": "справедливые доходы",
     "future": "всё будет по справедливости"},
    {"name": "Повешенный", "num": "XII", "symbol": "🙃",
     "description": "остановка, жертва, взгляд под другим углом",
     "love": "пауза, ожидание, пересмотр чувств",
     "career": "задержка — время переосмыслить подход",
     "money": "пауза в делах",
     "future": "время переосмыслить, взгляните иначе"},
    {"name": "Смерть", "num": "XIII", "symbol": "💀",
     "description": "конец цикла, трансформация, перерождение",
     "love": "завершение или трансформация отношений",
     "career": "конец этапа — начало нового",
     "money": "крупные перемены в финансах",
     "future": "конец одного этапа, начало другого"},
    {"name": "Умеренность", "num": "XIV", "symbol": "🍷",
     "description": "баланс, гармония, терпение, алхимия",
     "love": "гармоничные отношения, баланс",
     "career": "стабильный прогресс, не спешить",
     "money": "умеренность в тратах",
     "future": "гармония и баланс, золотая середина"},
    {"name": "Дьявол", "num": "XV", "symbol": "😈",
     "description": "искушение, зависимость, материальные узы",
     "love": "страсть, но риск зависимости",
     "career": "материальная выгода, осторожно с этикой",
     "money": "соблазн лёгких денег, кредиты",
     "future": "остерегайтесь искушений"},
    {"name": "Башня", "num": "XVI", "symbol": "🗼",
     "description": "крушение, внезапные перемены, разрушение старого",
     "love": "возможен разрыв, кризис, очищение",
     "career": "внезапные перемены, слом планов",
     "money": "финансовые потрясения",
     "future": "внезапные события всё изменят"},
    {"name": "Звезда", "num": "XVII", "symbol": "⭐",
     "description": "надежда, вдохновение, исцеление, свет",
     "love": "светлые надежды, чистота чувств",
     "career": "вдохновение, светлая полоса",
     "money": "улучшение, надежда",
     "future": "светлая полоса, надежда оправдывается"},
    {"name": "Луна", "num": "XVIII", "symbol": "🌕",
     "description": "иллюзии, страхи, подсознание, неясность",
     "love": "неясность, страхи, сомнения",
     "career": "будьте осторожны, многое не то, чем кажется",
     "money": "скрытые риски",
     "future": "многое неясно — доверьтесь интуиции"},
    {"name": "Солнце", "num": "XIX", "symbol": "☀️",
     "description": "радость, успех, ясность, победа",
     "love": "яркие, радостные отношения",
     "career": "успех, признание, ясные цели",
     "money": "достаток, успех",
     "future": "светлый период, всё прояснится"},
    {"name": "Суд", "num": "XX", "symbol": "📯",
     "description": "возрождение, важный этап, пробуждение",
     "love": "возвращение чувств, важное решение",
     "career": "новые возможности, призвание",
     "money": "возрождение финансов, второй шанс",
     "future": "важный этап, возрождение"},
    {"name": "Мир", "num": "XXI", "symbol": "🌍",
     "description": "завершение, целостность, успех, гармония",
     "love": "гармония, полнота чувств, зрелый союз",
     "career": "завершение проекта, успех",
     "money": "финансовое благополучие",
     "future": "успешное завершение, награда"},
]

SUITS = {
    "Жезлы": {"symbol": "🪄", "gen": "Жезлов", "theme": "энергии и действий"},
    "Кубки": {"symbol": "🏆", "gen": "Кубков", "theme": "чувств и отношений"},
    "Мечи": {"symbol": "⚔️", "gen": "Мечей", "theme": "мыслей и истины"},
    "Пентакли": {"symbol": "🪙", "gen": "Пентаклей", "theme": "денег и материи"},
}

RANKS = [
    ("Туз", "A", "новое начало"),
    ("Двойка", "II", "баланс и партнёрство"),
    ("Тройка", "III", "рост и первые результаты"),
    ("Четвёрка", "IV", "стабильность и прочная основа"),
    ("Пятёрка", "V", "конфликт и преодоление вызовов"),
    ("Шестёрка", "VI", "гармония и восстановление"),
    ("Семёрка", "VII", "терпение и оценка"),
    ("Восьмёрка", "VIII", "движение и прогресс"),
    ("Девятка", "IX", "зрелость и близость к финалу"),
    ("Десятка", "X", "завершение цикла и итог"),
    ("Паж", "P", "новость и начало пути"),
    ("Рыцарь", "Kn", "активные действия и скорость"),
    ("Королева", "Q", "мудрость, интуиция и забота"),
    ("Король", "K", "мастерство и контроль"),
]

def _build_minor():
    cards = []
    for suit, s in SUITS.items():
        for rank, num, rank_theme in RANKS:
            cards.append({
                "name": f"{rank} {s['gen']}",
                "num": num,
                "symbol": s["symbol"],
                "suit": suit,
                "description": f"{rank_theme} в сфере {s['theme']}",
                "love": f"{rank_theme} в любви",
                "career": f"{rank_theme} в работе",
                "money": f"{rank_theme} в финансах",
                "future": f"{rank_theme} в будущем",
            })
    return cards

ALL_CARDS = (
    [dict(c, arcana="major") for c in MAJOR]
    + [dict(c, arcana="minor") for c in _build_minor()]
)

def detect_theme(question: str) -> str:
    q = (question or "").lower()
    if any(w in q for w in ["люб", "отношен", "парн", "муж", "жен", "свидан", "брак", "чувств", "расставан", "девушк", "парень", "влюб", "симпат"]):
        return "love"
    if any(w in q for w in ["работ", "карьер", "бизнес", "проект", "уволь", "начальник", "коллег", "собесед", "вакан", "должност", "клиент"]):
        return "career"
    if any(w in q for w in ["деньг", "финанс", "доход", "богат", "заработ", "кредит", "инвест", "зарплат"]):
        return "money"
    return "future"

POSITIONS = [
    {"name": "Прошлое и корни вопроса", "short": "Прошлое"},
    {"name": "Настоящее и суть момента", "short": "Настоящее"},
    {"name": "Будущее и вектор развития", "short": "Будущее"},
]

def interpret_card(question: str, card: dict, position_index: int) -> str:
    theme = detect_theme(question)
    desc = (card.get(theme) or card.get("description")).lower().strip()
    if desc.endswith('.'):
        desc = desc[:-1]

    if card.get("arcana") == "major":
        flavor = [
            " Это старший аркан, поэтому события имеют судьбоносный масштаб.",
            " Будучи старшим арканом, эта карта говорит о важном жизненном этапе.",
            " Это мощная энергия старшего аркана, которая задает тон всему раскладу.",
            " Карта старшего аркана — значит, речь идет о серьезных переменах."
        ]
        suffix = random.choice(flavor)
    else:
        suffix = ""

    templates = {
        0: [
            f"В основе вашей ситуации лежит карта «{card['name']}». Она указывает на то, что ранее в вашей жизни ключевую роль играло {desc}. Это тот фундамент, на котором строится текущий момент. Подумайте, как этот прошлый опыт влияет на вас сейчас.{suffix}",
            f"Корни вашего вопроса уходят в «{card['name']}». В прошлом вы столкнулись с энергией, где главенствовало {desc}. Это могло задать определенный тон или создать предпосылки для того, что происходит сегодня.{suffix}",
            f"Карта прошлого, «{card['name']}», раскрывает истоки. Ранее ваше внимание или обстоятельства были сосредоточены на том, что можно описать как {desc}. Именно этот опыт привел вас к нынешней точке.{suffix}",
            f"Погружаясь в прошлое через карту «{card['name']}», мы видим {desc}. Эта энергия уже отработала свой этап, но ее отголоски до сих пор влияют на ваши решения.{suffix}"
        ],
        1: [
            f"В настоящем перед вами раскрывается «{card['name']}». Сейчас ваша реальность пропитана энергией: {desc}. Это то, с чем вы взаимодействуете в данный момент. Постарайтесь прочувствовать, как это проявляется в вашей повседневности.{suffix}",
            f"Текущий момент представлен картой «{card['name']}». Вы находитесь в точке, где ключевым фактором становится {desc}. Обратите внимание на знаки вокруг — они могут подсказать, как лучше использовать эту энергию.{suffix}",
            f"Карта настоящего «{card['name']}» говорит о том, что сейчас для вас особенно актуально {desc}. Возможно, именно в этой сфере сосредоточены ваши главные силы и переживания.{suffix}",
            f"«{card['name']}» описывает ваше сегодня. Это состояние {desc}. Оно не случайно: именно здесь сейчас находится ваша точка роста.{suffix}"
        ],
        2: [
            f"Заглядывая в будущее, мы видим карту «{card['name']}». Вектор вашего развития направлен на {desc}. Это не предопределенность, а скорее тенденция, которая набирает силу. Будьте готовы к тому, что эта энергия станет более ощутимой.{suffix}",
            f"В будущем вас ожидает «{card['name']}». Грядущие события могут принести с собой {desc}. Это то, к чему стоит подготовиться и что может стать важным этапом на вашем пути.{suffix}",
            f"Завершающая карта «{card['name']}» приоткрывает завесу будущего. Впереди вас ждет опыт, связанный с {desc}. Помните, что будущее пластично, и ваши текущие решения формируют его.{suffix}",
            f"Энергия «{card['name']}» задает тон вашему завтра. Она говорит о {desc}. Это то, что уже начинает проявляться на горизонте, даже если вы пока этого не замечаете.{suffix}"
        ]
    }

    return random.choice(templates[position_index])


# ================== ГЕНЕРАЦИЯ ОБЩЕГО РАСКЛАДА ==================
# 5 разных сюжетных структур + рандомизация блоков = огромное разнообразие

def _descr(card, theme):
    d = (card.get(theme) or card.get("description")).lower().strip()
    if d.endswith('.'):
        d = d[:-1]
    return d


def _structure_chronological(question, theme, cards, n1, n2, n3, m1, m2, m3):
    """Классическая хронология: прошлое → настоящее → будущее."""
    openings = [
        f"Ваш вопрос «{question}» получает глубокий ответ через три карты, сложившиеся в целостную историю.",
        f"Давайте разберем расклад на вопрос «{question}». Карты выстроились в логичную последовательность.",
        f"Синтез трех арканов раскрывает ваш вопрос «{question}» с неожиданной стороны.",
        f"Этот расклад получился говорящим. Он отвечает на ваш вопрос «{question}» через развитие событий.",
    ]
    parts = [random.choice(openings)]

    mid1 = random.choice([
        f"Все начинается с карты «{n1}» — в ней заложено {m1}. Именно эта энергия стала отправной точкой вашей ситуации.",
        f"Карта «{n1}» указывает на истоки: в основе лежит {m1}. Этот опыт сформировал текущее положение вещей.",
        f"Прошлое показывает «{n1}» — здесь ключевым было {m1}. Без понимания этого фундамента картина была бы неполной.",
    ])
    parts.append(mid1)

    mid2 = random.choice([
        f"Сегодня вы находитесь под влиянием «{n2}» — это состояние {m2}. Оно напрямую связано с тем, что было раньше.",
        f"Сейчас на первый план выходит «{n2}», олицетворяющая {m2}. Именно это определяет ваши текущие переживания.",
        f"В настоящем доминирует «{n2}» — энергия {m2}. Постарайтесь прочувствовать, как она проявляется в вашей жизни.",
    ])
    parts.append(mid2)

    mid3 = random.choice([
        f"А в будущем вас ждет «{n3}» — тенденция к {m3}. Это естественное продолжение текущей линии.",
        f"Финал расклада — «{n3}», приоткрывающая тему {m3}. Именно туда ведет вас текущий вектор.",
        f"Впереди — энергия «{n3}», связанная с {m3}. Это то, к чему стоит готовиться заранее.",
    ])
    parts.append(mid3)
    return " ".join(parts)


def _structure_question_first(question, theme, cards, n1, n2, n3, m1, m2, m3):
    """Начинается с прямого ответа на вопрос, потом раскрывает карты."""
    answers = {
        "love": [
            f"Если говорить прямо о вашем вопросе «{question}», карты показывают, что в основе лежит эмоциональный опыт — {m1}. Он плавно перетекает в текущее состояние {m2}. А в перспективе вас ждет {m3}.",
            f"Отвечая на «{question}»: сейчас вы находитесь между двумя состояниями — {m1} и {m3}, а в центре находится {m2}. Именно этот переход и определяет динамику.",
        ],
        "career": [
            f"По вопросу «{question}» карты показывают карьерный путь: от {m1} через {m2} к {m3}. Это достаточно предсказуемая и логичная траектория, если не свернуть с нее.",
            f"Касательно вашей рабочей ситуации: начав с {m1}, вы пришли к {m2}, и это ведет вас к {m3}. Понимание этой связи поможет не терять ориентир.",
        ],
        "money": [
            f"На вопрос о финансах «{question}» карты отвечают так: базой служит {m1}, сейчас вы имеете дело с {m2}, а впереди — {m3}. Держите этот баланс в голове.",
            f"Ваша финансовая линия: от {m1} → к {m2} → в сторону {m3}. Именно эта последовательность отвечает на ваш вопрос.",
        ],
        "future": [
            f"Ваш вопрос «{question}» получает прямой ответ: от {m1} через {m2} события движутся к {m3}. Это основная тенденция, которую стоит учитывать.",
            f"Судя по раскладу, на вопрос «{question}» есть такой ответ: вы прошли через {m1}, находитесь в {m2}, и это ведет вас к {m3}.",
        ],
    }
    parts = [random.choice(answers[theme])]

    detail = random.choice([
        f"Обратите внимание на первую карту «{n1}»: она объясняет причину. Без ее энергии расклад был бы поверхностным.",
        f"Основание расклада — «{n1}». Это важный маркер того, откуда все началось.",
        f"Ключ к пониманию ситуации лежит в «{n1}». Она показывает исходную точку.",
    ])
    parts.append(detail)

    link = random.choice([
        f"Центральная карта — «{n2}». Она описывает то поле, в котором вы сейчас находитесь, и то, как реагировать на происходящее.",
        f"Именно «{n2}» определяет качество вашего настоящего. Это ваша точка приложения сил.",
        f"«{n2}» — сердце расклада. Она показывает, что сейчас важнее всего.",
    ])
    parts.append(link)

    closing = random.choice([
        f"И наконец «{n3}» задает направление будущего. Если вы примете это во внимание, результат будет осознанным.",
        f"«{n3}» — ваш ориентир на ближайшее время. Эта энергия уже начинает проявляться.",
        f"Будущее связано с «{n3}». Помните: это тенденция, а не приговор.",
    ])
    parts.append(closing)
    return " ".join(parts)


def _structure_philosophical(question, theme, cards, n1, n2, n3, m1, m2, m3):
    """Начинается с философской мысли, карты вплетаются в размышление."""
    openings = [
        f"Каждый расклад — это разговор с самим собой через образы. Ваш вопрос «{question}» дает повод задуматься о том, как {m1} трансформируется в {m3}.",
        f"Карты не предсказывают, они подсвечивают. И в свете вашего вопроса «{question}» мы видим путь от {m1} через {m2} к {m3}.",
        f"Когда мы задаем вопрос «{question}», вселенная отвечает через символы. И сейчас эти символы говорят о переходе от {m1} к {m3}.",
        f"Есть что-то глубоко личное в том, как раскрывается ваш вопрос «{question}». Три карты показывают внутреннюю логику: от {m1} к {m3}.",
    ]
    parts = [random.choice(openings)]

    observations = [
        f"Карта «{n1}» напоминает: все имеет свои корни. В вашем случае это {m1}. Это не просто прошлое — это опыт, который продолжает влиять на вас.",
        f"«{n2}» — это ваше настоящее зеркало. Она отражает {m2} и приглашает честно посмотреть на это состояние.",
        f"«{n3}» — горизонт, к которому вы движетесь. Там ждет {m3}. Важно помнить: горизонт приближается ровно настолько, насколько вы идете к нему.",
    ]
    random.shuffle(observations)
    parts.extend(observations[:2])
    return " ".join(parts)


def _structure_contrast(question, theme, cards, n1, n2, n3, m1, m2, m3):
    """Строится на контрастах между картами."""
    parts = [random.choice([
        f"Ваш расклад на вопрос «{question}» построен на интересном контрасте между тремя силами.",
        f"В ответ на «{question}» карты показывают переходный процесс — от одного качества к другому.",
        f"Три карты на ваш вопрос «{question}» создают напряжение между разными состояниями. Разберем его.",
    ])]

    parts.append(random.choice([
        f"С одной стороны — «{n1}» с ее энергией {m1}. Это то, что вы уже прошли или проходите.",
        f"Одна сторона вашей ситуации — «{n1}», говорящая о {m1}. Это фундамент, от которого можно оттолкнуться.",
    ]))

    parts.append(random.choice([
        f"С другой стороны — «{n3}» и ее тема {m3}. Между этими полюсами и разворачивается ваша история.",
        f"Противоположный полюс — «{n3}» с энергией {m3}. Именно в этом направлении все движется.",
    ]))

    parts.append(random.choice([
        f"«{n2}» находится в самом центре, олицетворяя {m2}. Это точка равновесия, из которой можно влиять на исход.",
        f"А «{n2}» — это та самая точка перехода. Сейчас для вас актуально {m2}. Именно здесь решается исход.",
    ]))
    return " ".join(parts)


def _structure_conversational(question, theme, cards, n1, n2, n3, m1, m2, m3):
    """Разговорный стиль, будто таролог говорит с вами напрямую."""
    parts = [random.choice([
        f"Смотрите, что показывают карты по вашему вопросу «{question}».",
        f"Давайте разложим все по полочкам. Ваш вопрос «{question}» и три карты в ответ.",
        f"Хороший расклад получился на вопрос «{question}». Вот как это можно прочитать.",
    ])]

    parts.append(random.choice([
        f"Сначала — «{n1}». Это ваш опыт: {m1}. Согласитесь, откликается?",
        f"Первая карта «{n1}» — про {m1}. Это то, что вы уже знаете на своем опыте.",
        f"«{n1}» отражает то, что с вами было: {m1}. Это важный контекст.",
    ]))

    parts.append(random.choice([
        f"Теперь «{n2}» — это про сейчас. {m2.capitalize()}. Вот в каком поле вы находитесь.",
        f"Вторая карта «{n2}» описывает ваш момент: {m2}. Именно с этим вы сейчас имеете дело.",
        f"И вот «{n2}» — это ваша реальность на сегодня: {m2}.",
    ]))

    parts.append(random.choice([
        f"И третья карта «{n3}» — это вектор. Впереди {m3}. Куда это приведет — зависит от вас.",
        f"«{n3}» показывает перспективу: {m3}. Это тенденция, к которой все идет.",
        f"Финальная карта «{n3}» — про {m3}. Такова природа ближайшего будущего.",
    ]))
    return " ".join(parts)


def _build_meta_layer(cards, theme):
    """Мета-слой о картах (масть/старшинство). Добавляется не всегда."""
    majors = [c for c in cards if c.get("arcana") == "major"]
    suits = [c["suit"] for c in cards if "suit" in c]
    blocks = []

    if len(majors) == 3:
        blocks.append("Все три карты — старшие арканы. Это редкий расклад: он говорит о том, что ситуация имеет судьбоносный характер, а не бытовой.")
    elif len(majors) == 2:
        blocks.append("Два старших аркана в раскладе подчеркивают: здесь замешаны серьезные жизненные процессы, а не сиюминутные мелочи.")
    elif len(majors) == 0 and suits:
        blocks.append("Все три карты — младшие арканы. Это хороший знак: ситуация в ваших руках, и она решается повседневными шагами.")

    if suits:
        top, cnt = Counter(suits).most_common(1)[0]
        if cnt == 3:
            blocks.append(f"Все карты принадлежат масти {top}. Ваш вопрос полностью лежит в сфере {SUITS[top]['theme']} — это и есть главная тема расклада.")
        elif cnt == 2:
            blocks.append(f"Две из трех карт относятся к масти {top}, что дополнительно акцентирует сферу {SUITS[top]['theme']}.")

    return random.choice(blocks) if blocks else ""


def _build_advice(theme):
    advice_pool = {
        "love": [
            "Совет: позвольте чувствам говорить громче страхов. Искренность — это не слабость, а сила, которая притягивает правильных людей.",
            "Совет: не пытайтесь угадать чужие мысли — говорите о своих. Честный разговор сейчас важнее любых догадок.",
            "Совет: сохраняйте личные границы, даже когда тянет раствориться в другом. Здоровая близость начинается с уважения к себе.",
            "Совет: если что-то тревожит, не держите это в себе. В открытом диалоге находится больше решений, чем в молчании.",
            "Совет: прислушайтесь к себе. Если внутри есть сомнение — это не случайно, это сигнал разобраться глубже.",
        ],
        "career": [
            "Совет: действуйте, но не торопитесь. Настойчивость без анализа приводит к ошибкам, а анализ без действий — к застою.",
            "Совет: не бойтесь просить о помощи или совете. Иногда правильный человек рядом важнее долгих самостоятельных поисков.",
            "Совет: держите фокус на главной цели и не распыляйтесь. Сейчас важно выбрать одно направление и идти в нем.",
            "Совет: документируйте свои достижения. То, что вы не замечаете как победу, другие могут увидеть как серьезный вклад.",
            "Совет: если чувствуете застой — ищите новые способы. Старые методы не всегда работают в новых обстоятельствах.",
        ],
        "money": [
            "Совет: ведите учет финансов. Даже простой список трат даст понимание, где можно сохранить ресурсы.",
            "Совет: не принимайте финансовых решений на эмоциях. Дайте себе паузу перед крупной тратой или вложением.",
            "Совет: инвестируйте в себя. Обучение и навыки сейчас надежнее любых краткосрочных вложений.",
            "Совет: пересмотрите постоянные расходы. Возможно, там есть что оптимизировать без ущерба для качества жизни.",
            "Совет: избегайте импульсивных покупок. Отложите желаемое на день и проверьте — не пропало ли желание.",
        ],
        "future": [
            "Совет: не пытайтесь контролировать всё. Будущее строится из ваших текущих шагов, а не из тревог о завтрашнем дне.",
            "Совет: доверьтесь процессу, но держите руку на руле. Пассивность и гиперконтроль одинаково плохи.",
            "Совет: составьте план, но оставьте в нем место для неожиданностей. Гибкость — ваш главный союзник сейчас.",
            "Совет: сосредоточьтесь на том, что вы можете изменить. Остальное — не в вашей власти, и это нормально.",
            "Совет: прислушайтесь к интуиции. Она часто знает ответ раньше, чем разум успевает сформулировать.",
        ],
    }
    return random.choice(advice_pool[theme])


def _build_closing():
    return random.choice([
        "Помните: расклад показывает тенденции, а не фиксированный сценарий. Ваш выбор всегда сильнее карт.",
        "Пусть это станет пищей для размышлений, а не поводом для тревоги. Вы вправе распорядиться этой информацией по своему усмотрению.",
        "Карты — это зеркало. Оно отражает то, что уже есть, но не решает за вас, что делать дальше.",
        "В любом раскладе есть пространство для маневра. Используйте его осознанно.",
        "Это лишь один из возможных взглядов на ситуацию. Ваша жизнь многограннее любого расклада.",
    ])


def interpret_overall(question: str, cards: list) -> str:
    theme = detect_theme(question)
    m1 = _descr(cards[0], theme)
    m2 = _descr(cards[1], theme)
    m3 = _descr(cards[2], theme)
    n1, n2, n3 = cards[0]["name"], cards[1]["name"], cards[2]["name"]

    # Выбираем одну из 5 сюжетных структур
    structures = [
        _structure_chronological,
        _structure_question_first,
        _structure_philosophical,
        _structure_contrast,
        _structure_conversational,
    ]
    story = random.choice(structures)(question, theme, cards, n1, n2, n3, m1, m2, m3)

    # Мета-слой (не всегда)
    meta = _build_meta_layer(cards, theme) if random.random() < 0.6 else ""

    # Совет
    advice = _build_advice(theme)

    # Финал
    closing = _build_closing()

    parts = [story]
    if meta:
        parts.append(meta)
    parts.append(advice)
    parts.append(closing)

    return " ".join(parts)


def draw_cards(n: int = 3) -> list:
    return random.sample(ALL_CARDS, n)
'''

# ============ ai_interpreter.py ============
FILES["ai_interpreter.py"] = r'''
"""Обёртка над ИИ-генерацией с fallback на локальный генератор."""
import os


def _ai_available() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))


def _ai_call(prompt: str, max_tokens: int = 500) -> str | None:
    if not _ai_available():
        return None
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": ("Ты — живой таролог с большим опытом. Ты говоришь с человеком как с другом: тепло, вдумчиво и по существу. "
                             "Ты не используешь шаблоны, клише и заезженные фразы вроде 'эта карта говорит о'. "
                             "Ты пишешь так, будто перед тобой сидит реальный человек с реальным вопросом, и ты хочешь ему искренне помочь. "
                             "Каждый ответ уникален, потому что каждый расклад — уникален. Ты не повторяешь структуру из расклада в расклад.")},
                {"role": "user", "content": prompt},
            ],
            temperature=0.95,
            max_tokens=max_tokens,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ai_interpreter] OpenAI error: {e}")
        return None


def get_card_reading(question: str, card: dict, position_index: int) -> str:
    if _ai_available():
        pos_names = ["прошлое", "настоящее", "будущее"]
        prompt = (
            f"Вопрос человека: «{question}».\n"
            f"Позиция карты: {pos_names[position_index]}.\n"
            f"Карта: «{card['name']}».\n"
            f"Значение: {card.get('description')}.\n\n"
            f"Напиши 4-5 предложений толкования этой карты именно для этого человека и его вопроса. "
            f"Говори простыми словами, по-дружески, но с глубиной. Не используй шаблонов вроде «эта карта означает». "
            f"Начни с живого наблюдения или вопроса, а не с названия карты. Закончи мыслью, которая заставит задуматься."
        )
        ai = _ai_call(prompt, max_tokens=450)
        if ai:
            return ai
            
    from tarot_data import interpret_card
    return interpret_card(question, card, position_index)


def get_overall_reading(question: str, cards: list) -> str:
    if _ai_available():
        cards_text = "\n".join(
            f"— «{c['name']}»: {c.get('description')}"
            for c in cards
        )
        prompt = (
            f"Человек задал вопрос: «{question}».\n"
            f"Выпали три карты:\n{cards_text}\n\n"
            f"Напиши общий расклад — как настоящий таролог, который сидит напротив человека и говорит с ним лично. "
            f"Это должно быть живое, связное размышление на 6-9 предложений. "
            f"Покажи, как карты складываются в единую историю именно для этого вопроса. "
            f"Ответь прямо и вдумчиво, добавь поддерживающий совет. "
            f"ВАЖНО: не используй структуру «вступление → прошлое → настоящее → будущее → совет». "
            f"Пиши свободно, как пишет живой человек, а не робот по шаблону. Каждый раз начинай по-новому."
        )
        ai = _ai_call(prompt, max_tokens=900)
        if ai:
            return ai
            
    from tarot_data import interpret_overall
    return interpret_overall(question, cards)
'''

# ============ app.py ============
FILES["app.py"] = r'''
from flask import Flask, render_template, request, jsonify
from tarot_data import draw_cards, POSITIONS
from ai_interpreter import get_card_reading, get_overall_reading

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/reading", methods=["POST"])
def reading():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()

    # Защита: пустой вопрос или только знаки препинания
    if not question or len(question) < 2 or not any(c.isalpha() for c in question):
        return jsonify({"error": "Пожалуйста, напишите ваш вопрос текстом"}), 400
    if len(question) > 500:
        question = question[:500]

    cards = draw_cards(3)

    readings = []
    for i, card in enumerate(cards):
        readings.append({
            "position": POSITIONS[i]["name"],
            "text": get_card_reading(question, card, i),
        })

    overall = get_overall_reading(question, cards)

    return jsonify({
        "question": question,
        "cards": cards,
        "readings": readings,
        "overall": overall,
    })


if __name__ == "__main__":
    app.run(debug=True)
'''

# ============ templates/index.html ============
FILES["templates/index.html"] = r'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Таро-расклад онлайн</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

    <div class="bg-layer">
        <div class="bg-mandala-1"></div>
        <div class="bg-mandala-2"></div>
        <div class="bg-smoke"></div>
    </div>

    <canvas id="particlesCanvas" aria-hidden="true"></canvas>

    <div class="container">
        <section id="questionScreen" class="screen">
            <h1>🔮 Задайте вопрос Таро</h1>
            <p class="subtitle">Три карты откроют прошлое, настоящее и будущее</p>
            
            <form id="questionForm">
                <input id="questionInput" type="text"
                       placeholder="Например: что ждёт меня в будущем?"
                       maxlength="500" autocomplete="off">
                <button type="submit">Открыть карты</button>
            </form>

            <div class="hero-images-wrapper">
                <img src="{{ url_for('static', filename='img/hero-cards.png') }}" class="hero-cards" alt="Карты Таро">
            </div>
        </section>

        <section id="loading" class="screen" style="display:none">
            <div class="spinner"></div>
            <p>Карты тасуются...</p>
        </section>

        <section id="resultScreen" class="screen" style="display:none">
            <p class="user-question">Ваш вопрос: <span id="userQuestion"></span></p>
            <div id="cards" class="cards-row"></div>
            <div id="readings" class="readings"></div>
            <button id="resetBtn" class="reset">↺ Задать новый вопрос</button>
        </section>
    </div>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
'''

# ============ static/style.css ============
FILES["static/style.css"] = r'''
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    min-height: 100vh;
    background: #0d0517; 
    color: #f3e9c7;
    display: flex;
    justify-content: center;
    padding: 40px 20px;
    position: relative;
    overflow-x: hidden;
}

.bg-layer {
    position: fixed;
    inset: 0;
    z-index: -1;
    pointer-events: none;
    background-color: #0d0517;
    isolation: isolate;
}

.bg-mandala-1 {
    position: absolute;
    inset: 0;
    background: url('/static/img/bg-mandala-1.jpg') center/cover no-repeat;
    opacity: 0.1; 
    mix-blend-mode: screen; 
}

.bg-mandala-2 {
    position: absolute;
    inset: 0;
    background: url('/static/img/bg-mandala-2.jpg') center/cover no-repeat;
    opacity: 0.35;
    mix-blend-mode: color-dodge; 
}

.bg-smoke {
    position: absolute;
    inset: 0;
    background: url('/static/img/bg-smoke.jpg') center center / cover no-repeat;
    opacity: 0.4;
    mix-blend-mode: screen;
}

#particlesCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 100;
}

.container { max-width: 900px; width: 100%; position: relative; z-index: 1; }
.screen { text-align: center; animation: fadeIn 0.5s ease; }

h1 {
    font-size: 2.4rem;
    color: #e6c869;
    text-shadow: 0 0 20px rgba(230, 200, 105, 0.4);
    margin-bottom: 10px;
}
.subtitle { color: #b8a9d4; margin-bottom: 30px; font-style: italic; }

form { display: flex; gap: 10px; max-width: 600px; margin: 0 auto; }

#questionInput {
    flex: 1;
    padding: 14px 18px;
    font-size: 1rem;
    border: 2px solid #4a2a75;
    background: rgba(26, 15, 46, 0.8);
    color: #f3e9c7;
    border-radius: 10px;
    outline: none;
    transition: border 0.2s;
}
#questionInput:focus { border-color: #e6c869; }

button {
    padding: 14px 24px;
    background: linear-gradient(135deg, #7a3eb8, #c986e8);
    color: #fff;
    border: none;
    border-radius: 10px;
    font-size: 1rem;
    cursor: pointer;
    font-weight: bold;
    transition: transform 0.2s, box-shadow 0.2s;
}
button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(201, 134, 232, 0.4);
}

.hero-images-wrapper {
    position: relative;
    width: 100%;
    max-width: 400px; 
    margin: 160px auto 40px; 
    display: flex;
    justify-content: center;
    align-items: center;
}

.hero-cards {
    width: 60%; 
    max-width: 220px;
    filter: drop-shadow(0 15px 25px rgba(0,0,0,0.6));
}

.spinner {
    width: 60px;
    height: 60px;
    margin: 40px auto 20px;
    border: 5px solid #4a2a75;
    border-top-color: #e6c869;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.user-question {
    font-size: 1.1rem;
    color: #b8a9d4;
    margin-bottom: 26px;
}
.user-question span { color: #e6c869; font-style: italic; }

.cards-row {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 30px;
    min-height: 280px;
}

.tarot-card {
    width: 190px;
    min-height: 280px;
    background: linear-gradient(160deg, #fdf6e3 0%, #e8dcc0 100%);
    border: 3px solid #e6c869;
    border-radius: 12px;
    padding: 16px 12px;
    color: #2a1147;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 8px 30px rgba(230, 200, 105, 0.25);
    transform-style: preserve-3d;
}

.card-header { font-size: 0.85rem; font-weight: bold; color: #7a3eb8; letter-spacing: 2px; }
.card-symbol { font-size: 3.2rem; margin: 10px 0; }
.card-name { font-size: 1rem; font-weight: bold; text-align: center; color: #2a1147; margin-bottom: 8px; }
.card-desc { font-size: 0.82rem; text-align: center; color: #4a2a75; font-style: italic; }

.readings {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-bottom: 30px;
}

.card-reading {
    background: rgba(30, 15, 55, 0.85); 
    border: 1px solid #4a2a75;
    border-left: 4px solid #e6c869;
    border-radius: 12px;
    padding: 18px 22px;
    text-align: left;
    line-height: 1.7;
    font-size: 1.02rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}

.reading-position {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #e6c869;
    margin-bottom: 8px;
    font-weight: bold;
}

.overall {
    background: linear-gradient(135deg, rgba(60, 30, 100, 0.9), rgba(30, 15, 55, 0.9));
    border: 2px solid #e6c869;
    border-radius: 14px;
    padding: 24px 26px;
    text-align: left;
    line-height: 1.75;
    font-size: 1.05rem;
    box-shadow: 0 10px 40px rgba(230, 200, 105, 0.2);
    margin-top: 10px;
}

.overall h2 { color: #e6c869; font-size: 1.2rem; margin-bottom: 12px; text-align: center; letter-spacing: 1px; }

.reset { background: transparent; border: 2px solid #7a3eb8; color: #c986e8; margin-top: 10px; }
.reset:hover { background: #7a3eb8; color: #fff; }

@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

@media (max-width: 640px) {
    h1 { font-size: 1.7rem; }
    form { flex-direction: column; }
    .hero-images-wrapper { max-width: 300px; margin-top: 120px; } 
    .tarot-card { width: 150px; min-height: 230px; }
    .card-symbol { font-size: 2.4rem; }
    .cards-row { gap: 10px; min-height: auto; }
}
'''

# ============ static/script.js ============
FILES["static/script.js"] = r'''
const form = document.getElementById('questionForm');
const questionInput = document.getElementById('questionInput');
const questionScreen = document.getElementById('questionScreen');
const loading = document.getElementById('loading');
const resultScreen = document.getElementById('resultScreen');
const userQuestion = document.getElementById('userQuestion');
const cardsRow = document.getElementById('cards');
const readingsList = document.getElementById('readings');
const resetBtn = document.getElementById('resetBtn');

const delay = (ms) => new Promise((r) => setTimeout(r, ms));

/* ============ PARTICLE SYSTEM ============ */
const canvas = document.getElementById('particlesCanvas');
const ctx = canvas.getContext('2d');
let particles = [];
let animationId = null;

function resizeCanvas() {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = window.innerWidth * dpr;
    canvas.height = window.innerHeight * dpr;
    canvas.style.width = window.innerWidth + 'px';
    canvas.style.height = window.innerHeight + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const PARTICLE_COLORS = [
    '#e6c869', '#ffd700', '#c986e8', '#a56ee8', '#f3e9c7', '#ffffff'
];

function spawnBurst(x, y, count = 45) {
    for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = 1.5 + Math.random() * 5.5;
        particles.push({
            x, y,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed - 2,
            gravity: 0.06 + Math.random() * 0.08,
            friction: 0.985,
            life: 1,
            decay: 0.008 + Math.random() * 0.018,
            size: 1.5 + Math.random() * 3.5,
            color: PARTICLE_COLORS[Math.floor(Math.random() * PARTICLE_COLORS.length)],
            isStar: Math.random() < 0.3,
            rotation: Math.random() * Math.PI,
            rotSpeed: (Math.random() - 0.5) * 0.2,
        });
    }
    if (!animationId) animateParticles();
}

function drawStar(cx, cy, spikes, outerR, innerR, rotation) {
    let rot = rotation;
    let x = cx, y = cy;
    const step = Math.PI / spikes;
    ctx.beginPath();
    ctx.moveTo(cx + Math.cos(rot) * outerR, cy + Math.sin(rot) * outerR);
    for (let i = 0; i < spikes; i++) {
        rot += step;
        x = cx + Math.cos(rot) * innerR;
        y = cy + Math.sin(rot) * innerR;
        ctx.lineTo(x, y);
        rot += step;
        x = cx + Math.cos(rot) * outerR;
        y = cy + Math.sin(rot) * outerR;
        ctx.lineTo(x, y);
    }
    ctx.closePath();
    ctx.fill();
}

function animateParticles() {
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx; p.y += p.vy;
        p.vy += p.gravity;
        p.vx *= p.friction; p.vy *= p.friction;
        p.rotation += p.rotSpeed;
        p.life -= p.decay;
        if (p.life <= 0 || p.y > window.innerHeight + 80) {
            particles.splice(i, 1); continue;
        }
        ctx.globalAlpha = Math.max(0, p.life);
        ctx.fillStyle = p.color;
        ctx.shadowBlur = 10;
        ctx.shadowColor = p.color;
        const size = p.size * p.life;
        if (p.isStar) {
            drawStar(p.x, p.y, 4, size * 1.6, size * 0.6, p.rotation);
        } else {
            ctx.beginPath();
            ctx.arc(p.x, p.y, size, 0, Math.PI * 2);
            ctx.fill();
        }
    }
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
    if (particles.length > 0) {
        animationId = requestAnimationFrame(animateParticles);
    } else {
        animationId = null;
        ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    }
}

function getElementCenter(el) {
    const rect = el.getBoundingClientRect();
    return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
}

/* ============ DOM HELPERS ============ */
function makeCardEl(card) {
    const el = document.createElement('div');
    el.className = 'tarot-card';
    el.style.opacity = '0';
    el.style.transform = 'translateY(-30px) rotateY(90deg)';
    el.innerHTML =
        '<div class="card-header">' + card.num + '</div>' +
        '<div class="card-symbol">' + card.symbol + '</div>' +
        '<div class="card-name">' + card.name + '</div>' +
        '<div class="card-desc">' + card.description + '</div>';
    return el;
}

function makeReadingEl(reading, card) {
    const el = document.createElement('div');
    el.className = 'card-reading';
    el.style.opacity = '0';
    el.innerHTML =
        '<div class="reading-position">' + reading.position +
        ' — «' + card.name + '»</div>' +
        '<div class="reading-text">' + reading.text + '</div>';
    return el;
}

function makeOverallEl(text) {
    const el = document.createElement('div');
    el.className = 'overall';
    el.style.opacity = '0';
    el.innerHTML =
        '<h2>✨ Общий расклад</h2>' +
        '<div class="reading-text">' + text + '</div>';
    return el;
}

/* ============ REVEAL ============ */
async function revealAll(data) {
    cardsRow.innerHTML = '';
    readingsList.innerHTML = '';
    particles = [];

    for (let i = 0; i < data.cards.length; i++) {
        const card = data.cards[i];
        const reading = data.readings[i];

        const cardEl = makeCardEl(card);
        cardsRow.appendChild(cardEl);
        await delay(20);

        const center = getElementCenter(cardEl);
        spawnBurst(center.x, center.y, 55);

        cardEl.style.transition = 'opacity 0.5s ease, transform 0.75s cubic-bezier(0.2, 0.8, 0.3, 1.2)';
        cardEl.style.opacity = '1';
        cardEl.style.transform = 'translateY(0) rotateY(0)';

        setTimeout(() => {
            const c = getElementCenter(cardEl);
            spawnBurst(c.x, c.y, 25);
        }, 380);

        await delay(750);

        const c2 = getElementCenter(cardEl);
        spawnBurst(c2.x, c2.y, 18);

        const readingEl = makeReadingEl(reading, card);
        readingsList.appendChild(readingEl);
        readingEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        await delay(20);
        readingEl.style.transition = 'opacity 0.8s ease';
        readingEl.style.opacity = '1';

        await delay(1100);
    }

    const overallEl = makeOverallEl(data.overall);
    readingsList.appendChild(overallEl);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    await delay(20);
    overallEl.style.transition = 'opacity 1s ease';
    overallEl.style.opacity = '1';

    const oc = getElementCenter(overallEl);
    setTimeout(() => {
        spawnBurst(oc.x, oc.y - 30, 90);
        setTimeout(() => spawnBurst(oc.x - 120, oc.y, 40), 180);
        setTimeout(() => spawnBurst(oc.x + 120, oc.y, 40), 360);
    }, 250);

    await delay(600);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/* ============ SUBMIT / RESET ============ */
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const question = questionInput.value.trim();

    // Клиентская проверка: не пустой и содержит хотя бы одну букву
    if (!question || question.length < 2 || !/[а-яА-Яa-zA-Z]/.test(question)) {
        alert('Пожалуйста, напишите ваш вопрос текстом');
        questionInput.focus();
        return;
    }

    questionScreen.style.display = 'none';
    resultScreen.style.display = 'none';
    loading.style.display = 'block';

    try {
        const res = await fetch('/api/reading', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || 'Ошибка сервера');

        userQuestion.textContent = '«' + question + '»';
        loading.style.display = 'none';
        resultScreen.style.display = 'block';
        window.scrollTo({ top: 0, behavior: 'smooth' });

        await revealAll(data);
    } catch (err) {
        alert('Ошибка: ' + err.message);
        loading.style.display = 'none';
        questionScreen.style.display = 'block';
    }
});

resetBtn.addEventListener('click', () => {
    resultScreen.style.display = 'none';
    questionScreen.style.display = 'block';
    cardsRow.innerHTML = '';
    readingsList.innerHTML = '';
    particles = [];
    questionInput.value = '';
    questionInput.focus();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
'''

# ============ requirements.txt ============
FILES["requirements.txt"] = r'''
Flask==3.0.3
openai>=1.40.0
gunicorn==21.2.0
'''

# ============ Запись ============
for path, content in FILES.items():
    full = os.path.join(BASE, path)
    parent = os.path.dirname(full)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content.lstrip("\n"))
    print(f"[OK] {path}")

print("\n========================================")
print("✅ Все файлы обновлены (Общий расклад — 5 сюжетных структур).")
print("Запускай: python setup.py -> python app.py")
print("========================================")