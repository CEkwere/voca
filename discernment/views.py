from django.shortcuts import render
from .models import Question, Choice

# Charism descriptions and information
CHARISM_DATA = {
    "capuchin": {
        "name": "Capuchin",
        "description": "Emphasis on simplicity, poverty, and direct service to the poor. Capuchins value humility and a close relationship with nature.",
        "values": ["Simplicity", "Poverty", "Service", "Humility", "Community"]
    },
    "dominican": {
        "name": "Dominican",
        "description": "Focus on study, preaching, and intellectual pursuit. Dominicans seek truth through learning and share it through teaching and ministry.",
        "values": ["Study", "Preaching", "Intellectual pursuit", "Teaching", "Service"]
    },
    "benedictine": {
        "name": "Benedictine",
        "description": "Balance of prayer and work (ora et labora). Benedictines value liturgical life, stability, and communal rhythms.",
        "values": ["Prayer", "Work", "Stability", "Community", "Liturgy"]
    },
    "carmelite": {
        "name": "Carmelite",
        "description": "Contemplative prayer and mystical experience. Carmelites seek deep union with God through silent prayer and interior transformation.",
        "values": ["Contemplation", "Prayer", "Mysticism", "Interior life", "Silence"]
    },
    "augustinian": {
        "name": "Augustinian",
        "description": "Balance of study and pastoral care. Augustinians combine intellectual rigor with compassionate service to others.",
        "values": ["Learning", "Pastoral care", "Balance", "Compassion", "Community"]
    }
}

def quiz(request):
    questions = Question.objects.all()

    if request.method == "POST":
        scores = {
            "capuchin": 0,
            "dominican": 0,
            "benedictine": 0,
            "carmelite": 0,
            "augustinian": 0,
        }

        for question in questions:
            choice_id = request.POST.get(f"question_{question.id}")
            choice = Choice.objects.get(id=choice_id)

            scores["capuchin"] += choice.capuchin
            scores["dominican"] += choice.dominican
            scores["benedictine"] += choice.benedictine
            scores["carmelite"] += choice.carmelite
            scores["augustinian"] += choice.augustinian

        # Get highest score
        result = max(scores, key=scores.get)

        # Pass all scores and charism data to result page
        context = {
            "result": result,
            "result_display": result.title(),
            "scores": scores,
            "charism_data": CHARISM_DATA,
        }
        return render(request, "result.html", context)

    return render(request, "quiz.html", {"questions": questions})


def home(request):
    # Simple landing page with a CTA to start the quiz
    return render(request, "home.html")