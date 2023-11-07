

----------------imageProcessing1 is to add a value to each pixel of a picture-------------
cd imageProcessing1
docker build -t imageprocessing1 .   
docker run -p 8080:5000 imageprocessing1
curl -X POST -F "image=@@path/to/yourImage.jpg" -F "value=10.0" http://127.0.0.1:8080/process_image -o path/to/processedImage.jpeg    
