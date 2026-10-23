"""
Создаёт все файлы проекта Таро. Обновлен генератор ИИ (вдумчивые, связные ответы).
Запуск: python setup.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = {}

# ============ tarot_data.py ============
FILES["tarot_data.py"] = r'''
"""78 карт Таро + локальный генератор глубоких толкований."""
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
            " Это мощная энергия старшего аркана, которая задает тон всему раскладу."
        ]
        suffix = random.choice(flavor)
    else:
        suffix = ""

    templates = {
        0: [
            f"В основе вашей ситуации лежит карта «{card['name']}». Она указывает на то, что ранее в вашей жизни ключевую роль играло {desc}. Это тот фундамент, на котором строится текущий момент. Подумайте, как этот прошлый опыт влияет на вас сейчас.{suffix}",
            f"Корни вашего вопроса уходят в «{card['name']}». В прошлом вы столкнулись с энергией, где главенствовало {desc}. Это могло задать определенный тон или создать предпосылки для того, что происходит сегодня.{suffix}",
            f"Карта прошлого, «{card['name']}», раскрывает истоки. Ранее ваше внимание или обстоятельства были сосредоточены на том, что можно описать как {desc}. Именно этот опыт привел вас к нынешней точке.{suffix}"
        ],
        1: [
            f"В настоящем перед вами раскрывается «{card['name']}». Сейчас ваша реальность пропитана энергией: {desc}. Это то, с чем вы взаимодействуете в данный момент. Постарайтесь прочувствовать, как это проявляется в вашей повседневности.{suffix}",
            f"Текущий момент представлен картой «{card['name']}». Вы находитесь в точке, где ключевым фактором становится {desc}. Обратите внимание на знаки вокруг — они могут подсказать, как лучше использовать эту энергию.{suffix}",
            f"Карта настоящего «{card['name']}» говорит о том, что сейчас для вас особенно актуально {desc}. Возможно, именно в этой сфере сосредоточены ваши главные силы и переживания.{suffix}"
        ],
        2: [
            f"Заглядывая в будущее, мы видим карту «{card['name']}». Вектор вашего развития направлен на {desc}. Это не предопределенность, а скорее тенденция, которая набирает силу. Будьте готовы к тому, что эта энергия станет более ощутимой.{suffix}",
            f"В будущем вас ожидает «{card['name']}». Грядущие события могут принести с собой {desc}. Это то, к чему стоит подготовиться и что может стать важным этапом на вашем пути.{suffix}",
            f"Завершающая карта «{card['name']}» приоткрывает завесу будущего. Впереди вас ждет опыт, связанный с {desc}. Помните, что будущее пластично, и ваши текущие решения формируют его.{suffix}"
        ]
    }

    return random.choice(templates[position_index])


def interpret_overall(question: str, cards: list) -> str:
    theme = detect_theme(question)
    majors = [c for c in cards if c.get("arcana") == "major"]
    suits = [c["suit"] for c in cards if "suit" in c]
    parts = []

    parts.append(f"Объединяя три карты в единый рассказ, мы получаем развернутый ответ на ваш вопрос — «{question}».")

    if len(majors) >= 2:
        parts.append("Присутствие нескольких старших арканов говорит о том, что в этой ситуации задействованы глубинные процессы. Здесь больше судьбы, чем случайности, и происходящее имеет для вас большое значение.")
    else:
        parts.append("Преобладание младших арканов напоминает: исход ситуации во многом зависит от ваших ежедневных шагов и решений. Вы сами творите свою реальность.")

    if suits:
        top, cnt = Counter(suits).most_common(1)[0]
        if cnt >= 2:
            parts.append(f"Тот факт, что две или три карты относятся к масти {top}, акцентирует ваше внимание на сфере {SUITS[top]['theme']}.")

    names = " → ".join(f"«{c['name']}»" for c in cards)
    parts.append(f"История вашего расклада разворачивается от карты {names.split(' → ')[0]} через текущий момент к финалу. Это показывает, как одна энергия плавно перетекает в другую, формируя вашу реальность.")

    advice = {
        "love": "Главный совет: прислушайтесь к своим чувствам и не бойтесь быть искренними. Отношения сейчас требуют деликатности, но при этом важно не забывать о своих собственных границах.",
        "career": "Главный совет: действуйте осознанно. Проявите инициативу там, где это необходимо, но не забывайте анализировать детали. Ваш успех сейчас кроется в балансе между смелостью и расчетом.",
        "money": "Главный совет: сохраняйте финансовую осознанность. Избегайте спонтанных крупных трат, но будьте открыты к новым возможностям для заработка, которые могут появиться на вашем пути.",
        "future": "Главный совет: доверьтесь течению жизни, но держите руку на руле. Будущее не предопределено, и ваши осознанные действия сегодня могут мягко скорректировать вектор событий.",
    }[theme]
    parts.append(advice)
    parts.append("Помните, что карты Таро — это зеркало вашей текущей энергии, а не жесткий приговор. Осознанный выбор всегда в ваших руках.")
    
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
                 "content": ("Ты — опытный и вдумчивый таролог. Твоя задача — дать глубокий, связный и человечный ответ на вопрос пользователя по выпавшей карте. "
                             "Пиши развернуто (4-5 предложений), используй теплый, доверительный тон. "
                             "Избегай сухих шаблонов и клише. Задавай наводящие вопросы или давай пищу для размышлений. "
                             "Свяжи суть карты с позицией в раскладе и конкретным вопросом пользователя.")},
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
        pos_names = ["прошлое", "настоящее", "будущее"]
        prompt = (
            f"Вопрос пользователя: «{question}».\n"
            f"Позиция в раскладе: {pos_names[position_index]}.\n"
            f"Выпавшая карта: «{card['name']}».\n"
            f"Базовое значение карты: {card.get('description')}\n\n"
            f"ЗАДАЧА: Напиши толкование этой карты для пользователя.\n"
            f"ПРАВИЛА:\n"
            f"1. Пиши связно, вдумчиво, простыми и понятными словами.\n"
            f"2. Объем: 4-5 предложений.\n"
            f"3. Уникальность: придумай уникальное вступление, не используй шаблонные фразы (например, 'эта карта означает').\n"
            f"4. Связь: покажи, как энергия карты проявляется в контексте вопроса и позиции в раскладе.\n"
            f"5. Рефлексия: заверши советом или вопросом, который заставит пользователя задуматься."
        )
        ai = _ai_call(prompt, max_tokens=400)
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
            f"Напиши ОБЩИЙ СИНТЕЗ-РАСКЛАД (6-8 предложений):\n"
            f"1. Свяжи все три карты в единую, плавную историю (от прошлого к будущему).\n"
            f"2. Прямо и развернуто ответь на заданный вопрос пользователя.\n"
            f"3. Дай глубокий, поддерживающий совет.\n"
            f"Пиши красивым, литературным языком, обращаясь на «вы»."
        )
        ai = _ai_call(prompt, max_tokens=700)
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

    <!-- ФОНОВЫЕ СЛОИ -->
    <div class="bg-layer">
        <div class="bg-mandala-1"></div>
        <div class="bg-mandala-2"></div>
        <div class="bg-smoke"></div>
    </div>

    <!-- Canvas для частиц -->
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

            <!-- БЛОК С КАРТИНКОЙ (Только карты, без рамки) -->
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

/* =========================================
   МНОГОСЛОЙНЫЙ ФОН
   ========================================= */
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

/* =========================================
   ОСНОВНОЙ КОНТЕНТ
   ========================================= */
#particlesCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 100;
}

.container { 
    max-width: 900px; 
    width: 100%; 
    position: relative; 
    z-index: 1; 
}
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

/* =========================================
   БЛОК С КАРТИНКОЙ (КАРТЫ)
   ========================================= */
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

/* =========================================
   ОСТАЛЬНЫЕ ЭЛЕМЕНТЫ
   ========================================= */
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
   REVEAL
   ============================================================ */
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
print("✅ Все файлы обновлены (Связные и глубокие ответы).")
print("Запускай: python setup.py -> python app.py")
print("========================================")