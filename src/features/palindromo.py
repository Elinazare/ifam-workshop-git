def palindromo(num:int):
    num = str(num)
    num_invertido = num[::-1]
    palindromo = num==num_invertido
    return palindromo

    
num = int(input('Valor: '))
palindromo = palindromo(num)

if palindromo:
    print("verdadeiro")
else:
    print('false')