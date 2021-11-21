import cv2

def simple_paste(src_path, mask_path, target_path, resize=None):
    src = cv2.imread(src_path)
    mask = cv2.imread(mask_path)
    target = cv2.imread(target_path)
    if resize is not None:
        src = cv2.resize(src, resize)
        mask = cv2.resize(mask, resize)
        target = cv2.resize(target, resize)
    a = cv2.bitwise_and(src, mask)    # 大豆のみ
    n_mask = cv2.bitwise_not(mask)
    b = cv2.bitwise_and(target, n_mask)
    result = a + b
    cv2.imwrite("out.png", result)
    return
