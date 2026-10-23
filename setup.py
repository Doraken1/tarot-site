"""
Создаёт все файлы проекта Таро. Убран статический совет, финал строится из карт.
Запуск: python setup.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = {}

# ============ tarot_data.py ============
FILES["tarot_data.py"] = r'''
"""Полная колода 78 карт + генератор прогноза, где финал строится только из карт и вопроса."""
import random
from collections import Counter

# ================= СТАРШИЕ АРКАНЫ (22) =================
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

# ================= МЛАДШИЕ АРКАНЫ (56) =================
MINOR = [
    {"name": "Туз Жезлов", "num": "A", "symbol": "🪄", "suit": "Жезлы", "description": "новый импульс, вдохновение, начало активного проекта", "love": "вспышка страсти", "career": "старт нового дела", "money": "новый источник дохода", "future": "прилив энергии и новых идей"},
    {"name": "Двойка Жезлов", "num": "II", "symbol": "🪄", "suit": "Жезлы", "description": "планирование, выбор направления, дальновидность", "love": "выбор между двумя людьми", "career": "разработка стратегии", "money": "планирование бюджета", "future": "необходимость сделать выбор"},
    {"name": "Тройка Жезлов", "num": "III", "symbol": "🪄", "suit": "Жезлы", "description": "расширение, первые результаты, взгляд вдаль", "love": "развитие отношений", "career": "успешные переговоры", "money": "рост инвестиций", "future": "первые плоды трудов"},
    {"name": "Четвёрка Жезлов", "num": "IV", "symbol": "🪄", "suit": "Жезлы", "description": "праздник, стабильность, гармония в доме", "love": "помолвка или совместный быт", "career": "завершение важного этапа", "money": "финансовая стабильность", "future": "радостное событие, праздник"},
    {"name": "Пятёрка Жезлов", "num": "V", "symbol": "🪄", "suit": "Жезлы", "description": "конкуренция, споры, хаотичная энергия", "love": "соперничество", "career": "конфликты в коллективе", "money": "споры о деньгах", "future": "соревнование или мелкие ссоры"},
    {"name": "Шестёрка Жезлов", "num": "VI", "symbol": "🪄", "suit": "Жезлы", "description": "победа, триумф, общественное признание", "love": "успех у противоположного пола", "career": "повышение или награда", "money": "крупная премия", "future": "успех и признание заслуг"},
    {"name": "Семёрка Жезлов", "num": "VII", "symbol": "🪄", "suit": "Жезлы", "description": "защита своих позиций, стойкость, преодоление", "love": "борьба за отношения", "career": "отстаивание проекта", "money": "защита активов", "future": "необходимость постоять за себя"},
    {"name": "Восьмёрка Жезлов", "num": "VIII", "symbol": "🪄", "suit": "Жезлы", "description": "скорость, стремительное развитие, новости", "love": "быстрое развитие романа", "career": "срочные новости", "money": "быстрый оборот средств", "future": "стремительные события"},
    {"name": "Девятка Жезлов", "num": "IX", "symbol": "🪄", "suit": "Жезлы", "description": "упорство, последний рубеж, усталость", "love": "осторожность после травмы", "career": "финальный рывок", "money": "экономия ресурсов", "future": "испытание на прочность"},
    {"name": "Десятка Жезлов", "num": "X", "symbol": "🪄", "suit": "Жезлы", "description": "бремя, перегрузка, завершение цикла", "love": "тяжесть обязательств", "career": "чрезмерная нагрузка", "money": "долги", "future": "освобождение от лишнего груза"},
    {"name": "Паж Жезлов", "num": "P", "symbol": "🪄", "suit": "Жезлы", "description": "энтузиазм, новая идея, любопытство", "love": "легкий флирт", "career": "интересный проект", "money": "новая подработка", "future": "появление вдохновляющей идеи"},
    {"name": "Рыцарь Жезлов", "num": "Kn", "symbol": "🪄", "suit": "Жезлы", "description": "страсть, действие, импульсивность", "love": "стремительный роман", "career": "смелый шаг", "money": "рискованная сделка", "future": "активные действия"},
    {"name": "Королева Жезлов", "num": "Q", "symbol": "🪄", "suit": "Жезлы", "description": "уверенность, харизма, творческая энергия", "love": "привлекательность", "career": "лидерство", "money": "независимость", "future": "уверенность в своих силах"},
    {"name": "Король Жезлов", "num": "K", "symbol": "🪄", "suit": "Жезлы", "description": "видение, лидерство, воля", "love": "доминирование", "career": "управление проектом", "money": "крупный успех", "future": "взятие контроля в свои руки"},
    
    {"name": "Туз Кубков", "num": "A", "symbol": "🏆", "suit": "Кубки", "description": "новые чувства, любовь, эмоциональный подъем", "love": "зарождение любви", "career": "работа в удовольствие", "money": "приятный подарок", "future": "всплеск позитивных эмоций"},
    {"name": "Двойка Кубков", "num": "II", "symbol": "🏆", "suit": "Кубки", "description": "союз, взаимность, гармония в паре", "love": "идеальное партнерство", "career": "удачный альянс", "money": "совместные накопления", "future": "встреча или укрепление союза"},
    {"name": "Тройка Кубков", "num": "III", "symbol": "🏆", "suit": "Кубки", "description": "дружба, веселье, праздник", "love": "радость общения", "career": "сплоченная команда", "money": "приятные траты", "future": "веселое событие в кругу друзей"},
    {"name": "Четвёрка Кубков", "num": "IV", "symbol": "🏆", "suit": "Кубки", "description": "апатия, застой, скука", "love": "неудовлетворенность", "career": "рутина", "money": "упущенная выгода", "future": "период поиска нового смысла"},
    {"name": "Пятёрка Кубков", "num": "V", "symbol": "🏆", "suit": "Кубки", "description": "утрата, сожаление, грусть", "love": "расставание", "career": "разочарование в проекте", "money": "финансовая потеря", "future": "исцеление после потери"},
    {"name": "Шестёрка Кубков", "num": "VI", "symbol": "🏆", "suit": "Кубки", "description": "ностальгия, детство, теплые воспоминания", "love": "возвращение прошлой любви", "career": "опыт из прошлого", "money": "помощь от родственников", "future": "приятные новости из прошлого"},
    {"name": "Семёрка Кубков", "num": "VII", "symbol": "🏆", "suit": "Кубки", "description": "иллюзии, выбор, множество вариантов", "love": "нереальные ожидания", "career": "много предложений", "money": "миражи богатства", "future": "необходимость отличить мечту от реальности"},
    {"name": "Восьмёрка Кубков", "num": "VIII", "symbol": "🏆", "suit": "Кубки", "description": "уход, поиск истины, смена обстановки", "love": "уход из отношений", "career": "смена работы", "money": "отказ от привычных трат", "future": "движение к новому"},
    {"name": "Девятка Кубков", "num": "IX", "symbol": "🏆", "suit": "Кубки", "description": "удовлетворение, исполнение желаний, комфорт", "love": "получение желаемого", "career": "успех и довольство", "money": "исполнение материальной мечты", "future": "исполнение заветного желания"},
    {"name": "Десятка Кубков", "num": "X", "symbol": "🏆", "suit": "Кубки", "description": "гармония, семья, абсолютное счастье", "love": "счастливый брак", "career": "мир в коллективе", "money": "достаток для семьи", "future": "гармония и мир"},
    {"name": "Паж Кубков", "num": "P", "symbol": "🏆", "suit": "Кубки", "description": "творчество, чувствительность, романтическая весть", "love": "признание в любви", "career": "творческий проект", "money": "небольшой подарок", "future": "романтическое или творческое послание"},
    {"name": "Рыцарь Кубков", "num": "Kn", "symbol": "🏆", "suit": "Кубки", "description": "романтика, предложение, следование за мечтой", "love": "сказочный роман", "career": "вдохновляющая работа", "money": "траты на искусство", "future": "романтическое приключение"},
    {"name": "Королева Кубков", "num": "Q", "symbol": "🏆", "suit": "Кубки", "description": "эмпатия, забота, интуиция", "love": "глубокая привязанность", "career": "поддержка коллег", "money": "интуитивные покупки", "future": "эмоциональная поддержка"},
    {"name": "Король Кубков", "num": "K", "symbol": "🏆", "suit": "Кубки", "description": "мудрость, дипломатия, контроль эмоций", "love": "зрелые отношения", "career": "мудрое руководство", "money": "стабильное благополучие", "future": "сохранение спокойствия и баланса"},

    {"name": "Туз Мечей", "num": "A", "symbol": "⚔️", "suit": "Мечи", "description": "прорыв, ясность, истина", "love": "расстановка точек", "career": "гениальная идея", "money": "четкое планирование", "future": "озарение и ясность ума"},
    {"name": "Двойка Мечей", "num": "II", "symbol": "⚔️", "suit": "Мечи", "description": "неопределенность, тупик, пауза", "love": "игнорирование проблем", "career": "закрытые двери", "money": "заморозка средств", "future": "необходимость принять сложное решение"},
    {"name": "Тройка Мечей", "num": "III", "symbol": "⚔️", "suit": "Мечи", "description": "боль, разрыв, печальная правда", "love": "измена или ссора", "career": "увольнение", "money": "потеря", "future": "разочарование, которое пойдет на пользу"},
    {"name": "Четвёрка Мечей", "num": "IV", "symbol": "⚔️", "suit": "Мечи", "description": "отдых, восстановление, тишина", "love": "тайм-аут в отношениях", "career": "отпуск", "money": "экономия", "future": "необходимость сделать паузу"},
    {"name": "Пятёрка Мечей", "num": "V", "symbol": "⚔️", "suit": "Мечи", "description": "конфликт, поражение, эго", "love": "борьба за власть", "career": "интриги", "money": "потери из-за споров", "future": "урок смирения"},
    {"name": "Шестёрка Мечей", "num": "VI", "symbol": "⚔️", "suit": "Мечи", "description": "переход, отъезд, уход от проблем", "love": "побег от прошлого", "career": "смена места", "money": "перевод средств", "future": "смена обстановки к лучшему"},
    {"name": "Семёрка Мечей", "num": "VII", "symbol": "⚔️", "suit": "Мечи", "description": "хитрость, обман, стратегия", "love": "неискренность", "career": "кража идеи", "money": "финансовая махинация", "future": "необходимость быть бдительным"},
    {"name": "Восьмёрка Мечей", "num": "VIII", "symbol": "⚔️", "suit": "Мечи", "description": "ограничения, ловушка, страхи", "love": "ощущение связанности", "career": "нехватка ресурсов", "money": "жесткие рамки", "future": "освобождение от страхов"},
    {"name": "Девятка Мечей", "num": "IX", "symbol": "⚔️", "suit": "Мечи", "description": "тревога, бессонница, страхи", "love": "мнительность", "career": "стресс", "money": "финансовая бессонница", "future": "избавление от тревожных мыслей"},
    {"name": "Десятка Мечей", "num": "X", "symbol": "⚔️", "suit": "Мечи", "description": "дно, завершение, болезненный финал", "love": "окончательный разрыв", "career": "провал", "money": "банкротство", "future": "полное завершение сложного этапа"},
    {"name": "Паж Мечей", "num": "P", "symbol": "⚔️", "suit": "Мечи", "description": "любопытство, новости, бдительность", "love": "проверка информации", "career": "стажировка", "money": "новые знания", "future": "получение важной информации"},
    {"name": "Рыцарь Мечей", "num": "Kn", "symbol": "⚔️", "suit": "Мечи", "description": "прямота, скорость, агрессия", "love": "выяснение отношений", "career": "резкие решения", "money": "быстрые действия", "future": "стремительное решение проблемы"},
    {"name": "Королева Мечей", "num": "Q", "symbol": "⚔️", "suit": "Мечи", "description": "независимость, холодный разум, проницательность", "love": "отказ от иллюзий", "career": "жесткие переговоры", "money": "финансовая независимость", "future": "необходимость включить логику"},
    {"name": "Король Мечей", "num": "K", "symbol": "⚔️", "suit": "Мечи", "description": "логика, справедливость, авторитет", "love": "контроль чувств", "career": "экспертное мнение", "money": "юридические вопросы", "future": "справедливое разрешение спора"},

    {"name": "Туз Пентаклей", "num": "A", "symbol": "🪙", "suit": "Пентакли", "description": "шанс, богатство, материальная возможность", "love": "прочное начало", "career": "выгодное предложение", "money": "крупное поступление", "future": "отличная материальная возможность"},
    {"name": "Двойка Пентаклей", "num": "II", "symbol": "🪙", "suit": "Пентакли", "description": "жонглирование, баланс, гибкость", "love": "совмещение личного и работы", "career": "многозадачность", "money": "несколько источников дохода", "future": "необходимость балансировать"},
    {"name": "Тройка Пентаклей", "num": "III", "symbol": "🪙", "suit": "Пентакли", "description": "командная работа, мастерство, качество", "love": "совместное строительство", "career": "успешный проект", "money": "доход от сотрудничества", "future": "признание ваших навыков"},
    {"name": "Четвёрка Пентаклей", "num": "IV", "symbol": "🪙", "suit": "Пентакли", "description": "стабильность, контроль, удержание", "love": "собственничество", "career": "страх потерять работу", "money": "накопления", "future": "сохранение текущих позиций"},
    {"name": "Пятёрка Пентаклей", "num": "V", "symbol": "🪙", "suit": "Пентакли", "description": "нужда, потеря, изоляция", "love": "чувство одиночества", "career": "материальные трудности", "money": "финансовый кризис", "future": "выход из зоны дискомфорта"},
    {"name": "Шестёрка Пентаклей", "num": "VI", "symbol": "🪙", "suit": "Пентакли", "description": "щедрость, помощь, справедливый обмен", "love": "равные вложения", "career": "премия", "money": "получение кредита или подарка", "future": "получение помощи или награды"},
    {"name": "Семёрка Пентаклей", "num": "VII", "symbol": "🪙", "suit": "Пентакли", "description": "оценка, терпение, ожидание результата", "love": "выжидание", "career": "анализ проделанной работы", "money": "долгосрочные инвестиции", "future": "время собирать плоды"},
    {"name": "Восьмёрка Пентаклей", "num": "VIII", "symbol": "🪙", "suit": "Пентакли", "description": "труд, обучение, усердие", "love": "работа над отношениями", "career": "повышение квалификации", "money": "монотонный заработок", "future": "кропотливый труд принесет результат"},
    {"name": "Девятка Пентаклей", "num": "IX", "symbol": "🪙", "suit": "Пентакли", "description": "изобилие, независимость, комфорт", "love": "самодостаточность", "career": "успех", "money": "финансовая свобода", "future": "достижение комфорта"},
    {"name": "Десятка Пентаклей", "num": "X", "symbol": "🪙", "suit": "Пентакли", "description": "богатство, семья, наследие", "love": "создание семьи", "career": "наследство или крупный бизнес", "money": "стабильное богатство", "future": "прочный фундамент на годы"},
    {"name": "Паж Пентаклей", "num": "P", "symbol": "🪙", "suit": "Пентакли", "description": "новые начинания, учеба, возможности", "love": "робкое начало", "career": "обучение", "money": "новая работа", "future": "получение новых знаний"},
    {"name": "Рыцарь Пентаклей", "num": "Kn", "symbol": "🪙", "suit": "Пентакли", "description": "надежность, методичность, упорство", "love": "серьезные намерения", "career": "стабильная работа", "money": "постепенное накопление", "future": "медленное, но верное продвижение"},
    {"name": "Королева Пентаклей", "num": "Q", "symbol": "🪙", "suit": "Пентакли", "description": "практичность, забота, уют", "love": "создание уюта", "career": "финансовый менеджмент", "money": "бережливость", "future": "обретение уверенности в завтрашнем дне"},
    {"name": "Король Пентаклей", "num": "K", "symbol": "🪙", "suit": "Пентакли", "description": "успех, процветание, стабильность", "love": "надежный партнер", "career": "руководящая должность", "money": "крупный капитал", "future": "достижение материального успеха"}
]

ALL_CARDS = (
    [dict(c, arcana="major") for c in MAJOR]
    + [dict(c, arcana="minor") for c in MINOR]
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
    {"name": "Предзнаменование 1", "short": "1"},
    {"name": "Предзнаменование 2", "short": "2"},
    {"name": "Предзнаменование 3", "short": "3"},
]

def interpret_card(question: str, card: dict, position_index: int) -> str:
    theme = detect_theme(question)
    desc = (card.get(theme) or card.get("description")).lower().strip()
    if desc.endswith('.'):
        desc = desc[:-1]

    templates = [
        f"Карта «{card['name']}» предвещает, что в будущем вас ожидает {desc}. Это событие или состояние уже начинает формироваться на горизонте.",
        f"Скоро в вашей жизни проявится энергия карты «{card['name']}». Ожидайте {desc}. Это станет важным этапом вашего пути.",
        f"В грядущих событиях ключевую роль сыграет «{card['name']}». Впереди {desc}. Будьте готовы принять эту энергию.",
        f"«{card['name']}» указывает на то, что вас ждет {desc}. Это то, к чему стоит подготовиться и что принесет новые перемены."
    ]

    if card.get("arcana") == "major":
        suffix = " Это карта старшего аркана, поэтому ее влияние будет глубоким и судьбоносным."
    else:
        suffix = ""

    return random.choice(templates) + suffix


def interpret_overall(question: str, cards: list) -> str:
    theme = detect_theme(question)
    # Достаём смыслы карт и убираем точки в конце
    m1 = (cards[0].get(theme) or cards[0]["description"]).lower().rstrip('.')
    m2 = (cards[1].get(theme) or cards[1]["description"]).lower().rstrip('.')
    m3 = (cards[2].get(theme) or cards[2]["description"]).lower().rstrip('.')
    n1, n2, n3 = cards[0]["name"], cards[1]["name"], cards[2]["name"]

    # 5 разных сюжетных структур — ни один из них не содержит статических советов
    structures = [
        # 1. Хронология
        f"По вашему вопросу «{question}» карты показывают следующий сценарий. Сначала придет энергия «{n1}» — это {m1}. Затем она перерастет в «{n2}»: {m2}. А завершит этот цикл «{n3}», принеся {m3}. Таков прогноз развития ситуации.",

        # 2. Акцент на карту в середине
        f"Отвечая на «{question}», центральная карта «{n2}» обещает {m2}. Это станет ключевым поворотом. При этом «{n1}» ({m1}) подготовит почву, а «{n3}» ({m3}) покажет конечный результат. Именно в такой связке эти карты формируют ваше ближайшее будущее.",

        # 3. Прямой ответ
        f"Вас ожидает период, где {m1} (карта «{n1}») сменится {m2} (карта «{n2}»). Важно готовиться к тому, что в финале проявится {m3} (карта «{n3}»). Это прямой ответ на ваш вопрос «{question}», основанный на трех энергиях.",

        # 4. Философская
        f"Размышляя над вопросом «{question}», можно увидеть путь трансформации. «{n1}» показывает отправную точку ({m1}), «{n2}» — процесс ({m2}), а «{n3}» — итог ({m3}). Эти три силы уже работают, формируя вашу реальность.",

        # 5. Контрастная
        f"Ваш вопрос «{question}» показывает контраст: с одной стороны — «{n1}» с энергией {m1}, с другой — «{n3}» с темой {m3}. Мостом между ними становится «{n2}» ({m2}). Именно этот переход и станет главным событием ближайшего будущего."
    ]

    story = random.choice(structures)

    # Финальный акцент на основе мастей и арканов (без клише)
    majors = [c for c in cards if c.get("arcana") == "major"]
    suits = [c["suit"] for c in cards if "suit" in c]
    
    emphasis = ""
    if len(majors) >= 2:
        emphasis = " Поскольку в раскладе преобладают старшие арканы, событие имеет судьбоносный вес — оно изменит многое."
    elif suits:
        top, cnt = Counter(suits).most_common(1)[0]
        if cnt >= 2:
            emphasis = f" Особый акцент — на масти {top}, что делает сферу {SUITS[top]['theme']} главной для вас."
    
    return story + emphasis


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
                 "content": ("Ты — опытный таролог. Предсказывай будущее строго на основе выпавших карт. "
                             "Никаких общих советов, клише, упоминаний 'карты — это зеркало' или 'всё в ваших руках'. "
                             "Только конкретный прогноз: что, когда и как произойдёт. "
                             "Пиши живо, уникально для каждого запроса.")},
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
        prompt = (
            f"Вопрос: «{question}».\n"
            f"Карта: «{card['name']}».\n"
            f"Значение: {card.get('description')}.\n\n"
            f"Напиши прогноз (3-4 предложения) о том, что эта карта предвещает в будущем. "
            f"Что именно ждёт человека. Без общих фраз."
        )
        ai = _ai_call(prompt, max_tokens=350)
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
            f"Вопрос: «{question}».\n"
            f"Выпали карты:\n{cards_text}\n\n"
            f"Напиши общий прогноз (5-6 предложений) — единый сценарий будущего. "
            f"Что произойдет сначала, что потом, к чему приведет. "
            f"Строго по смыслу карт и вопросу. Без шаблонов, советов и клише."
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
    <title>Таро-прогноз на будущее</title>
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
            <h1>🔮 Прогноз на будущее</h1>
            <p class="subtitle">Три карты откроют, что вас ждёт впереди</p>
            
            <form id="questionForm">
                <input id="questionInput" type="text"
                       placeholder="Например: что ждёт меня в будущем?"
                       maxlength="500" autocomplete="off">
                <button type="submit">Узнать будущее</button>
            </form>

            <div class="hero-images-wrapper">
                <img src="{{ url_for('static', filename='img/hero-cards.png') }}" class="hero-cards" alt="Карты Таро">
            </div>
        </section>

        <section id="loading" class="screen" style="display:none">
            <div class="spinner"></div>
            <p>Карты раскрывают будущее...</p>
        </section>

        <section id="resultScreen" class="screen" style="display:none">
            <p class="user-question">Ваш вопрос: <span id="userQuestion"></span></p>
            
            <div id="cardsGrid" class="cards-grid"></div>
            
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

.container { max-width: 1000px; width: 100%; position: relative; z-index: 1; }
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

.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 40px;
    align-items: start;
}

.card-block {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.tarot-card {
    width: 100%;
    min-height: 240px;
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
    justify-content: center;
}

.card-header { font-size: 0.85rem; font-weight: bold; color: #7a3eb8; letter-spacing: 2px; }
.card-symbol { font-size: 3.2rem; margin: 10px 0; }
.card-name { font-size: 1.1rem; font-weight: bold; text-align: center; color: #2a1147; margin-bottom: 8px; }
.card-desc { font-size: 0.85rem; text-align: center; color: #4a2a75; font-style: italic; }

.card-mini-reading {
    background: rgba(30, 15, 55, 0.85); 
    border: 1px solid #4a2a75;
    border-top: 3px solid #e6c869;
    border-radius: 10px;
    padding: 15px;
    text-align: left;
    font-size: 0.95rem;
    line-height: 1.6;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    flex-grow: 1;
}

.readings {
    max-width: 800px;
    margin: 0 auto 30px;
}

.overall {
    background: linear-gradient(135deg, rgba(60, 30, 100, 0.9), rgba(30, 15, 55, 0.9));
    border: 2px solid #e6c869;
    border-radius: 14px;
    padding: 24px 26px;
    text-align: left;
    line-height: 1.8;
    font-size: 1.05rem;
    box-shadow: 0 10px 40px rgba(230, 200, 105, 0.2);
}

.overall h2 { 
    color: #e6c869; 
    font-size: 1.3rem; 
    margin-bottom: 15px; 
    text-align: center; 
    letter-spacing: 1px; 
}

.reset { background: transparent; border: 2px solid #7a3eb8; color: #c986e8; margin-top: 20px; }
.reset:hover { background: #7a3eb8; color: #fff; }

@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

@media (max-width: 768px) {
    h1 { font-size: 1.7rem; }
    form { flex-direction: column; }
    .hero-images-wrapper { max-width: 300px; margin-top: 80px; } 
    .cards-grid {
        grid-template-columns: 1fr;
    }
    .tarot-card { min-height: 200px; width: 80%; margin: 0 auto; }
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
const cardsGrid = document.getElementById('cardsGrid');
const readingsList = document.getElementById('readings');
const resetBtn = document.getElementById('resetBtn');

const delay = (ms) => new Promise((r) => setTimeout(r, ms));

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

function makeCardBlock(card, readingText) {
    const wrapper = document.createElement('div');
    wrapper.className = 'card-block';
    wrapper.style.opacity = '0';
    wrapper.style.transform = 'translateY(-20px)';
    
    const cardEl = document.createElement('div');
    cardEl.className = 'tarot-card';
    cardEl.innerHTML =
        '<div class="card-header">' + card.num + '</div>' +
        '<div class="card-symbol">' + card.symbol + '</div>' +
        '<div class="card-name">' + card.name + '</div>' +
        '<div class="card-desc">' + card.description + '</div>';
        
    const textEl = document.createElement('div');
    textEl.className = 'card-mini-reading';
    textEl.innerText = readingText;

    wrapper.appendChild(cardEl);
    wrapper.appendChild(textEl);
    
    return wrapper;
}

function makeOverallEl(text) {
    const el = document.createElement('div');
    el.className = 'overall';
    el.style.opacity = '0';
    el.innerHTML =
        '<h2>✨ Итоговый прогноз</h2>' +
        '<div class="reading-text">' + text + '</div>';
    return el;
}

async function revealAll(data) {
    cardsGrid.innerHTML = '';
    readingsList.innerHTML = '';
    particles = [];

    for (let i = 0; i < data.cards.length; i++) {
        const card = data.cards[i];
        const reading = data.readings[i];

        const blockEl = makeCardBlock(card, reading.text);
        cardsGrid.appendChild(blockEl);
        
        await delay(50);

        const cardVisual = blockEl.querySelector('.tarot-card');
        const center = getElementCenter(cardVisual);

        blockEl.style.transition = 'opacity 0.5s ease, transform 0.6s ease-out';
        blockEl.style.opacity = '1';
        blockEl.style.transform = 'translateY(0)';
        
        spawnBurst(center.x, center.y, 45);
        
        setTimeout(() => {
            spawnBurst(center.x, center.y, 20);
        }, 300);

        await delay(800);
    }

    const overallEl = makeOverallEl(data.overall);
    readingsList.appendChild(overallEl);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    await delay(20);
    overallEl.style.transition = 'opacity 1s ease';
    overallEl.style.opacity = '1';

    const oc = getElementCenter(overallEl);
    setTimeout(() => {
        spawnBurst(oc.x, oc.y - 30, 80);
        setTimeout(() => spawnBurst(oc.x - 120, oc.y, 40), 180);
        setTimeout(() => spawnBurst(oc.x + 120, oc.y, 40), 360);
    }, 250);

    await delay(600);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const question = questionInput.value.trim();

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
    cardsGrid.innerHTML = '';
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
print("✅ Все файлы обновлены (Убраны статические советы, финал из карт).")
print("Запускай: python setup.py -> python app.py")
print("========================================")