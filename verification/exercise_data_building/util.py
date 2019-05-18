from os import listdir

def get_single_file(directory, str):
    # TODO: throw if more than a single file matches
    for object_name in listdir(directory):
        if str in object_name:
            return object_name
        


