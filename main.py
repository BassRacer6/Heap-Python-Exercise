import heapq

def create_max_heap():
    return []

def push_max_heap(max_heap, value):
    heapq.heappush(max_heap, -value)

def pop_max_heap(max_heap):
    return -heapq.heappop(max_heap) if max_heap else None

def peek_max_heap(max_heap):
    return -max_heap[0] if max_heap else None

def heapify_list(nums):
    nums = [-num for num in nums]
    heapq.heapify(nums)
    return nums

def get_n_largest(nums, n):
    return heapq.nsmallest(n, nums)

def main():
    max_heap = create_max_heap()
    
    while True:
        print("\nMenu do Max Heap:")
        print("1. Inserir no Max Heap")
        print("2. Remover do Max Heap")
        print("3. Consultar topo do Max Heap")
        print("4. Transformar lista em Max Heap")
        print("5. Obter N maiores elementos")
        print("6. Sair")
        
        escolha = input("Digite sua escolha: ")
        
        if escolha == "1":
            valor = int(input("Digite um valor para inserir: "))
            push_max_heap(max_heap, valor)
            print("Max Heap (valores invertidos):", max_heap)
        elif escolha == "2":
            resultado = pop_max_heap(max_heap)
            print("Valor removido do max heap:", resultado)
            print("Max Heap (valores invertidos):", max_heap)
        elif escolha == "3":
            print("Topo do max heap:", peek_max_heap(max_heap))
        elif escolha == "4":
            nums = list(map(int, input("Digite os números separados por espaço: ").split()))
            max_heap = heapify_list(nums)
            print("Lista transformada em max heap:", max_heap)
        elif escolha == "5":
            n = int(input("Digite N: "))
            print("N maiores elementos:", get_n_largest(max_heap, n))
        elif escolha == "6":
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
