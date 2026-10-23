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
