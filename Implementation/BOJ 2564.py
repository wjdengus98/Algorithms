# 백준 2564번
# 경비원

def cal_dist(loc, dst):
    if loc == 1:    # 북쪽
        return dst
    elif loc == 4:  # 동쪽
        return w + dst
    elif loc == 2:  # 남쪽
        return w + h + (w - dst)
    elif loc == 3:  # 서쪽
        return w + h + w + (h - dst)

w, h = map(int, input().split())
area = 2 * w + 2 * h

n = int(input())

locations = []
for i in range(n):
    loc_dir, loc_dst = map(int, input().split())
    locations.append((loc_dir, loc_dst))

dong_dir, dong_dst = map(int, input().split())
dong = cal_dist(dong_dir, dong_dst)

min_val = 0

for loc_dir, loc_dst in locations:
    dist = cal_dist(loc_dir, loc_dst)
    clock = abs(dist - dong)
    reverse_clock = area - clock
    min_val += min(clock, reverse_clock)

print(min_val)
      