def process_user_query(query_string):
    student_name = query_string
    x = []
    for i in student_name:
        x += f'Hi, {i}'
    result = x
    return result


print(str(process_user_query(input().split())), end = '\n')
