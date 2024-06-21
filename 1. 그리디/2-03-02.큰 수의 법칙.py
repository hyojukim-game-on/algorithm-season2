# M번 더해서 가장 큰 수 만들기
# 특정 인덱스 중복 허용하지만 최대 K번까지만 더할 수 있음
N, M, K = list(map(int, input().split()))
numbers = list(map(int, input().split()))
# 큰 수의 법칙에 따른 결과를 출력하기
# 큰 수가 앞에 오도록 정렬
numbers.sort(reverse=True)
# 가장 큰 수 K번 더하고 그 다음 수 1번 더하고 또 K 더해서 M 이 될 때까지 계속하기
sum_v = 0
total_cnt = 0
max_num_cnt = 0
while total_cnt < M:
    total_cnt += 1
    max_num_cnt += 1
    if max_num_cnt > K:
        sum_v += numbers[1]
        max_num_cnt = 0
    else:
        sum_v += numbers[0]
print(sum_v)