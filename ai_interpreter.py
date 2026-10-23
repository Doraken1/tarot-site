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
