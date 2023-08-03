# N번째 피보나치 수를 리턴해보자.

def fibonacci(n):                               # 피보나치 함수 정의
  if n == 1 or n == 2:                          # 피보나치 수열에서 첫번째, 두번째 n 값은 1로 고정
    return 1                                    # 1 반환
  return fibonacci(n - 1) + fibonacci(n - 2)    # n 번째 수를 기준으로 n - 1, n - 2의 합을 반환

for i in range(1, 11):                          # fibonacci(1) ~ fibonacci(10)까지의 출력
  print(fibonacci(i))