from lib.utils import make_mask_by_threshold

def test_make_mask_by_threshold():
    image_path = "../example/soybean/P8020163.JPG"
    resize = (640,480)
    make_mask_by_threshold(image_path, resize=resize)


if __name__ == "__main__":
    test_make_mask_by_threshold()