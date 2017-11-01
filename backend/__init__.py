def process_user_query(query_string):
    for i in query_string:
        if (i == й) or (i == ъ) or (i == ы) or (i == э) or (i == щ):
            m = 'Russian'
            break
        else:
            m = 'No lenguage detected'
    return m
