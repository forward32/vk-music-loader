import sys, os
from urllib.request import urlretrieve


"""
Usage:
    python3 simple_loader.py <filename> <dirname>

Description:
    This script takes information about all tracks inside file 'filename'
    and downloads them into folder 'dirname'.
    It skips track if it already exists in folder 'dirname'.

    File 'filename' contains information about music in next format:
        track name###track url
"""


def my_print(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def need_skip(filename):
    return os.path.exists(filename)


def create_dir(dirname):
    if not need_skip(dirname):
        os.mkdir(dirname)


"""
Replaces 'bad' symbols on '_'.
Adds '.mp3' format.
"""
def get_correct_filename(filename):
    bad_symbols = {'\\','/',':','?','*','|','<', '>', '\"', '\'', ' '}
    for c in filename:
        if c in bad_symbols:
            filename = filename.replace(c, '_')

    filename += ".mp3"
    return filename


def load_track(filename, url):
    filename = get_correct_filename(filename)
    if need_skip(filename):
        my_print("Skip track {0} - file exists\n".format(filename))
        return

    try:
        my_print("Loading track {0}...".format(filename))
        urlretrieve(url, filename)
        my_print("Done\n")
    except:
        my_print("...FAILED\n")


def load_all_tracks(tracks_filename, dirname):
    tracks_filename = os.path.abspath(tracks_filename)
    create_dir(dirname)
    cur_dir = os.getcwd()
    os.chdir(dirname)

    with open(tracks_filename) as f:
        for track in f:
            filename, url = track.split("###")
            load_track(filename, url)

    os.chdir(cur_dir)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        my_print("usage: python3 simple_loader.py <filename> <directory>\n")
        sys.exit(-1)

    tracks_filename = sys.argv[1]
    dirname = sys.argv[2]
    load_all_tracks(tracks_filename, dirname)
    sys.exit(0)
