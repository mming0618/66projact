start = 36893488147419103232
end = 73786976294838206463
num_groups = 300

step = (end - start) // num_groups

with open("groups1.txt", "w") as file:
    for i in range(num_groups):
        group_start = start + i * step
        group_end = start + (i + 1) * step - 1
        group_hex_start = hex(group_start)
        group_hex_end = hex(group_end)
        file.write(f"Group {i + 1} - Start: {group_start} (Hex: {group_hex_start}), End: {group_end} (Hex: {group_hex_end})\n")

print("Data has been saved to 'groups1.txt'.")
