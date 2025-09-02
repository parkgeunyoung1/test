T = int(input())                      # T 삽입
for tc in range(1, T+1):              # tc 생성
    num = list(map(int, input().split()))  # 숫자열 리스트 생성
    num_sum = 0          # 초기 숫자합
    for i in num:        # 숫자열리스트 순회
        if i % 2 == 1:   # 홀수(나머지가 1)찾기
            num_sum += i # 홀수 더하기
 
    print(f'#{tc} {num_sum}')