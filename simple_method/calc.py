def calc(expression):
    allowed = '+-*/'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Expression must contain at least one character ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a,b: a+b,
                    '-': lambda a,b: a-b,
                    '*': lambda a,b: a*b,
                    '/': lambda a,b: a/b
                }[sign] (left, right)
            except (ValueError, TypeError):
                raise ValueError('Expression must contain 2 integers and 1 sign')


if __name__ == '__main__':
    print(calc('2/3'))
