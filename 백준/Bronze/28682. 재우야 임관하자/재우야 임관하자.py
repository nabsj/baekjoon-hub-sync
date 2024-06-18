#수영, 축구, 볼링
# 몬티홀, 세과목중 두과목을 f 받고 한과목 pass
import sys

n = int(input().strip())

lst = ["swimming", "bowling", "soccer"]

# 항상 'swimming'을 Pass라고 가정하고 제출
sys.stdout.write(" ".join(["swimming"] * n) + "\n")
sys.stdout.flush()

# 교수님으로부터 F를 받은 과목 받기
failures = input().strip().split()
res = []
for fail_i in failures:
    remaining = [o for o in lst if (o != fail_i) and (o != "swimming")]
    res.append(remaining[0])

sys.stdout.write(" ".join(res) + "\n")
sys.stdout.flush()