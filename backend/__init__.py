def process_user_query(query_string):
    lenguages_char = {
        'Slavic' : 'БГДЁЖЗИЙЛФЦЧШЩЪЫЬЭЮЯ',
        'Armenian' : 'ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖ',
        'Georgian' : 'აბგდევზჱთიკლმნჲოპჟრსტჳუფქღყშჩცძწჭხჴჯჰჵჶჷჸ',
        'Latin' : 'DFGJLQRSTVWZ',
        'Chinese' : '诶比西迪伊弗吉尺杰开勒马娜哦屁吉吾儿艾丝提伊吾维豆贝尔维克斯吾贼德',
        'Japanese' : 'あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん',
        'Korean' : 'ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ',
        'Cambodian' : 'កខគឃងចឆជឈញដឋឌឍណតថទធនបផពភមយរលវឝឞសហឡអ',
        'Greek' : 'αβΓγΔδεΖζηΘθιΛλμΞξπρΣΤτΥΦφχΨψΩω',
        'Arabic': 'غظضذخثتشرقصفعسنملكيطحزوهدجبا',
        'Tamil' : 'அஆஇஈஉஊஎஏஐஒஓஔகஙசஞடணதநபமய'
    }
    leng = {
        'French' : ['le', 'il', 'est'],
        'Spanish' : ['los', 'las', 'unos', 'unas', 'y'],
        'Romanian' : ['și', 'în', 'între', 'cea', 'au'],
        'Italina' : ['è', 'di', 'con', 'per'],
        'Portuguese' : [ 'à', 'e', 'às', 'em', 'são', 'mas', 'que'],
        'Wallon' : ['dji', 'nén', 'rén', 'bén', 'pol', 'ås', 'vs', 'ki', 'pô', 'èn', 'dj'],
        'English' : [ 'an', 'and', 'in', 'of', 'the', 'that', 'is', 'I'],
        'German' : [ 'der', 'die', 'dem', 'sie', 'ist', 'ich', 'aber'],
        'Dutch' : ['het', 'op', 'een', 'voor'],
        'Afrikaans' : [ f'\'n', 'vir', 'nie'],
        'Swedish' : [ 'och', 'att', 'det', 'som', 'är'],
        'Danish' : ['af', 'til', 'med', 'det'],
        'Norwegian' : ['ble', 'å', 'eller'],
        'Latvian' : ['bija', 'tika', 'viņš'],
        'Lithuanian' : ['yra', 'kad'],
        'Polish' : [ 'w', 'jest', 'się'],
        'Czech' : ['z', 'k', 'až', 'však'],
        'Slovak' : [ 'yr', 'ac'],
        'Turkish' : ['bir', 'bu', 'fakat', 'oldu', 'şu'],
        'Welsh' : ['yr', 'ac'],
        'Finnish' : ['sinä'],
        'Estonian' : ['või'],
        'Hungarian' : ['az', 'ez', 'egy', 'hogy']
    }
    for word in set(query_string.split()):
        for letter in word:
            for key,value in lenguages_char.items():
                for char in value:
                    if letter == char:
                        m = key
                        #return m
    if m == 'Latin':
        for word in query_string.split():
            for key, value in leng.items():
                if word in value:
                    m = key
    if m == 'Slavic':
        for word in query_string.split():
            if word == 'със':
                m = 'Bulgarian'
            else:
                for letter in word:
                    if letter in ['ј', 'љ', 'њ','џ', 'ђ', 'ћ']:
                        m = 'Serbian'
                        break
                    else:
                        m = 'Russian'

    return m
