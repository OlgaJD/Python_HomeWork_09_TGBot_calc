def get_complex_result(user_ex):
    try:
        result = eval(user_ex)
        return result
    except:
        return 'Выражение введено неверно'