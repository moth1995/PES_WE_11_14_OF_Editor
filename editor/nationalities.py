import csv
from .utils import common_functions

def get_nation(nations, idx:int):
    return nations[idx] if 0 <= idx < len(nations) else nations[nations.index("Free Nationality")]

def get_nation_idx(nations, nation:str):
    return nations.index(nation) if nation in nations else nations.index("Free Nationality")

def get_nationality_by_demonyms(dem:str):
    csv_file = csv.reader(open(common_functions.resource_path('resources/demonyms.csv'), "r", encoding='utf-8'), delimiter=",")
    for row in csv_file:
        if row[0].lower() == dem.lower():
             return (row[1])
    return "Free Nationality"

def get_demonyms_by_nationality(nat:str):
    csv_file = csv.reader(open(common_functions.resource_path('resources/demonyms.csv'), "r", encoding='utf-8'), delimiter=",")
    for row in csv_file:
        if row[1].lower() == nat.lower():
             return (row[0])
    return "Free Nationality"
