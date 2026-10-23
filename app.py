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
