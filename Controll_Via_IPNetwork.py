import tkinter as tk
import threading
import socket

# Dummy filter and other functions (assuming these are defined in your existing modules)
from Dummy_filter import apply_dummy_filter
from RGB_TO_Monochrome_Filter import display_grayscale
from sharpener_filter import sharpen_image
from Brightness_Correction import BrightneesCorrection
from Threshold_Filter import Threshold
from Median_Filter import MedianFilter
from HDM_Video import Video_Function
from HDM_RealTime import Webcam_Detection_Function

# Function to apply filters based on the checkbox selections
def apply_filters():
    if dummy_var.get():
        apply_dummy_filter('0b9aec984321bf53.jpg')
    if grayscale_var.get():
        display_grayscale('0b9aec984321bf53.jpg')
    if sharpen_var.get():
        sharpen_image('0b9aec984321bf53.jpg')
    if brightness_var.get():
        BrightneesCorrection('0b9aec984321bf53.jpg')
    if threshold_var.get():
        Threshold('0b9aec984321bf53.jpg')
    if median_var.get():
        MedianFilter('0b9aec984321bf53.jpg')
    if Video_var.get():
        Video_Function()
    if RealTime_var.get():
        Webcam_Detection_Function()

# Function to handle each client connection
def handle_client_connection(client_socket):
    while True:
        try:
            command = client_socket.recv(1024).decode('utf-8')
            if command:
                print(f"Received command: {command}")
                # Execute the corresponding function
                if command == 'apply_dummy_filter':
                    dummy_var.set(1)
                elif command == 'display_grayscale':
                    grayscale_var.set(1)
                elif command == 'apply_sharpening_filter':
                    sharpen_var.set(1)
                elif command == 'apply_brightness_correction':
                    brightness_var.set(1)
                elif command == 'apply_threshold_filter':
                    threshold_var.set(1)
                elif command == 'apply_median_filter':
                    median_var.set(1)
                elif command == 'start_video_function':
                    Video_var.set(1)
                elif command == 'start_webcam_detection':
                    RealTime_var.set(1)

                # Apply the filters
                apply_filters()
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()

# The function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('172.20.10.8', 5000))
    server.listen(5)
    print("Server listening on port 8080")

    while True:
        client_sock, address = server.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client_connection, args=(client_sock,))
        client_handler.start()

# Tkinter GUI Setup
root = tk.Tk()
root.title("Filter Selection Interface")

# Variables to track the status of each filter
dummy_var = tk.IntVar()
grayscale_var = tk.IntVar()
sharpen_var = tk.IntVar()
brightness_var = tk.IntVar()
threshold_var = tk.IntVar()
median_var = tk.IntVar()
Video_var = tk.IntVar()
RealTime_var = tk.IntVar()

# Checkboxes to activate/deactivate filters
tk.Checkbutton(root, text="Apply Dummy Filter", variable=dummy_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Display Grayscale", variable=grayscale_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Sharpening Filter", variable=sharpen_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Brightness Correction", variable=brightness_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Threshold Filter", variable=threshold_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Median Filter", variable=median_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Start Video Function", variable=Video_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Start Webcam Detection", variable=RealTime_var).pack(anchor=tk.W)

# Button to apply selected filters
tk.Button(root, text="Apply Filters", command=apply_filters).pack()

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

# Start the Tkinter main loop
root.mainloop()
