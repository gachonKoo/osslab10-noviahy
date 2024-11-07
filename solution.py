
import sys

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    # 명령줄 인수로 입력 받기
    number = int(sys.argv[1])
    
    # 약수 구하기
    divisors = get_divisors(number)
    
    # 출력
    print(" ".join(map(str, divisors)))
