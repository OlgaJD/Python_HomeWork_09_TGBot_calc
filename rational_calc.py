def summ(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def get_rational_result(expression):
    try:
        if '(' in expression:
            start = 0
            for i in range(len(expression)):
                if expression[i] == '(':
                    start = i
            fin = start + expression[start:].index(')')
            temp = expression[start+1:fin]
            result = get_rational_result(temp)
            return get_rational_result(f'{expression[:start]}{result}{expression[fin+1:]}')

        sign = ''
        for s in '+-*/':
            if s in expression:
                sign = s
                break
        if sign == '':
            return int(expression)
        else:
            a, b = expression.split(sign, 1)
            if sign == '*': return mult(get_rational_result(a), get_rational_result(b))
            if sign == '/': return div(get_rational_result(a), get_rational_result(b))
            if sign == '+': return summ(get_rational_result(a), get_rational_result(b))
            if sign == '-': return diff(get_rational_result(a), get_rational_result(b))
    except:
        return 'Выражение введено неверно'