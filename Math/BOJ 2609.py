#백준 2609번
#최대공약수와 최소공배수
import math

a,b = map(int,input().split())

print(math.gcd(a,b)) #최대공약수
print(math.lcm(a,b)) #최소공배수