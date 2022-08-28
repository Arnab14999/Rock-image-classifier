# Rock-image-classifier
In this project I have used Convolutional Neural Network to classify rock images to 7 classes namely basalt, granite, coal, limestone, sandstone, quartzite, marble.

Trained the images in a batch size of 8 using a CNN.

Firstly the images were colected from Kaggle dataset and then they were resized into 512 X 512 pixels using resizer.py.
After resizing the data was augumented and resized and rescaled so that the limitation of less data was compensetated.
Accuracy of 60% was achieved initially. The model could detect coal and sandstone well than limestones and quartzite.
