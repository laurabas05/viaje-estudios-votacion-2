from __future__ import annotations

import os

from flask import Flask, flash, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

SCORES = {
    "alumno1": 0,
    "alumno2": 0,
    "alumno3": 0,
    "alumno4": 0,
}


def compute_scores() -> tuple[list[tuple[str, int]], int]:
    total_votes = sum(SCORES.values())
    ranking = sorted(SCORES.items(), key=lambda item: item[1], reverse=True)
    return ranking, total_votes


MAX_UNIQUE_VOTES = 3


def candidate_exists(candidate: str) -> bool:
    candidate_lower = candidate.lower()
    return any(existing.lower() == candidate_lower for existing in SCORES)


@app.route("/", methods=["GET", "POST"])
def index():
    user_votes = session.get("votes_cast", [])
    if request.method == "POST":
        form_type = request.form.get("form_type", "vote")
        if form_type == "vote":
            vote = request.form.get("vote", "")
            if vote in SCORES:
                if vote in user_votes:
                    flash("Ya votaste a esta persona.")
                elif len(user_votes) >= MAX_UNIQUE_VOTES:
                    flash(f"Solo puedes votar a {MAX_UNIQUE_VOTES} personas distintas.")
                else:
                    updated_votes = [*user_votes, vote]
                    session["votes_cast"] = updated_votes
                    SCORES[vote] += 1
                    flash(f"Voto registrado para {vote}.")
            else:
                flash("Selecciona un candidato válido.")
        elif form_type == "new_candidate":
            candidate_name = request.form.get("new_candidate", "").strip()
            if not candidate_name:
                flash("Ingresa un nombre válido para dar de alta.")
            elif candidate_exists(candidate_name):
                flash("Esa persona ya está registrada.")
            else:
                SCORES[candidate_name] = 0
                flash(f"{candidate_name} se añadió a la lista.")
        else:
            flash("Acción no reconocida.")
        return redirect(url_for("index"))

    ranking, total_votes = compute_scores()
    return render_template(
        "index.html",
        ranking=ranking,
        total_votes=total_votes,
        user_votes=user_votes,
        max_unique_votes=MAX_UNIQUE_VOTES,
    )


@app.route("/api/scores", methods=["GET"])
def api_scores():
    ranking, total_votes = compute_scores()
    return {
        "ranking": [{"candidate": candidate, "score": score} for candidate, score in ranking],
        "total_votes": total_votes,
    }


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
