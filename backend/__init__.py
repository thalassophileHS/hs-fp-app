def process_user_query(query_string):
    lenguages = {
        'Russian' : 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    }

    for t in set(query_string.split()):
        for i in t:
            for s in lenguages.values():
                for y in s:
                    if i == y:
                        m = lenguages.keys()
                        m = ' '.join(m)
                        break
                    else:
                        m = 'No lenguage detected'
    return str(m)

#print(process_user_query('В ЮАР Нельсон Мандела также известен как Мадиба (одно из клановых имён народа коса)[26]. Самый пожилой и долгоживущий президент ЮАР: прожил 95 лет (на момент начала президентства — 76 лет, на момент окончания — 81).'))
