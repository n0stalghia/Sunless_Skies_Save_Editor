import json


def open_savefile(file_name):
    with open(file_name) as json_file:
        save_file = json.load(json_file)
    return save_file


def get_value(save_file, key, val_id):
    query = next((quality for quality in save_file['QualitiesPossessedList'] if quality['AssociatedQuality']['Id'] ==
                  val_id), None)
    return str(query[key]) if key in query else '0'
