from flask import Flask

from utils import load_candidates, format_candidates

app = Flask(__name__)

@app.route('/')

def page_main():
    "Загружаем список кандидатов "
    candidates: list[dict] = load_candidates()
    result: str = format_candidates(candidates)
    return result

@app.route('/candidate/<int:uid>')

def page_candidate(uid):
    "Кандиданты по pk"

    candidates: list[dict] = load_candidates()
    result = '<pre>'

    for candidate in candidates:
        result += f"""
            {candidate['name']} \n
            {candidate['position']} \n
            {candidate['skills']} \n
            """

    result += '</pre>'
    return result

app.run()

