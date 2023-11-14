#==========================================================
# Kelompok 8 : Fadjri Adha Putra Kuswara	| 1301190395
#              Adela Corissa                | 1301190419
#==========================================================

def searchtoken(tokens,terminals) :
    for count in tokens :
        if count not in terminals :
            return False
    return True

def lexical(tokens,teminals) :
    for count in tokens :
        if count in terminals :
            print(count," IS VALID")
        else :
            print(count," ISN'T VALID")

# Bentuk grammar dan String yang diterima oleh program Parser
        
non_terminals = ['S', 'NN', 'VB']
terminals = ['mama','baba','dada','dirisha','chakula','mlango','begi','anamwuliza','kuleta','kufunga']

parse_table = {}
parse_table[('S', 'mama')] = ['NN', 'VB', 'NN']
parse_table[('S', 'baba')] = ['NN', 'VB', 'NN']
parse_table[('S', 'dada')] = ['NN', 'VB','NN']
parse_table[('S', 'dirisha')] = ['NN', 'VB','NN']
parse_table[('S', 'chakula')] = ['NN', 'VB','NN']
parse_table[('S', 'mlango')] = ['NN', 'VB','NN']
parse_table[('S', 'begi')] = ['NN', 'VB','NN']
parse_table[('S', 'anamwuliza')] = ['error']
parse_table[('S', 'kuleta')] = ['error']
parse_table[('S', 'kufunga')] = ['error']
parse_table[('S', 'EOS')] = ['error']
parse_table[('NN', 'mama')] = ['mama']
parse_table[('NN', 'baba')] = ['baba']
parse_table[('NN', 'dada')] = ['dada']
parse_table[('NN', 'dirisha')] = ['dirisha']
parse_table[('NN', 'chakula')] = ['chakula']
parse_table[('NN', 'mlango')] = ['mlango']
parse_table[('NN', 'begi')] = ['begi']
parse_table[('NN', 'anamwuliza')] = ['error']
parse_table[('NN', 'kuleta')] = ['error']
parse_table[('NN', 'kufunga')] = ['error']
parse_table[('NN', 'EOS')] = ['error']
parse_table[('VB', 'mama')] = ['error']
parse_table[('VB', 'baba')] = ['error']
parse_table[('VB', 'dada')] = ['error']
parse_table[('VB', 'dirisha')] = ['error']
parse_table[('VB', 'chakula')] = ['error']
parse_table[('VB', 'mlango')] = ['error']
parse_table[('VB', 'begi')] = ['error']
parse_table[('VB', 'anamwuliza')] = ['anamwuliza']
parse_table[('VB', 'kuleta')] = ['kuleta']
parse_table[('VB', 'kufunga')] = ['kufunga']
parse_table[('VB', 'EOS')] = ['error']

print('Daftar Kata :')
print(terminals)

sentence = input('Masukan Sentence : ')
tokens = sentence.lower().split()

item = searchtoken(tokens,terminals)
if item == False:
    print("Kata atau kalimat tidak sesuai")
lexical(tokens,terminals)
while tokens != 'exit' and item == True:  

    tokens.append('EOS')
    stack = ['#','S']
    indext = 0
    symbol = tokens[0]

    while (len(stack) > 0):
        top = stack[len(stack)-1]
        if top in terminals:
            if top == symbol:
                stack.pop()
                indext += 1
                symbol = tokens[indext]
                if symbol == 'EOS':
                    stack.pop()
            else:
                break
        elif top in non_terminals:
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbols_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                    stack.append(symbols_to_be_pushed[i])
            else:
                break
        else:
            break

    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('STRING', sentence, 'DITERIMA')
        print()
    else:
        print('ERROR! :', sentence, ' TIDAK SESUAI DENGAN GRAMMAR')
        print()
        
    sentence = input('Input your sentence: ')
    tokens = sentence.lower().split()
    item = searchtoken(tokens,terminals)
    lexical(tokens,terminals)
print('EXITED')
  