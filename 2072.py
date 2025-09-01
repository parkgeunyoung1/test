T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    skills = list(map(int, input().split()))
    skills.sort()

    max_team = 0
    start = 0
    for end in range(N):
        while skills[end] - skills[start] > K:
            start += 1
        max_team = max(max_team, end - start + 1)

    print(f"#{test_case} {max_team}")