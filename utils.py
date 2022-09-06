from __future__ import annotations

import json

def load_candidates() -> list[dict]:
    with open('data.json', 'r', encoding = 'utf-8') as file:
        candidates = json.load(file)
        return candidates

def format_candidates(сandidates: list[dict]) -> str:
    #Форматирование списка кандидатов - передаем список, она нам создает отформатированный html"
    result = '<pre>'

    for candidate in сandidates:
        result += f"""
                {candidate['name']} \n
                {candidate['position']} \n
                {candidate['skills']} \n
                """

    result += '</pre>'
    return result

def get_all_candidates() -> list[dict]:
    return load_candidates()

def get_candidate_by_pk(uid: int) -> dict|None: #может быть только один кандидат
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['pk'] == uid:
            return candidate
    return None

def get_candidate_by_skill(skill: str) -> list[dict]: #может быть несколько кандидатов, возврадаем список со словарями
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)

    return result

#print(get_candidate_by_skill('Delphi'))