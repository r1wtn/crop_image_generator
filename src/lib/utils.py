import cv2
import numpy as np
import os
from typing import List, Optional, Tuple


def make_mask_from_png(image_path: str) -> None:
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    mask = cv2.cvtColor(image[:,:,-1], cv2.COLOR_GRAY2BGR)
    save_dir = os.path.dirname(image_path)
    file_name = os.path.basename(image_path)
    save_path = os.path.join(save_dir, file_name.split(".png")[0]+"_mask.png")
    cv2.imwrite(save_path, mask)
    return 


def make_mask_by_threshold(
        image_path: str,
        out_dir: Optional[str] = "../outputs/",
        resize: Optional[Tuple[int]] = None,
        inf: Optional[Tuple[int]] = (36, 0, 0),
        sup: Optional[Tuple[int]] = (86, 255, 255)
    ) -> None:
    image = cv2.imread(image_path)
    if resize is not None:
        image = cv2.resize(image, resize)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    bin_img = cv2.inRange(hsv, inf, sup)
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(bin_img)
    for contour in contours:
        cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
    mask[:,0] = 0
    mask[0,:] = 0
    mask[:,-1] = 0
    mask[-1,:] = 0

    # save process
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    file_name = os.path.basename(image_path).split(".")[0]
    if resize is not None:
        file_name += "_resize"
    img_path = os.path.join(out_dir, file_name+".png")
    mask_path = os.path.join(out_dir, file_name+"_mask.png")
    cv2.imwrite(img_path, image)
    cv2.imwrite(mask_path, mask)
    return
