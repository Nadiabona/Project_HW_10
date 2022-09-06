from flask import Flask

from utils import load_candidates, format_candidates, get_all_candidates, get_candidate_by_pk, get_candidate_by_skill

app = Flask(__name__)

@app.route('/')

def page_main():
    "Главная страница "
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result

@app.route('/candidate/<int:uid>')

def page_candidate(uid):
    "Кандиданты по pk"
    candidate: dict = get_candidate_by_pk(uid)
    result = f'<img src = "{candidate["picture"]}">'
    result+= format_candidates([candidate])
    return result


@app.route('/skills/<skill>')

def page_skills(skill):
    "Кандиданты по навыкам"
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result

app.run()

#print (get_candidate_by_pk(1))