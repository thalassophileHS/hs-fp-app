def print_greeting(student_name):
    print(f'Hello {student_name}!')

def process_user_query(query_string):
    x = input().split()
    result = print_greeting(x)
    return result
