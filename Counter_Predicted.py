import os

def count_person_labels(file_path):
    """ Count the number of lines that begin with zero in a text file. """
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip().startswith('0'):  # Check if line starts with '0'
                count += 1
    return count

def process_directory(directory_path, output_file_name, max_files=300):
    """ Process files in a directory and write counts to an output file. """
    files_processed = 0
    with open(output_file_name, 'w') as output_file:
        for filename in sorted(os.listdir(directory_path)):
            if files_processed >= max_files:
                break  # Stop after processing max_files

            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                count = count_person_labels(file_path)
                output_file.write(f"{filename}: {count}\n")
                files_processed += 1

# Directory path (change this to your actual directory path)
directory_path = r"C:\Users\Alsbirij\Desktop\alsbirij\dataset\predicted_Labels"
output_file_name = "result_2.txt"

process_directory(directory_path, output_file_name)