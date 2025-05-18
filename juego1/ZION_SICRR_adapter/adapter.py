# ZION_SICRR_adapter/adapter.py

import json
from pathlib import Path
from sicrr_tools import some_tool_function  # Adjust import as needed
from sicrr_analytics import analyze_player
from sicrr_model_trainer import train_model

BASE_DIR = Path(__file__).resolve().parent
MEMORY_FILE = BASE_DIR.parent.parent / 'SICRR' / 'memoria.json'
PERSONALITY_FILE = BASE_DIR.parent.parent / 'SICRR' / 'personalidad.json'

class SICRRAdapter:
    def __init__(self):
        # Load memory and personality
        self.memory = self._load_json(MEMORY_FILE)
        self.personality = self._load_json(PERSONALITY_FILE)

    def _load_json(self, path):
        if not path.exists():
            return {}
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_json(self, path, data):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def record_action(self, player_id, action, context=None):
        entry = {'action': action, 'context': context}
        self.memory.setdefault(player_id, []).append(entry)
        self._save_json(MEMORY_FILE, self.memory)

    def get_personality(self, player_id):
        return self.personality.get(player_id, {})

    def evaluate_player(self, player_id):
        player_memory = self.memory.get(player_id, [])
        return analyze_player(player_memory)

    def train_on_memory(self, player_id):
        player_memory = self.memory.get(player_id, [])
        train_model(player_memory)
        return True

# Example usage
if __name__ == "__main__":
    adapter = SICRRAdapter()
    adapter.record_action('user123', 'entered_zone', {'zone': 'Valle de los Orcos'})
    print('Personality:', adapter.get_personality('user123'))
    print('Evaluation:', adapter.evaluate_player('user123'))
