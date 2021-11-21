from lib.poisson import poisson_blend
import numpy as np
import cv2

def test_paste_soybean():
    src_path = "../outputs/P8020163_resize.png"
    mask_path = "../outputs/P8020163_resize_mask.png"
    target_path = "../example/background/PB190524.JPG"

    src = np.array(cv2.resize(cv2.imread(src_path), (640,480)) / 255.0, dtype=np.float32)
    _mask = np.array(cv2.resize(cv2.imread(mask_path, 0),(640,480)) / 255.0, dtype=np.uint8)
    _, mask = cv2.threshold(_mask, 0, 255, cv2.THRESH_OTSU)
    mask = mask / 255.0
    target = np.array(cv2.resize(cv2.imread(target_path, 1), (640,480)) / 255.0, dtype=np.float32)
    result, _ = poisson_blend(src, mask, target, "import", "../outputs")

    cv2.imwrite("../outputs/poisson.png", result)


if __name__ == "__main__":
    test_paste_soybean()