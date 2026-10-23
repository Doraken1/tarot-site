"""
Создаёт все файлы проекта Таро с анимацией частиц.
Запуск: python setup.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = {}

# ============ tarot_data.py ============
FILES["tarot_data.py"] = r'''
"""78 карт Таро + локальный генератор толкований."""
import random
import hashlib
from collections import Counter

MAJOR = [
    {"name": "Шут", "num": "0", "symbol": "🃏",
     "description": "Новое начало, спонтанность, прыжок в неизвестность.",
     "love": "свежесть чувств, новые знакомства, лёгкость, отсутствие привязанностей",
     "career": "начало нового пути, готовность рискнуть, нестандартный ход",
     "money": "нестабильность, но неожиданные возможности и лёгкие деньги",
     "future": "впереди новое и неизвестное, потребуется доверие к жизни"},
    {"name": "Маг", "num": "I", "symbol": "🎩",
     "description": "Воля, мастерство, проявление намерения в реальность.",
     "love": "умение привлечь, активная позиция, осознанный выбор партнёра",
     "career": "успех через инициативу, таланты и умение говорить",
     "money": "предприимчивость, умение зарабатывать своими идеями",
     "future": "вы способны управлять событиями через собственные действия"},
    {"name": "Верховная Жрица", "num": "II", "symbol": "🌙",
     "description": "Интуиция, тайна, скрытые знания, доверие внутреннему голосу.",
     "love": "глубокие, но скрытые чувства, недосказанность, интуитивное понимание",
     "career": "не всё очевидно, важные сведения скрыты, доверьтесь интуиции",
     "money": "скрытые факторы, осторожность, не все обстоятельства видны",
     "future": "многое пока скрыто — прислушайтесь к внутреннему голосу"},
    {"name": "Императрица", "num": "III", "symbol": "🌸",
     "description": "Плодородие, творчество, забота, изобилие.",
     "love": "тёплые, заботливые отношения, возможен рост семьи",
     "career": "творческий рост, плодотворный период, признание таланта",
     "money": "изобилие, доходы растут, ресурсы приумножаются",
     "future": "плодотворный период, воплощение задуманного"},
    {"name": "Император", "num": "IV", "symbol": "👑",
     "description": "Структура, власть, порядок, авторитет.",
     "love": "стабильные отношения, возможен контроль со стороны партнёра",
     "career": "успех через дисциплину, структуру и ответственность",
     "money": "стабильность, финансовый контроль, порядок в делах",
     "future": "порядок и стабильность, важно взять ситуацию в свои руки"},
    {"name": "Иерофант", "num": "V", "symbol": "📿",
     "description": "Традиции, обучение, духовный наставник.",
     "love": "традиционные отношения, серьёзные намерения, брак",
     "career": "работа в структуре, обучение, наставник, проверенный путь",
     "money": "традиционные методы, стабильность, проверенные схемы",
     "future": "уроки и обучение, важно опереться на опыт"},
    {"name": "Влюблённые", "num": "VI", "symbol": "💕",
     "description": "Выбор, любовь, гармония, союз.",
     "love": "взаимные чувства, важный выбор, единство сердец",
     "career": "удачное партнёрство, союз с единомышленником",
     "money": "совместные финансы, доход в паре",
     "future": "важный выбор и партнёрство, на развилке решает сердце"},
    {"name": "Колесница", "num": "VII", "symbol": "🏇",
     "description": "Победа, движение, контроль над ситуацией.",
     "love": "активное развитие, победа над препятствиями",
     "career": "успех через настойчивость и дисциплину",
     "money": "рост через действие, доход от активности",
     "future": "победа и движение вперёд, важно не сворачивать"},
    {"name": "Сила", "num": "VIII", "symbol": "🦁",
     "description": "Внутренняя сила, терпение, мягкая мощь.",
     "love": "гармония через терпение, зрелые чувства",
     "career": "успех через выдержку и мягкую настойчивость",
     "money": "равновесие через терпение, избегайте импульсов",
     "future": "вы справитесь, внутренней силы достаточно"},
    {"name": "Отшельник", "num": "IX", "symbol": "🕯️",
     "description": "Уединение, поиск истины, внутренний свет.",
     "love": "период осмысления отношений, потребность в личном пространстве",
     "career": "время подумать, уединённая работа, внутренний поиск",
     "money": "скромность, экономия, разумные ограничения",
     "future": "время осмысления, ответ внутри, а не снаружи"},
    {"name": "Колесо Фортуны", "num": "X", "symbol": "🎡",
     "description": "Судьба, перемены, циклы, удача.",
     "love": "перемены в отношениях, поворот судьбы",
     "career": "удачный поворот, неожиданное везение",
     "money": "возможно везение, но и перемены",
     "future": "судьба готовит перемены, колесо поворачивается"},
    {"name": "Справедливость", "num": "XI", "symbol": "⚖️",
     "description": "Правда, баланс, закон, справедливость.",
     "love": "честные, равные отношения, ясность",
     "career": "признание по заслугам, справедливая оценка",
     "money": "справедливые доходы, законные схемы",
     "future": "всё будет по справедливости, по заслугам"},
    {"name": "Повешенный", "num": "XII", "symbol": "🙃",
     "description": "Остановка, жертва, взгляд под другим углом.",
     "love": "пауза, ожидание, готовность пересмотреть чувства",
     "career": "задержка — время переосмыслить подход",
     "money": "пауза в делах, временная жертва ради будущего",
     "future": "время переосмыслить, взгляните иначе"},
    {"name": "Смерть", "num": "XIII", "symbol": "💀",
     "description": "Конец цикла, трансформация, перерождение.",
     "love": "завершение или глубокая трансформация отношений",
     "career": "конец этапа — начало нового, отпустите старое",
     "money": "крупные перемены в финансах, обновление",
     "future": "конец одного этапа, начало другого"},
    {"name": "Умеренность", "num": "XIV", "symbol": "🍷",
     "description": "Баланс, гармония, терпение, алхимия.",
     "love": "гармоничные отношения, баланс, мягкое течение",
     "career": "стабильный прогресс, важно не спешить",
     "money": "умеренность в тратах, баланс доходов и расходов",
     "future": "гармония и баланс, золотая середина"},
    {"name": "Дьявол", "num": "XV", "symbol": "😈",
     "description": "Искушение, зависимость, материальные узы.",
     "love": "страсть, но риск зависимости, привязанность",
     "career": "материальная выгода, осторожно с этикой и манипуляциями",
     "money": "соблазн лёгких денег, кредиты, зависимости",
     "future": "остерегайтесь искушений, посмотрите на свои цепи"},
    {"name": "Башня", "num": "XVI", "symbol": "🗼",
     "description": "Крушение, внезапные перемены, разрушение старого.",
     "love": "возможен разрыв, кризис, шок — но очищающий",
     "career": "внезапные перемены, обрушение старых планов",
     "money": "финансовые потрясения, срочная перестройка",
     "future": "внезапные события всё изменят, освобождение"},
    {"name": "Звезда", "num": "XVII", "symbol": "⭐",
     "description": "Надежда, вдохновение, исцеление, свет.",
     "love": "светлые надежды, чистота чувств, исцеление",
     "career": "вдохновение, светлая полоса, признание",
     "money": "улучшение, надежда, свет в конце тоннеля",
     "future": "светлая полоса, надежда оправдывается"},
    {"name": "Луна", "num": "XVIII", "symbol": "🌕",
     "description": "Иллюзии, страхи, подсознание, неясность.",
     "love": "неясность, страхи, сомнения, возможно скрытое",
     "career": "будьте осторожны, многое не то, чем кажется",
     "money": "скрытые риски, туманные схемы",
     "future": "многое неясно — доверьтесь интуиции, подождите"},
    {"name": "Солнце", "num": "XIX", "symbol": "☀️",
     "description": "Радость, успех, ясность, победа.",
     "love": "яркие, радостные отношения, взаимность",
     "career": "успех, признание, ясные цели",
     "money": "достаток, успех, изобилие",
     "future": "светлый период, всё прояснится"},
    {"name": "Суд", "num": "XX", "symbol": "📯",
     "description": "Возрождение, важный этап, пробуждение.",
     "love": "возвращение чувств, важное решение в отношениях",
     "career": "новые возможности, призвание зовёт",
     "money": "возрождение финансов, второй шанс",
     "future": "важный этап, возрождение, зов"},
    {"name": "Мир", "num": "XXI", "symbol": "🌍",
     "description": "Завершение, целостность, успех, гармония.",
     "love": "гармония, полнота чувств, зрелый союз",
     "career": "завершение проекта, успех, признание",
     "money": "финансовое благополучие, устойчивость",
     "future": "успешное завершение, целостность, награда"},
]

SUITS = {
    "Жезлы": {"symbol": "🪄", "gen": "Жезлов",
              "theme": "страсть, действие, творчество, энергия"},
    "Кубки": {"symbol": "🏆", "gen": "Кубков",
              "theme": "эмоции, чувства, отношения, интуиция"},
    "Мечи": {"symbol": "⚔️", "gen": "Мечей",
             "theme": "разум, правда, конфликты, решения"},
    "Пентакли": {"symbol": "🪙", "gen": "Пентаклей",
                 "theme": "деньги, стабильность, материя, результат"},
}

RANKS = [
    ("Туз", "A", "начало, семя, потенциал, шанс"),
    ("Двойка", "II", "баланс, партнёрство, выбор"),
    ("Тройка", "III", "рост, творчество, первые результаты"),
    ("Четвёрка", "IV", "стабильность, структура, основа"),
    ("Пятёрка", "V", "конфликт, потери, вызов"),
    ("Шестёрка", "VI", "гармония, восстановление, помощь"),
    ("Семёрка", "VII", "оценка, терпение, испытание"),
    ("Восьмёрка", "VIII", "движение, мастерство, прогресс"),
    ("Девятка", "IX", "почти финал, зрелость"),
    ("Десятка", "X", "завершение, итог, пик цикла"),
    ("Паж", "P", "новость, ученик, начало пути"),
    ("Рыцарь", "Kn", "действие, движение, скорость"),
    ("Королева", "Q", "зрелость, интуиция, забота"),
    ("Король", "K", "мастерство, власть, контроль"),
]

def _build_minor():
    cards = []
    for suit, s in SUITS.items():
        for rank, num, theme in RANKS:
            cards.append({
                "name": f"{rank} {s['gen']}",
                "num": num,
                "symbol": s["symbol"],
                "suit": suit,
                "description": f"{theme.capitalize()}. Сфера: {s['theme']}.",
                "love": f"{theme} — в любви это проявления {s['theme']}",
                "career": f"{theme} — в работе это касается {s['theme']}",
                "money": f"{theme} — в финансах это {s['theme']}",
                "future": f"{theme} — в будущем это {s['theme']}",
            })
    return cards

ALL_CARDS = (
    [dict(c, arcana="major") for c in MAJOR]
    + [dict(c, arcana="minor") for c in _build_minor()]
)

def detect_theme(question: str) -> str:
    q = (question or "").lower()
    if any(w in q for w in ["люб", "отношен", "парн", "муж", "жен",
                             "свидан", "брак", "чувств", "расставан",
                             "девушк", "парень", "влюб", "симпат"]):
        return "love"
    if any(w in q for w in ["работ", "карьер", "бизнес", "проект",
                             "уволь", "начальник", "коллег", "собесед",
                             "вакан", "должност", "клиент"]):
        return "career"
    if any(w in q for w in ["деньг", "финанс", "доход", "богат",
                             "заработ", "кредит", "инвест", "зарплат"]):
        return "money"
    return "future"

POSITIONS = [
    {"name": "Прошлое и корни вопроса", "short": "Прошлое"},
    {"name": "Настоящее и суть момента", "short": "Настоящее"},
    {"name": "Будущее и вектор развития", "short": "Будущее"},
]

def _hash_idx(*args, size):
    s = "|".join(str(a) for a in args)
    return int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16) % size

_OPENERS = {
    0: [
        "Открывая первую карту, «{name}», мы видим истоки вашего вопроса.",
        "Первая карта, «{name}», показывает корни вашей ситуации.",
        "Первой выходит карта «{name}» — она рассказывает о начале вашего вопроса.",
    ],
    1: [
        "Вторая карта, «{name}», отражает настоящее — то, что происходит сейчас.",
        "Открывая вторую карту, «{name}», мы видим текущий момент.",
        "Вторая карта, «{name}», показывает, что сейчас определяет ситуацию.",
    ],
    2: [
        "Третья карта, «{name}», приоткрывает будущее — вектор развития.",
        "Завершающая карта, «{name}», говорит, куда ведёт текущее развитие.",
        "Третья карта, «{name}», показывает перспективу.",
    ],
}

_CLOSERS = {
    0: {
        "love": "Это эмоциональный или событийный багаж, с которым вы вошли в текущие отношения.",
        "career": "Это профессиональный опыт и обстоятельства, приведшие вас к нынешней точке.",
        "money": "Это финансовая основа — то, на чём выстроено ваше текущее положение.",
        "future": "Это причина, из которой произрастает ваше будущее.",
    },
    1: {
        "love": "Сейчас важно услышать, что эта энергия говорит о ваших чувствах и партнёре.",
        "career": "Эта энергия определяет ваши рабочие обстоятельства — используйте её осознанно.",
        "money": "Обратите внимание, как эта энергия проявляется в доходах и тратах.",
        "future": "Это точка, из которой формируется ваше завтра.",
    },
    2: {
        "love": "Такой видится перспектива отношений, если ничего не менять сознательно.",
        "career": "Таков вероятный вектор карьерного развития при текущем движении.",
        "money": "Такой прогноз по финансам — это тенденция, а не приговор.",
        "future": "Это тенденция, а не приговор: осознанность меняет исход.",
    },
}

def interpret_card(question: str, card: dict, position_index: int) -> str:
    theme = detect_theme(question)
    meaning = card.get(theme) or card.get("description")
    opener = _OPENERS[position_index][
        _hash_idx(question, card["name"], position_index,
                  size=len(_OPENERS[position_index]))
    ].format(name=card["name"])
    core = f"Её значение — {meaning}."
    closer = _CLOSERS[position_index][theme]
    extra = ""
    if card.get("arcana") == "major":
        extra = (" Это старший аркан, поэтому энергия карты сильная "
                 "и судьбоносная — событие имеет вес.")
    return f"{opener} {core}{extra} {closer}"


def interpret_overall(question: str, cards: list) -> str:
    theme = detect_theme(question)
    majors = [c for c in cards if c.get("arcana") == "major"]
    suits = [c["suit"] for c in cards if "suit" in c]
    parts = []

    parts.append(
        f"Собрав три карты вместе, мы видим целостную картину по вашему "
        f"вопросу — «{question}»."
    )

    if len(majors) == 3:
        parts.append(
            "Все три карты — старшие арканы. Это знак судьбоносного периода: "
            "события разворачиваются по крупному сценарию."
        )
    elif len(majors) == 2:
        parts.append(
            "Две карты из трёх — старшие арканы. В вашей ситуации больше "
            "судьбы, чем случая: происходящее важно."
        )
    else:
        parts.append(
            "Преобладание младших арканов означает, что исход во многом "
            "в ваших руках: ситуация складывается из повседневных действий."
        )

    if suits:
        top, cnt = Counter(suits).most_common(1)[0]
        if cnt == 3:
            parts.append(
                f"Все три карты относятся к масти {top} — весь расклад "
                f"вращается вокруг темы: {SUITS[top]['theme']}."
            )
        elif cnt == 2:
            parts.append(
                f"Две карты из трёх — масти {top}, что подчёркивает "
                f"важность сферы {SUITS[top]['theme']}."
            )

    names = " → ".join(f"«{c['name']}»" for c in cards)
    parts.append(
        f"Путь карт: {names}. Расклад показывает связную линию развития "
        f"от истоков через текущий момент к будущему."
    )

    advice = {
        "love": ("Главный совет: прислушайтесь к чувствам и не бойтесь "
                 "открыто говорить о них. Отношения требуют честности "
                 "и мягкости одновременно."),
        "career": ("Главный совет: действуйте решительно, но с расчётом. "
                   "Ситуация требует инициативы, но и внимания к деталям."),
        "money": ("Главный совет: будьте внимательны к финансам, избегайте "
                  "импульсивных трат, но не бойтесь возможностей."),
        "future": ("Главный совет: доверьтесь потоку событий, но не будьте "
                   "пассивны. Будущее формируется сейчас."),
    }[theme]
    parts.append(advice)
    parts.append(
        "Помните: карты показывают тенденции, а не приговор. "
        "Осознанный выбор всегда может повернуть события."
    )
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


def _ai_call(prompt: str, max_tokens: int = 400) -> str | None:
    if not _ai_available():
        return None
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": ("Ты — опытный таролог. Отвечай по-русски, "
                             "тёплым доверительным тоном, без клише. "
                             "Пиши связным текстом, обращаясь к пользователю.")},
                {"role": "user", "content": prompt},
            ],
            temperature=0.85,
            max_tokens=max_tokens,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ai_interpreter] OpenAI error: {e}")
        return None


def get_card_reading(question: str, card: dict, position_index: int) -> str:
    if _ai_available():
        pos_names = [
            "прошлое и корни вопроса",
            "настоящее и суть момента",
            "будущее и вектор развития",
        ]
        prompt = (
            f"Вопрос пользователя: «{question}».\n"
            f"Позиция в раскладе: {pos_names[position_index]}.\n"
            f"Выпавшая карта: «{card['name']}».\n"
            f"Краткое значение: {card.get('description')}\n\n"
            f"Напиши развёрнутое толкование этой одной карты "
            f"применительно к вопросу пользователя (4–6 предложений). "
            f"Свяжи значение карты с позицией и с самим вопросом. "
            f"Говори только об этой карте."
        )
        ai = _ai_call(prompt, max_tokens=350)
        if ai:
            return ai
    from tarot_data import interpret_card
    return interpret_card(question, card, position_index)


def get_overall_reading(question: str, cards: list) -> str:
    if _ai_available():
        cards_text = "\n".join(
            f"{i + 1}. «{c['name']}» — {c.get('description')}"
            for i, c in enumerate(cards)
        )
        prompt = (
            f"Вопрос пользователя: «{question}».\n"
            f"Выпали три карты Таро:\n{cards_text}\n\n"
            f"Напиши общий синтез-расклад (6–9 предложений):\n"
            f"1. Свяжи все три карты в единую линию развития;\n"
            f"2. Прямо ответь на заданный вопрос;\n"
            f"3. Дай мягкий, но конкретный совет.\n"
            f"Пиши связным текстом, обращаясь на «вы»."
        )
        ai = _ai_call(prompt, max_tokens=600)
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

    if not question:
        return jsonify({"error": "Введите вопрос"}), 400
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
    background: radial-gradient(ellipse at top, #2a1147 0%, #0d0517 70%);
    color: #f3e9c7;
    display: flex;
    justify-content: center;
    padding: 40px 20px;
}

/* ===== Canvas для частиц ===== */
#particlesCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 100;
}

.container { max-width: 900px; width: 100%; }
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
    background: #1a0f2e;
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

.card-header {
    font-size: 0.85rem;
    font-weight: bold;
    color: #7a3eb8;
    letter-spacing: 2px;
}
.card-symbol { font-size: 3.2rem; margin: 10px 0; }
.card-name {
    font-size: 1rem;
    font-weight: bold;
    text-align: center;
    color: #2a1147;
    margin-bottom: 8px;
}
.card-desc {
    font-size: 0.82rem;
    text-align: center;
    color: #4a2a75;
    font-style: italic;
}

.readings {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-bottom: 30px;
}

.card-reading {
    background: rgba(30, 15, 55, 0.75);
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
    background: linear-gradient(135deg,
                rgba(60, 30, 100, 0.85),
                rgba(30, 15, 55, 0.85));
    border: 2px solid #e6c869;
    border-radius: 14px;
    padding: 24px 26px;
    text-align: left;
    line-height: 1.75;
    font-size: 1.05rem;
    box-shadow: 0 10px 40px rgba(230, 200, 105, 0.2);
    margin-top: 10px;
}

.overall h2 {
    color: #e6c869;
    font-size: 1.2rem;
    margin-bottom: 12px;
    text-align: center;
    letter-spacing: 1px;
}

.reset {
    background: transparent;
    border: 2px solid #7a3eb8;
    color: #c986e8;
    margin-top: 10px;
}
.reset:hover { background: #7a3eb8; color: #fff; }

@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

@media (max-width: 640px) {
    h1 { font-size: 1.7rem; }
    form { flex-direction: column; }
    .tarot-card { width: 150px; min-height: 230px; }
    .card-symbol { font-size: 2.4rem; }
    .cards-row { gap: 10px; min-height: auto; }
}
'''

# ============ static/script.js ============
FILES["static/script.js"] = r'''
/* ============================================================
   DOM
   ============================================================ */
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


/* ============================================================
   PARTICLE SYSTEM
   ============================================================ */
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
    let x = cx;
    let y = cy;
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
        p.x += p.vx;
        p.y += p.vy;
        p.vy += p.gravity;
        p.vx *= p.friction;
        p.vy *= p.friction;
        p.rotation += p.rotSpeed;
        p.life -= p.decay;

        if (p.life <= 0 || p.y > window.innerHeight + 80) {
            particles.splice(i, 1);
            continue;
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


/* ============================================================
   DOM HELPERS
   ============================================================ */
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


/* ============================================================
   REVEAL — пошаговое открытие карт + частицы
   ============================================================ */
async function revealAll(data) {
    cardsRow.innerHTML = '';
    readingsList.innerHTML = '';
    particles = [];   // сброс на всякий случай

    for (let i = 0; i < data.cards.length; i++) {
        const card = data.cards[i];
        const reading = data.readings[i];

        // 1. Карта появляется (пока ещё "рубашкой" — поворот 90°)
        const cardEl = makeCardEl(card);
        cardsRow.appendChild(cardEl);
        await delay(20);

        const center = getElementCenter(cardEl);

        // 2. Взрыв частиц — момент появления
        spawnBurst(center.x, center.y, 55);

        // 3. Запускаем переворот
        cardEl.style.transition = 'opacity 0.5s ease, transform 0.75s cubic-bezier(0.2, 0.8, 0.3, 1.2)';
        cardEl.style.opacity = '1';
        cardEl.style.transform = 'translateY(0) rotateY(0)';

        // 4. Промежуточный искристый "щелчок" в середине переворота
        setTimeout(() => {
            const c = getElementCenter(cardEl);
            spawnBurst(c.x, c.y, 25);
        }, 380);

        await delay(750);

        // 5. Финальный "оседающий" бурст после переворота
        const c2 = getElementCenter(cardEl);
        spawnBurst(c2.x, c2.y, 18);

        // 6. Появление толкования
        const readingEl = makeReadingEl(reading, card);
        readingsList.appendChild(readingEl);
        readingEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        await delay(20);
        readingEl.style.transition = 'opacity 0.8s ease';
        readingEl.style.opacity = '1';

        await delay(1100);
    }

    // 7. Общий расклад
    const overallEl = makeOverallEl(data.overall);
    readingsList.appendChild(overallEl);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    await delay(20);
    overallEl.style.transition = 'opacity 1s ease';
    overallEl.style.opacity = '1';

    // 8. Большой праздничный бурст над общим раскладом
    const oc = getElementCenter(overallEl);
    setTimeout(() => {
        spawnBurst(oc.x, oc.y - 30, 90);
        setTimeout(() => spawnBurst(oc.x - 120, oc.y, 40), 180);
        setTimeout(() => spawnBurst(oc.x + 120, oc.y, 40), 360);
    }, 250);

    await delay(600);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
}


/* ============================================================
   SUBMIT / RESET
   ============================================================ */
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const question = questionInput.value.trim();
    if (!question) {
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
print("✅ Все файлы созданы (с частицами).")
print("Запускай: python app.py")
print("========================================")