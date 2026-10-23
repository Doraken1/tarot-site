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
                 "content": ("Ты — опытный таролог. Твоя задача — дать краткий, простой и понятный ответ на вопрос пользователя по выпавшей карте. "
                             "Пиши лаконично (строго 2-3 предложения). Избегай общих фраз и шаблонов. Текст должен быть уникальным для каждой карты. "
                             "Объясни суть карты простыми словами и свяжи её с вопросом.")},
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
            f"1. Пиши простыми, понятными словами. Без сложного эзотерического жаргона.\n"
            f"2. Лаконичность: строго 2-3 предложения.\n"
            f"3. Уникальность: не используй шаблонные фразы (например, 'карта говорит о', 'эта карта означает'). Начни сразу с сути.\n"
            f"4. Прямой ответ: свяжи суть карты напрямую с вопросом пользователя.\n"
            f"5. Суть карты: обязательно отрази именно значение этой конкретной карты (если выпала Башня — говори о резких переменах, если Солнце — о радости)."
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
            f"Напиши ОБЩИЙ СИНТЕЗ-РАСКЛАД (5-7 предложений):\n"
            f"1. Свяжи все три карты в единую линию развития;\n"
            f"2. Прямо ответь на заданный вопрос пользователя;\n"
            f"3. Дай мягкий, но конкретный совет.\n"
            f"Пиши простыми словами, связным текстом, обращаясь на «вы». Без лишних вступлений."
        )
        ai = _ai_call(prompt, max_tokens=600)
        if ai:
            return ai
            
    from tarot_data import interpret_overall
    return interpret_overall(question, cards)
