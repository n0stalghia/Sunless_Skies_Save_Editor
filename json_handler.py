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


def get_quality_value(save_file, val_id, key='EffectiveLevel'):
    query = next((quality for quality in save_file['QualitiesPossessedList'] if quality['AssociatedQuality']['Id'] ==
                  val_id), None)
    if not query:
        return '0'
    return str(query[key]) if key in query else '0'


def write_stats(save_file, val1, val2, val_id):
    query = next((quality for quality in save_file['QualitiesPossessedList'] if quality['AssociatedQuality']['Id'] ==
                  val_id), None)
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

        for index, quality in enumerate(save_file['QualitiesPossessedList']):
            if quality['AssociatedQuality']['Id'] == val_id:
                save_file['QualitiesPossessedList'][index] = query

    return save_file


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

    if all(item != True for item in region['FogBools']):
        state = Qt.Checked
    elif all(item == True for item in region['FogBools']):
        state = Qt.Unchecked
    else:
        state = Qt.PartiallyChecked

    return state


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


def get_port_reports(save_file):
    return Qt.Unchecked


def get_heirloom(save_file, param):
    return Qt.Unchecked