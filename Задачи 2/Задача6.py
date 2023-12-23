def total_volume(*boxes):
    total = 0
    for box in boxes:
        volume = 1
        for dimension in box:
            volume *= dimension
        total += volume
    return total

box1 = [(2, 3, 4)]
box2 = [(5, 6, 7)]