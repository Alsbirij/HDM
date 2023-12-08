import socket

def send_command(command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000)) # replace localhost with the ip-adress of the server in this case my laptop
                                               # und port 
    client_socket.send(command.encode())
    client_socket.close()

if __name__ == "__main__":
    # Example commands
    commands = ['apply_dummy_filter', 'display_grayscale', 'apply_sharpening_filter', 'apply_brightness_correction', 'apply_threshold_filter', 'apply_median_filter', 'start_video_function', 'start_webcam_detection']

    # Send each command to the server
    #for cmd in commands:
    #print(f"Sending command: {cmd}")
    send_command(commands[0])
