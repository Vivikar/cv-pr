import sys
import cv2


def take_picture():
    capture = cv2.VideoCapture(0)
    while True:
        retval, image = capture.read()
        cv2.imshow('task_1', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('task_1.jpg', image)
            break

    capture.release()
    cv2.destroyAllWindows()


def make_image_magic(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_grb_from_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
    img_grb_from_gray = cv2.line(
        img_grb_from_gray, (0, 0), (42, 42), color=(42, 42, 42), thickness=1)
    img_grb_from_gray = cv2.rectangle(
        img_grb_from_gray, (42, 42), (84, 84), color=(0, 255, 0), thickness=1)
    return img_grb_from_gray


def convert_to_grey_scale():
    img = cv2.imread('task_1.jpg')
    img_grb_from_gray = make_image_magic(img)
    cv2.imshow('task_2', img_grb_from_gray)
    cv2.imwrite('task_2.jpg', img_grb_from_gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def do_all_magic_at_once():
    capture = cv2.VideoCapture(0)
    retval, image = capture.read()

    while(True):
        cv2.imshow('Original Image', image)
        transformed_image = make_image_magic(image)
        cv2.imshow('Transformed Image', transformed_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('task_1.jpg', image)
            cv2.imwrite('task_2.jpg', transformed_image)
            cv2.destroyAllWindows()
            break

    capture.release()
    cv2.destroyAllWindows()


def record_weird_video():
    capture = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    writer = cv2.VideoWriter('task_3.avi', fourcc, 20.0, (640, 480))

    while(capture.isOpened()):
        retval, image = capture.read()
        image = make_image_magic(image)

        if retval == True:
            writer.write(image)

            cv2.imshow('Video Feed for Task 3', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    capture.release()
    writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if sys.argv[1] == 'task1':
        take_picture()
    elif sys.argv[1] == 'task2':
        convert_to_grey_scale()
    elif sys.argv[1] == 'task3':
        record_weird_video()
    elif sys.argv[1] == 'task1_2':
        do_all_magic_at_once()
    else:
        print('Provide proper arguments! Read the readme file if you are not sure.')
