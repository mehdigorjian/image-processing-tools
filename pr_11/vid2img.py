import cv2
import os
import numpy as np
import argparse

def extract_images(video_input_file_path, sep, image_output_dir_path):
    # if os.path.exists(image_output_dir_path):
    #     return
    count = 0
    print('Extracting frames from video: ', video_input_file_path)
    vidcap = cv2.VideoCapture(video_input_file_path)
    success, image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 100))  # added this line
        success, image = vidcap.read()
        # print('Read a new frame: ', success)
        if success:
            # cv2.imwrite(image_output_dir_path + os.path.sep + "frame%d.jpg" % count, image)
            cv2.imwrite(image_output_dir_path + os.path.sep + "{}_frame{}.jpg".format(sep, count), image)
            count = count + 1

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-i', '--input', help='input videos folder path')
    parse.add_argument('-m', '--mode', help='creating images in a seprate folders for each video')
    parse.add_argument('-f', '--folder_name', help='name of folder')
    args = parse.parse_args()

    # Create images in a seprate folders for each video
    def create_seprate_folder(path):
        videos = [f for f in os.listdir(path) if not f.startswith('.')]
        for i, video in enumerate(videos):
            print(i)
            f, ext = os.path.splitext(video)
            vPath = path + '/' + f + ext
            _name = 'video_' + str(i)
            name = os.path.join(path, _name)
            print('Writing Folder: ', _name)
            os.makedirs(name)
            extract_images(vPath, i, name)

    def create_images(path, folder_name):
        videos = [f for f in os.listdir(path) if not f.startswith('.')]
        (head, _) = os.path.split(path)
        name = os.path.join(head, folder_name)
        os.makedirs(name)

        for i, video in enumerate(videos):
            print(i)
            f, ext = os.path.splitext(video)
            vPath = path + '/' + f + ext
            print(vPath)
            extract_images(vPath, i, name)

    if args.mode == 'seprate':
        create_seprate_folder(args.input)
    else:
        create_images(args.input, args.folder_name)
                
# TO RUN THE CODE: python vid2img.py -i path -f folderName