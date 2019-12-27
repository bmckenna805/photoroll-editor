import glob
import os
from PIL import Image


def open_image(path):
    try:
        image = Image.open(path)
    except IOError:
        print('Error opening file with Pillow')
        pass
    return image


def rotate_image(image, degrees, path):
    rotated_image = image.rotate(degrees)
    rotated_image.save(path)


def flip_image(image, path):
    transposed_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    # Saved in the same relative location
    transposed_image.save(path)


def delete_image(path):
    try:
        os.remove(path)
        print('File {} deleted'.format(path))
    except IOError:
        print('Could not delete {}'.format(path))


def gen_image_list(path):
    """Returns a list of images generated from
    the contents of path"""
    globpath = os.path.join(path, '*.jpg')
    for filename in glob.glob(globpath):
        yield filename


if __name__ == "__main__":
    command = ''
    raw_path = input('What path would you like to find images in?: ')
    if os.path.isdir(raw_path):
        path = raw_path
        print('Looking for photos in {}'.format(path))
    else:
        print('Path is invalid')
    for image_path in gen_image_list(path):
        while command != 'n':
            image = open_image(image_path)
            image.show()
            print('1.  Rotate Image')
            print('2.  Flip Image')
            print('3.  Delete Image')
            print('4.  Next Image')
            raw_command = input('What operatione?(1-4): ')
            if raw_command == '1':
                rotate_image(image, 90, image_path)
                image.close()
            elif raw_command == '2':
                flip_image(image, image_path)
                image.close()
            elif raw_command == '3':
                delete_image(image_path)
                command = 'n'
                image.close()
            elif raw_command == '4':
                command = 'n'
                image.close()
            else:
                print('Please enter a number between 1 and 4')
        command = ''
