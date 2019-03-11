import json
from PyQt5.QtCore import Qt
from Data.globals import *


def open_json_file(file_name):
    with open(file_name, 'r') as json_file:
        save_file = json.load(json_file)
    return save_file


def save_json_file(file_name, save_file):
    with open(file_name, 'w') as json_file:
        json.dump(save_file, json_file)


def get_query(save_file, val_id):
    return next((quality for quality in save_file['QualitiesPossessedList']
                 if quality['AssociatedQuality']['Id'] == val_id), None)


def get_quality_value(save_file, val_id, key='Level'):
    query = get_query(save_file, val_id)

    if not query:
        return '0'
    return str(query[key]) if key in query else '0'


def get_current_port_name(save_file):
    region_id = save_file['GeneratedWorld']['CurrentRegionId']
    port_id = save_file['GeneratedWorld']['CurrentPortId']
    return PORTS[region_id]['Id'][port_id]['DisplayName']


def get_current_region_name(save_file):
    region_id = save_file['GeneratedWorld']['CurrentRegionId']
    return PORTS[region_id]['Name']


def get_port_list(save_file, selected_region=''):
    port_list = []
    ports = ''

    if selected_region != '':
        for region in PORTS:
            if PORTS[region]['Name'] == selected_region:
                ports = PORTS[region]['Id']
    else:
        if save_file != {}:
            region_id = save_file['GeneratedWorld']['CurrentRegionId']
            ports = PORTS[region_id]['Id']
        else:
            return ['']

    for port in ports:
        # noinspection PyTypeChecker
        port_list.append(ports[port]['DisplayName'])

    return port_list


def get_region(save_file, region_name):
    region_id = ''
    for region in PORTS:
        if PORTS[region]['Name'] == region_name:
            region_id = region
            break

    for region in save_file['GeneratedWorld']['Regions']:
        if region['Id'] == region_id:
            return region


def get_fow_state(save_file, region_name):
    region = get_region(save_file, region_name)

    if all(item is False for item in region['FogBools']):
        state = Qt.Checked
    elif all(item is True for item in region['FogBools']):
        state = Qt.Unchecked
    else:
        state = Qt.PartiallyChecked

    return state


def get_port_reports(save_file, region_name):
    ids = PORT_REPORT_IDS[region_name]
    status = [False] * len(ids)

    for index, port_id in enumerate(ids):
        for quality in save_file['QualitiesPossessedList']:
            if quality['AssociatedQuality']['Id'] == port_id:
                if 'EffectiveLevel' in quality:
                    status[index] = True
                    break
                else:
                    break

    if all(item is False for item in status):
        return Qt.Unchecked
    elif all(item is True for item in status):
        return Qt.Checked
    else:
        return Qt.PartiallyChecked


def get_heirloom(save_file, val_id):
    query = get_query(save_file, val_id)

    return True if query else False


def write_query(save_file, query):
    for index, quality in enumerate(save_file['QualitiesPossessedList']):
        if quality['AssociatedQuality']['Id'] == query['AssociatedQuality']['Id']:
            save_file['QualitiesPossessedList'][index] = query

    return save_file


def write_stats(save_file, val1, val2, val_id):
    query = get_query(save_file, val_id)

    if not query:
        query = {
            "EffectiveLevel": val1 + val2,
            "Level": val1,
            "AssociatedQuality": {
                "Tag": "",
                "Id": val_id
            }
        }

        if val2 != 0:
            query['EffectiveLevelModifier'] = val2

        save_file['QualitiesPossessedList'].append(query)
    else:
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

        save_file = write_query(save_file, query)

    return save_file


def write_current_port(save_file, port_name, cache):
    region_id = ''
    port_id = ''
    location_name = ''
    query = {}
    position = {}

    if port_name == '':
        return save_file

    # get static values from local dict
    for region in PORTS:
        for port in PORTS[region]['Id']:
            if PORTS[region]['Id'][port]['DisplayName'] == port_name:
                region_id = region
                port_id = port
                location_name = PORTS[region]['Id'][port]['InternalName']
                break

    # get dynamic values from gamesave
    for region in cache['GeneratedWorld']['Regions']:
        if region['Id'] == region_id:
            query = region
            break

    for segment in query['Segments']:
        for skyless_scene in segment:
            for landmark in skyless_scene['SkylessScene']['Landmarks']:
                if landmark['InstanceId'] == port_id:
                    position = skyless_scene['Position']
                    break

    save_file['GeneratedWorld']['CurrentRegionId'] = region_id
    save_file['GeneratedWorld']['CurrentPortId'] = port_id
    save_file['GeneratedWorld']['LocationName'] = location_name
    save_file['GeneratedWorld']['CurrentSegmentPosition'] = position

    return save_file


def write_fow_values(save_file, state, region_name):
    region = get_region(save_file, region_name)
    if state == Qt.Checked:
        new_fow = [False] * len(region['FogBools'])
    else:
        new_fow = [True] * len(region['FogBools'])

    for saved_region in save_file['GeneratedWorld']['Regions']:
        if saved_region['Id'] == region['Id']:
            saved_region['FogBools'] = new_fow
            break

    return save_file


def write_possessions(save_file, value, val_id):
    query = get_query(save_file, val_id)
    value = int(value)

    if not query:
        query = {
            "EffectiveLevel": value,
            "Level": value,
            "AssociatedQuality": {
                "Tag": "",
                "Id": val_id
            }
        }

        save_file['QualitiesPossessedList'].append(query)
    else:
        modifier = query.get('EffectiveLevelModifier', 0)

        if value == 0 and modifier != 0:
            query['EffectiveLevel'] = modifier
            if 'Level' in query:
                del query['Level']
        elif value == 0 and modifier == 0:
            if 'Level' in query:
                del query['Level']
                del query['EffectiveLevel']
                query['Name'] = ''
        else:
            query['Level'] = value
            query['EffectiveLevel'] = value + modifier

        save_file = write_query(save_file, query)

    return save_file


def write_port_reports(save_file, state, region_name):
    for report_id in PORT_REPORT_IDS[region_name]:
        query = get_query(save_file, report_id)

        if state == Qt.Checked:
            if query is None:
                query = {
                    'Name': '',
                    'EffectiveLevel': 1,
                    'Level': 1,
                    'AssociatedQuality': {
                        'Tag': '',
                        'Id': report_id
                    }
                }

                save_file['QualitiesPossessedList'].append(query)

            else:
                query['EffectiveLevel'] = 1
                query['Level'] = 1

                save_file = write_query(save_file, query)
        else:
            if query is not None and 'Level' in query:
                del query['EffectiveLevel']
                del query['Level']

            save_file = write_query(save_file, query)

    return save_file


def write_heirlooms(save_file, state, val_id):
    query = get_query(save_file, val_id)

    if state:
        if query is None:
            query = {
                'Name': '',
                'EffectiveLevel': 1,
                'Level': 1,
                'AssociatedQuality': {
                    'Tag': '',
                    'Id': val_id
                }
            }

            save_file['QualitiesPossessedList'].append(query)
    else:
        for index, quality in enumerate(save_file['QualitiesPossessedList']):
            if quality['AssociatedQuality']['Id'] == val_id:
                del save_file['QualitiesPossessedList'][index]

    return save_file


def get_cargo(save_file, cargo_id):
    name = CARGO_IDS.get(cargo_id, f'Unknown ID {cargo_id}')
    amount = str(save_file['SavedBankItems'][cargo_id])
    return name, amount
