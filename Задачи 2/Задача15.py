def remove_enemies(names, enemies):
    result = [name for name in names if name not in enemies]
    return result

all_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
enemy_list = ["Bob", "David"]

names_without_enemies = remove_enemies(all_names, enemy_list)
print("Имена без врагов:", names_without_enemies)