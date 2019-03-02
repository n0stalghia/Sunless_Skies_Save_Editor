import json


def open_savefile(file_name):
    with open(file_name) as json_file:
        save_file = json.load(json_file)
    return save_file


def get_value(save_file, key, val_id):
    query = next((quality for quality in save_file['QualitiesPossessedList'] if quality['AssociatedQuality']['Id'] ==
                  val_id), None)
    return str(query[key]) if key in query else '0'


def write_values(save_file, val1, val2, val_id):
    query = next((quality for quality in save_file['QualitiesPossessedList'] if quality['AssociatedQuality']['Id'] ==
                  val_id), None)

    if val1 == 0:
        if 'Level' in query:
            del query['Level']
    else:
        query['Level'] = val1

    if val2 == 0:
        if 'EffectiveLevelModifier' in query:
            del query['EffectiveLevelModifier']
    else:
        query['EffectiveLevelModifier'] = val2

    if (val1 + val2) == 0:
        if 'EffectiveLevel' in query:
            del query['EffectiveLevel']
    else:
        query['EffectiveLevel'] = val1 + val2

    for index, quality in enumerate(save_file['QualitiesPossessedList']):
        if quality['AssociatedQuality']['Id'] == val_id:
            save_file['QualitiesPossessedList'][index] = query

    return save_file
