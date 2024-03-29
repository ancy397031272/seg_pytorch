import cv2
from utils.misc import loadYaml
from datalayer.datalayer import Datalayer
from datalayer.augmentations import get_training_augmentation

if __name__ == '__main__':

    config = loadYaml('../config/config.yaml')
    dataset = Datalayer(config=config, augmentation=get_training_augmentation())
    print(len(dataset))
    for i, (img, mask) in enumerate(dataset):
        if i == len(dataset):
            break
        cv2.namedWindow('img', 0)
        cv2.imshow('img', img)
        cv2.namedWindow('mask', 0)
        cv2.imshow('mask', mask)
        # cv2.imshow('mask', mask)
        cv2.waitKey(33)
