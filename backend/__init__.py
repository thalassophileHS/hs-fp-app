def process_user_query(query_string):
    m = []
    for i in query_string.split():
        for t in i:
                if t.isupper():
                    m.append(i)
                break
    for i in m:
        greetings = f'Hi {i}'
    return greetings
