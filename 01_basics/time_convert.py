total_seconds = 3725

hours = total_seconds // 3600
rest = total_seconds % 3600

minutes = rest // 60
second = rest % 60

print(f"{hours} ч {minutes} мин {second} сек")