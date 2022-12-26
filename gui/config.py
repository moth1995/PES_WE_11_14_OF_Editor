import yaml
from pathlib import Path
import os
from editor import common_functions

class Config:
    current_dir = os.getcwd()
    config_dir = current_dir + '/' + "config"
    default_file = common_functions.resource_path("resources/default.yaml")
    is_default = False

    filelist = []
    games_config = []

    def __init__(self,file:str=None):
        self.filelist = []
        self.games_config = []

        self.get_config_files(self.config_dir)

        self.file_location = self.check_if_default(file)

        self.load_config()

    def check_if_default(self, file:str):
        if file is None:
            file = self.load_default()
            self.is_default = True
        else: 
            self.is_default = False
        return file        

    def load_default(self):
        """
        If we didn't found any setting file we land here, it will try to load any config file, the first that founds
        otherwise it will load from the resources folder

        Returns:
            str: location of configuration file
        """
        return self.default_file if os.listdir(self.config_dir) == [] else self.filelist[0]

    def load_config(self):
        
        stream = open(self.file_location)
        self.file = yaml.safe_load(stream)
        stream.close()

    def get_config_files(self, directory:str):
        
        if not self.is_default:
            try:
                for p in Path(directory).iterdir():
                    if p.is_file():
                        self.filelist.append(directory + "/" + p.name)
                        parent = p.parent
                        if parent.name != "config":
                            #print(parent.name)
                            self.games_config.append(parent.name + ":" + p.stem)
                        else:
                            #print("main dir",parent.name)
                            self.games_config.append(p.stem)
                    elif p.is_dir():
                        self.get_config_files(directory + "/" + p.name)
            except Exception as e:
                self.filelist = []
                self.games_config = []
