import json
import os


class ReaderType:
    def __init__(self, config_file='swagger_server/utils/Readers/JSON/types.json'):
        self.config_file = config_file
        self.data = self._load_json()

    def _load_json(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"El archivo {self.config_file} no se encuentra.")
        with open(self.config_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_type_list(self, type_key):
        types = self.data.get('TYPES', {})
        return types.get(type_key.upper(), [])
