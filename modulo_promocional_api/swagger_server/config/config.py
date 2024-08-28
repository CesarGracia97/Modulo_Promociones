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

    def set_token(self, token):
        self.config['TOKER']['TOKEN_GEN'] = token
        with open(self.config_file_path, 'w') as file:
            json.dump(self.config, file, indent=4)

    def delete_token(self):
        self.config['TOKER']['TOKEN_GEN'] = ""
        with open(self.config_file_path, 'w') as file:
            json.dump(self.config, file, indent=4)


# Instancia de configuración global
config = Config()
