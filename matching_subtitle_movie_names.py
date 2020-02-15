import os
import re

# Sample base_folder = "/Volumes/Archive/learning/Udemy.Python.Django.Dev.To.Deployment.Q1_p30download.com/code"

base_folder = "/Volumes/Archive/learning/Udemy.Python.Django.Dev.To.Deployment.Q1_p30download.com/code"
folders = os.listdir(base_folder)
if '.DS_Store' in folders:
    folders.remove('.DS_Store')

def change_filenames(folders):
    for folder in folders:

        path = base_folder + "/" + folder
        files = os.listdir(path)
        srt_files = []
        movie_files = []
        file_names = []
        for i in files:

            if re.match(".*srt", i):
                file_name = i[:(len(i)-4)]
                srt_files.append(i)
                file_names.append(file_name)
            if re.match(".*mp4", i) or re.match(".*mkv", i):
                movie_files.append(i)


        srt_files = sorted(srt_files)
        movie_files = sorted(movie_files)
        file_names = sorted(file_names)

        for i in range(len(movie_files)):

                os.rename(path+"/"+ movie_files[i], path+"/"+file_names[i]+".mp4")


if __name__ == "__main__":
    change_filenames(folders)

