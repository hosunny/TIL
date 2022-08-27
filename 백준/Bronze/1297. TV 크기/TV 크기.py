D, H, W = map(int, input().split())
hungry = D / (((W ** 2) + (H ** 2)) ** 0.5)
print(int(H * hungry), int(W * hungry))