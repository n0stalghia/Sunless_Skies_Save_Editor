import os


def get_file_path(platform):
    if platform == 'linux':
        # TODO implement linux file pathing
        return ''
    elif platform == 'darwin':
        # TODO implement macOS file pathing
        return ''
    else:
        separator = '\\'
        appdata = os.getenv('APPDATA')
        arr = appdata.split(separator)
        del arr[-1]
        appdata = separator.join(arr) + '\LocalLow\Failbetter Games\Sunless Skies\storage\characterrepository'
        return appdata


def get_display_name(file_name):
    separator = '/'
    arr = file_name.split(separator)
    return separator.join(arr[-2:])
