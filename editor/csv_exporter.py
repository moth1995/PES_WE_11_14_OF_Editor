import csv
from . import Player
from .utils.constants import *

def create_csv(filename:str):
    csv_exporter = open(filename, WRITE_MODE,newline=NEWLINE, encoding=UTF_8)
    csv_creator = csv.writer(csv_exporter)       
    csv_creator.writerow(CSV_COLUMNS)
    csv_exporter.close()

def write_players(filename:str, players:'list[Player]'):
    csv_writer = open(filename, APPEND_MODE,newline=NEWLINE, encoding=UTF_8)
    csv_out=csv.writer(csv_writer)
    for player in players:
        try:
            if player is None:continue
            player.init_stats()
            csv_out.writerow(
                [player.idx, player.name, player.shirt_name, player.callname(), player.nation()]
                #+ player.basic_settings()[:-1] # we skip the growth type int value
                #+ [player.basic_settings.growth_type.get_growth_type_name()]
                + player.basic_settings()
                + [player.basic_settings.growth_type.get_growth_type_name()]
                + player.position()
                + player.abilities()
                + player.abilities_1_8()
                + player.special_abilities()
                + player.appearance()[:9]
                + [player.appearance.body_type]
                + [val() for val in player.appearance.body_parameters]
                + [player.national_team_name, player.club_team_name, NO_YES[player.free_agent]]
            )
        except:
            pass
        
    csv_writer.close()


