import os
import yaml


class ConfigLoader:
    def __init__(self, config_path: str = "config/test_config.yaml"):
        self.config_path = config_path
        self.config = self._load()

    def _load(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get(self, key, default=None):
        parts = key.split(".")
        value = self.config
        for part in parts:
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return default
        return value
