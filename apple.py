A = 0
B = 0
money = 1_000_000
apple_price = 30_000
strawberry_price = 16_000

# 1차 목표: 사과 박스 개수를 최대한 늘린다
A += 1
while True:
    price = A * apple_price + B * strawberry_price
    change = money - price
    if change < 0:
        A -= 1
        price = A * apple_price + B * strawberry_price
        change = money - price
        break 
    A += 1
# 2차 목표: 사과박스 개수를 하나씩 줄여가며
# A > B 큰 선에서 총 박스 수를 늘린다

sums = []
while True:
    price = A * apple_price + B * strawberry_price
    change = money - price
    if change > 0:
        while True:
            B += 1
            price = A * apple_price + B * strawberry_price
            change = money - price
            if change < 0:
                B -= 1
                break
    sums.append([A, B])
    A -= 1
    if A <= B:
        break
# 3차 목표: 모든 가능한 A> B 조합에서
# A+B가 가장 큰 원소를 골- 라 출력한다
hap = 0
idx = 0
for i, s in enumerate(sums):
    a = s[0]
    b = s[1]
    if a + b > hap:
        hap = a + b
        idx = i

print(sums)
print(sums[idx])

