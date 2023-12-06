def calculate_match_ratio(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_entries = 300
    match_count = sum(1 for line in lines if "Match" in line)

    match_ratio = match_count / total_entries
    return match_ratio

# Replace 'your_file_path.txt' with the path to your file
file_path = 'path_to_result_file.txt'
match_ratio = calculate_match_ratio(file_path)
print(f"Match Ratio: {match_ratio}")
