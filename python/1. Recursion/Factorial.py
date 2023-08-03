def factorial(n):                 # 함수 정의
  if n == 0:                      # 구하고자 하는 n값이 0에 도달할 경우
    return 1                      # 1로 반환
  return factorial(n - 1) * n     # 아닐 경우, 다음 Factorial 값과 구하고자 하는 값의 곱을 반환

print(factorial(4))               # 결과 출력

# 위의 Factorial을 반복문으로 풀 경우

result = 1                        # 결과로 출력할 값을 1로 정의

for i in range(4):                # 0부터 3까지 총 4번 반복
  result = result * (i + 1)       # 기존에 정의한 1에 (i + 1)을 곱해줌

print(result)                     # 결과값 출력