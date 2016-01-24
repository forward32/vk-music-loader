This is simple music-downloader from vk.com.

1) server.py - simple application using Flask as framework,
which saves information about your audio into file on disk.

Usage:
  python3 server.py

2) saver.py - script takes information about all tracks inside
file on disk and downloads them into corresponding folder.
It skips track if it already exists in corresponding folder.
File on disk contains information about music in next format:
  track name###track url

Usage:
  python3 saver.py <file> <folder>
