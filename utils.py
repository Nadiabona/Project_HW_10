import json

def load_candidates() -> list[dict]:
    with open('data.json', 'r', encoding = 'utf-8') as file:
        candidates = json.load(file)
        return candidates

def format_candidates(candidates: list[dict]) -> str:
    "Форматирование списка кандидатов - передаем список, она нам создает отформатированный html"
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

def get_all_candidates() -> list[dict]:
    return load_candidates()