import re


def anime_info_changer(text: str) -> str:
    return re.sub('.*: ', '',text)

def anime_slug_changer(text: str) -> str:
    return re.sub('.*/', '',text.rstrip('/'))