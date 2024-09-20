def find_divisors(n, i=1, divisors=None):
    if divisors is None:
        divisors = []
    
    if i > n:
        return divisors
    
    if n % i == 0:
        divisors.append(i)
    
    return find_divisors(n, i + 1, divisors)

def is_prime(n):
    if n <= 1:
        return False
    return len(find_divisors(n)) == 2

def main():

    while True:
        number = int(input("Введите целое число больше 0 и не превышающее 100000: "))

        if number <= 0 or number > 100000:
            print("Число должно быть больше 0 и не превышать 100000.")
            continue
            

        divisors = find_divisors(number)
        prime_status = is_prime(number)

        print(f"Делители числа {number}: {divisors}")

        if prime_status:
            print(f"Число {number} простое")
        else: 
            print(f"Число {number} не простое")        
        break

if __name__ == "__main__":
    main()
