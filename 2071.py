T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    num_sum = 0
    count = 0
    print(num)
    for i in num:
        num_sum += i
        count += 1
    result = round(num_sum / count)
    print(f'#{tc} {result}')