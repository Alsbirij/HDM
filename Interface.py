import tkinter as tk
from Dummy_filter import apply_dummy_filter
from RGB_TO_Monochrome_Filter import  display_grayscale
from sharpener_filter import sharpen_image
from Brightness_Correction import BrightneesCorrection
from Threshold_Filter import Threshold
from Median_Filter import MedianFilter
from HDM_Video import  Video_Function
from HDM_RealTime import Webcam_Detection_Function

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
        



  
           

root = tk.Tk()
root.title("Filter Selection Interface")

# Create variables to track the status of each filter
dummy_var = tk.IntVar()
grayscale_var = tk.IntVar()
sharpen_var = tk.IntVar()
brightness_var = tk.IntVar()
threshold_var = tk.IntVar()
median_var  = tk.IntVar()
Video_var  = tk.IntVar()
RealTime_var = tk.IntVar()



# Checkboxes to activate/deactivate filters
tk.Checkbutton(root, text="Apply Dummy Filter", variable=dummy_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Display Grayscale", variable=grayscale_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Sharpening Filter", variable=sharpen_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Brightness Correction", variable=brightness_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Threshold Filter", variable=threshold_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Video Filter", variable=Video_var).pack(anchor=tk.W)
tk.Checkbutton(root, text="Apply Real Time Detection Filter", variable=RealTime_var).pack(anchor=tk.W)

# Button to apply selected filters
tk.Button(root, text="Apply Filters", command=apply_filters).pack()

root.mainloop()