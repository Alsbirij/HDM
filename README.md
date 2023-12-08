# HDM_2
I have divided the dataset, which I downloaded from the open-source Open Images repository, into two folders: 'Images' and 'Labels'.
Following this, the images will be fed into my YOLOv3 model. 
This model will process the images to predict the presence of persons, and the results will be stored as text files in a folder named 'Predicted Labels'.

Subsequently, I will execute two Python scripts, named 'Counter 1' and 'Counter 2'.
These scripts will count the number of persons in the images, with 'Counter 1' focusing on the original labels and 'Counter 2' on the predicted labels. 
The results from these counts will be stored in two separate text files.

The final step involves a Python script named 'Comparator'. 
This script will read both text files, compare the results for each image, and store the comparisons in a text file.
This file will list the name of each image along with a flag indicating a match or mismatch. 
A match occurs when the number of persons predicted by the model equals the number in the original label.


The interface.py implements a GUI using Tkinter to control different filters
1.Dummy_filter
2.RGB_TO_Monochrome_Filter 
3.sharpener_filter
4.Brightness_Correction
5.Threshold_Filter
6.Median_Filter
7.HDM_Video
8. HDM_RealTime



