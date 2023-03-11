from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import shutil

def convert_to_mp3(file_path):
    clip = VideoFileClip(file_path)
    clip.audio.write_audiofile(file_path.replace(".avi", ".mp3"))


def move_files(src_folder, dst_folder):
    src_files = os.listdir(src_folder)
    for file_name in src_files:
        full_file_name = os.path.join(src_folder, file_name)
        if (os.path.isfile(full_file_name)):
            if full_file_name.endswith(".avi"):
                convert_to_mp3(full_file_name)
                shutil.move(full_file_name.replace(".avi", ".mp3"), dst_folder)


if __name__ == "__main__":
    src_folder = "./Film"
    dst_folder = "./Audio"
    move_files(src_folder, dst_folder)
