import json
import os


class Config:
    def __init__(self, config_file='config.json'):
        self.config_file_path = os.path.join(os.path.dirname(__file__), config_file)
        with open(self.config_file_path, 'r') as file:
            self.config = json.load(file)

    def get(self, *keys):
        value = self.config
        for key in keys:
            value = value[key]
        return value

    def set(self, value, *keys):
        config_section = self.config
        for key in keys[:-1]:
            config_section = config_section[key]
        config_section[keys[-1]] = value
        with open(self.config_file_path, 'w') as file:
            json.dump(self.config, file, indent=4)


# Instancia de configuración global
config = Config()
