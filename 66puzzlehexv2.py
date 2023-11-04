start = 36893488147419103232
end = 73786976294838206463

# 计算每组的范围
num_groups = 300
group_size = (end - start) // num_groups

# 打开一个.txt文件以写入结果
with open("groups2.txt", "w") as file:
    for i in range(num_groups):
        group_start = start + i * group_size
        group_end = group_start + group_size - 1

        # 将数据转换为十六进制和十进制
        hex_start = hex(group_start)
        hex_end = hex(group_end)

        # 写入每组数据到.txt文件
        file.write(f"开始：{hex_start}  结束：{hex_end}\n")
        file.write(f"十六进制：{hex_start} - {hex_end}\n")
        file.write(f"十进制：{group_start} - {group_end}\n\n")

print("处理完成，并已保存到 groups2.txt 文件中。")
