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
