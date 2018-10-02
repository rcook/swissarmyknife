import datetime
import exifread
import os

def rename(source_path):
    with open(source_path, "rb") as f:
        tags = exifread.process_file(f)
        d = datetime.datetime.strptime(str(tags["EXIF DateTimeDigitized"]), "%Y:%m:%d %H:%M:%S")

    source_dir = os.path.dirname(source_path)
    source_file_name = os.path.basename(source_path)

    target_file_name = "{0:04d}{1:02d}{2:02d}-{3}".format(d.year, d.month, d.day, source_file_name)
    target_dir = os.path.join(
        source_dir,
        os.path.join("{0:04d}".format(d.year), "{0:04d}-{1:02d}".format(d.year, d.month)))
    target_path = os.path.join(
        target_dir,
        target_file_name)

    print(target_path)

def scan(start_dir):
    for file_name in os.listdir(start_dir):
        _, ext = os.path.splitext(file_name)
        if ext == ".jpg":
            source_path = os.path.join(start_dir, file_name)
            rename(source_path)

scan("/home/rcook/Downloads")