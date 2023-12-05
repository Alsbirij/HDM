def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_contents(contents):
    parsed_data = {}
    for line in contents:
        parts = line.strip().split(': ')
        if len(parts) == 2:
            image_name, count = parts
            parsed_data[image_name] = int(count)
    return parsed_data

def compare_and_write_results(file_1_data, file_2_data, result_file_path):
    with open(result_file_path, 'w') as file:
        for image_name, count_1 in file_1_data.items():
            count_2 = file_2_data.get(image_name, None)
            if count_2 is not None:
                if count_1 == count_2:
                    file.write(f"{image_name}: Match ({count_1} people)\n")
                else:
                    file.write(f"{image_name}: Mismatch (Original: {count_1}, Predicted: {count_2})\n")
            else:
                file.write(f"{image_name}: Not found in second file\n")

# Example usage
file_path_1 = 'result_1.txt'  #  the path to the  first file
file_path_2 = 'result_2.txt'  #  the path to the second file
result_file_path = 'path_to_result_file.txt'  #  the result file

contents_1 = read_file(file_path_1)
contents_2 = read_file(file_path_2)

parsed_contents_1 = parse_contents(contents_1)
parsed_contents_2 = parse_contents(contents_2)

compare_and_write_results(parsed_contents_1, parsed_contents_2, result_file_path)
