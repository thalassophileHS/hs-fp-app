def process_user_query(query_string):
    lenguages = {
        'Slavic' : 'БГДЁЖЗИЙЛФЦЧШЩЪЫЬЭЮЯ',
        'Armenian' : 'ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖ',
        'Georgian' : 'აბგდევზჱთიკლმნჲოპჟრსტჳუფქღყშჩცძწჭხჴჯჰჵჶჷჸ',
        'Latin' : 'DFGJLQRSTVWZ',
        'Chinese' : '诶比西迪伊弗吉尺杰开勒马娜哦屁吉吾儿艾丝提伊吾维豆贝尔维克斯吾贼德',
        'Japanese' : 'あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん',
        'Korean' : 'ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ',
        'Cambodian' : 'កខគឃងចឆជឈញដឋឌឍណតថទធនបផពភមយរលវឝឞសហឡអ',
        'Greek' : 'αβΓγΔδεΖζηΘθιΛλμΞξπρΣΤτΥΦφχΨψΩω',
        'Arabic' : 'غظ ض ذ خ ث ت ش ر ق ص ف ع س ن م ل ك ي ط ح ز و ه د ج ب ا'
    }

    for word in set(query_string.split()):
        for letter in word:
            for key,value in lenguages.items():
                for char in value:
                    if letter == char:
                        m = key
                        break
                    else:
                        m = 'No lenguage detected'
                        continue
    return str(m)

print(process_user_query('JAUHFG'))
