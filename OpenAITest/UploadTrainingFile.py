from pathlib import Path
from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open(Path(__file__).parent / "training_bdabot.jsonl", "rb"),
  purpose="fine-tune"
)