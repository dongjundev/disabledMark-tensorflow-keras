import random
import numpy as np
class RandomHorizontalFlip(object):
    def __init__(self, p=0.5):
        self.p = p

    def __call__(self, img, bboxes):
        img_center = np.array(img.shape[:2])[::-1]/2
        img_center = img_center.astype(int)
        img_center = np.hstack((img_center, img_center))
        if random.random() < self.p:
            img = img[:, ::-1, :]
            bboxes[:, [0, 2]] += 2*(img_center[[0, 2]] - bboxes[:, [0, 2]])
            box_w = abs(bboxes[:, 0] - bboxes[:, 2])
            bboxes[:, 0] -= box_w
            bboxes[:, 2] += box_w
        return img, bboxes