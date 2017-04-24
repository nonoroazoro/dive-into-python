def test():
    student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

    print(student)

    if ('Rose' in student):
        print('Rose in')
    else:
        print('Rose out')

    a = set('abracadabra')
    b = set('alacazam')

    print(a)
    print(a - b)
    print(a | b)
    print(a & b)
    print(a ^ b)
