def process_user_query(query_string):
    m = []
    for i in query_string.split():
        for t in i:
            if t.isupper():
                m.append(f'Hi {i}')
                break
    return m
