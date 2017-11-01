def process_user_query(query_string):
    s = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
    for i in query_string.split():
        #for i in t:
        if i in s:
            m = 'Russian'
            break
        else:
            m = 'No lenguage detected'
    return m
