def convert_12_to_24(time_12h):
    return str(int(time_12h[:-6]) % 12 + 12 * (time_12h[-2:] == 'PM')).zfill(2) + time_12h[2:5]

def convert_24_to_12(time_24h):
    return str(int(time_24h[:2]) % 12 or 12) + time_24h[2:] + (' PM' if int(time_24h[:2]) >= 12 else ' AM')

time_12h = "3:45 PM"
time_24h = "21:30"

converted_24h = convert_12_to_24(time_12h)
converted_12h = convert_24_to_12(time_24h)

print(f"12-часовой формат '{time_12h}' конвертирован в 24-часовой формат: '{converted_24h}'")
print(f"24-часовой формат '{time_24h}' конвертирован в 12-часовой формат: '{converted_12h}'")