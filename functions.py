def max_min_select(arr, left, right):
    # Caso base: apenas um elemento
    if left == right: # mesma posição 
        return arr[left], arr[left] # retorna o único elemento do array

    # Caso base: dois elementos
    if right == left + 1: # posições sequenciais
        if arr[left] < arr[right]: # se o primeiro for menor que o segundo
            return arr[left], arr[right] # retorna ordem resultante
        else: # senão
            return arr[right], arr[left] # retorna ordem inversa

    # Divisão do problema
    middle = (left + right) // 2 # encontra o meio do array
    min_left, max_left = max_min_select(arr, left, middle) # primeira chamada recursiva para primeira metade
    min_right, max_right = max_min_select(arr, middle + 1, right) # segunda chamada recursiva para segunda metade

    # Combinação dos resultados
    min_final = min(min_left, min_right) # menor valor entre dois
    max_final = max(max_left, max_right) # maior valor entre dois

    return min_final, max_final # retorno final

