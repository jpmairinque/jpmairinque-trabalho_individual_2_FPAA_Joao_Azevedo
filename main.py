from functions import *

if __name__ == "__main__":    
    try:
        arr = list(map(int, input("Digite uma série de números separados por espaço: ").split()))
        if not arr:
            raise ValueError("A lista não pode estar vazia.")
        min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
        print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")