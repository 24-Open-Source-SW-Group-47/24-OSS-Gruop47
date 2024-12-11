# Vision-Based Object Mosaic

This project uses the YOLOv3 model to detect specific objects in an image and applies a mosaic effect to the detected areas. Users can specify the image path, the object to mosaic, and the mosaic strength.

## Features

- **Object Detection** using the YOLOv3 model.
- Mosaic processing for user-specified objects (e.g., person, car, dog).
- Adjustable mosaic strength (1 ~ 100).
- Visualization of the result.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy
- YOLOv3 weights and configuration files (`yolov3.weights`, `yolov3.cfg`)
- COCO class names file (`coco.names`)

You can install the required Python packages with:

```bash
pip install opencv-python numpy
```

## Preparation

1. **Download YOLOv3 model files**
    
    - [YOLOv3.weights (Darknet official)](https://pjreddie.com/media/files/yolov3.weights)
    - [YOLOv3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
    
    Place these files in the same directory as the script.
    
2. **Download COCO class names file**
    
    - Download the [COCO class names file](https://github.com/pjreddie/darknet/blob/master/data/coco.names) and place it in the project directory.

## How to Run

```bash
python mosaic.py
```

Follow the steps in the terminal:

1. Enter the image path:
    
    ```
    Enter the image path: sample.jpg
    ```
    
    - For an image in the current folder: `sample.jpg`
    - Absolute or relative paths are supported.
2. Enter the target object name:
    
    ```
    Enter the target object name: person
    ```
    
    - Specify the object to mosaic from the COCO dataset (e.g., `person`, `car`, `dog`).
3. Enter the mosaic strength (1 ~ 100):
    
    ```
    Enter the mosaic strength (1 ~ 100): 50
    ```
    

After completing these steps, the program will process the image, apply the mosaic effect to the specified objects, and display the result in a popup window.

## Output

- The processed image with the mosaic effect will be displayed in a separate window.
- Closing the window will exit the program.

## Example Screenshot
- ![Example 1](https://github.com/jkyu03/24-OSS-Gruop47/blob/main/202434641%20%EC%9C%A0%EC%A0%95%EA%B7%9C/src/image/e1.PNG)
- ![Example 2](https://github.com/jkyu03/24-OSS-Gruop47/blob/main/202434641%20%EC%9C%A0%EC%A0%95%EA%B7%9C/src/image/e2.PNG)
## Notes

- The script uses the YOLOv3 model, which may not detect objects perfectly. For better accuracy, consider using newer models like YOLOv4 or YOLOv5.
- Higher mosaic strength values make the object areas more blurred.
- The detection result depends on the image resolution and the model's performance.

## License

This project is licensed under the MIT License.
