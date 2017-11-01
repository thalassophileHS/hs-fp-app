def process_user_query(query_string):
    lenguages = {
        'Slavic' : 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'Armenian' : 'ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖ',
        'Georgian' : 'აბგდევზჱთიკლმნჲოპჟრსტჳუფქღყშჩცძწჭხჴჯჰჵჶჷჸ',
        'Latin' : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'Chinese' : '诶比西迪伊弗吉尺杰开勒马娜哦屁吉吾儿艾丝提伊吾维豆贝尔维克斯吾贼德',
        'Japanese' : 'あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん',
        'Korean' : 'ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ',
        'Cambodian' : 'កខគឃងចឆជឈញដឋឌឍណតថទធនបផពភមយរលវឝឞសហឡអ',
        'Greek' : 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝΞξΟοΠπΡρΣΤτΥυΦφΧχΨψΩω',
        'Arabic' : 'غظ ض ذ خ ث ت ش ر ق ص ف ع س ن م ل ك ي ط ح ز و ه د ج ب ا'
    }

    for t in set(query_string.split()):
        for i in t:
            for q,s in lenguages.items():
                for y in s:
                    if i == y:
                        m = q
                        break
                    else:
                        m = 'No lenguage detected'
    return str(m)

#print(process_user_query('نلسون رولیهلاهلا ماندلا (وه دی اومائه د ۲۶ تیر ۱۲۹۷ همبایی وا ۱۸ جوئیه ۱۹۱۸ - د دنیا رئته د ۱۴ آذر ۱۳۹۲ همبایی وا ۵ دسامر ۲۰۱۳) اولین سرکومره ولات افریقا هارگه ئه که د انتخاوات خلک سالار خلکمن انتخاوه بی'))
