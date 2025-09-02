T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    num_sum = 0
    for i in num:
        if i % 2 == 1:
            num_sum += i

    print(f'#{tc} {num_sum}')