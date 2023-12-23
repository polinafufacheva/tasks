original_dict = {
"apple": 2,
"banana": 3,
"orange": 5,
"kiwi": 1,
"peach": 4
}
keys = list(original_dict.keys())
values = list(original_dict.values())
keys[0], keys[-1] = keys[-1], keys[0]
values[0], values[-1] = values[-1], values[0]
swapped_dict = dict(zip(keys, values))
del swapped_dict[list(swapped_dict.keys())[1]]
swapped_dict["new_key"] = "new_value"
print(swapped_dict)