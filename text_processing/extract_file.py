file = input()
file_parts = file.split("\\")
needed_parts = file_parts[-1].split(".")
file_name = needed_parts[:len(needed_parts) - 1]
file_extension = needed_parts[-1]

print(f"File name: {''.join(file_name)}\nFile extension: {file_extension}")