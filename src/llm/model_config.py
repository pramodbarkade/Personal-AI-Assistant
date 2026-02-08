import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "models.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    _config = json.load(f)

DEFAULT_MODEL = _config["default_model"]
MODELS = {m["id"]: m for m in _config["models"]}