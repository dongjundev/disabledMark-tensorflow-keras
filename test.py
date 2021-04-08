# from IPython.display import display
# from PIL import Image
# from yolo import YOLO
#
# def objectDetection(file, model_path, class_path):
#     yolo = YOLO(model_path=model_path, classes_path=class_path, anchors_path="model_data/yolo_anchors.txt")
#     image = Image.open(file)
#     result_image = yolo.detect_image(image)
#     display(result_image)
#     result_image.show()
#
# objectDetection('dog.png', 'model_data/yolo.h5', 'model_data/coco_classes.txt')

from IPython.display import display
from PIL import Image
from yolo import YOLO

def objectDetection(file, model_path, class_path):
    yolo = YOLO(model_path=model_path, classes_path=class_path, anchors_path='model_data/yolo_anchors.txt')
    image = Image.open(file)
    result_image = yolo.detect_image(image)
    display(result_image)
    result_image.show()

objectDetection('data/light/test/562.jpg', '', 'data/light/classes.txt')
