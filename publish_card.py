from huggingface_hub import HfApi, ModelCard
from dotenv import load_dotenv
import os

REPO_ID = "Math29/exo-chap2"

load_dotenv()

token = os.getenv("HF_TOKEN")

if token is None:
    raise ValueError("HF_TOKEN manquant")

api = HfApi(token=token)

# Création du repo privé
api.create_repo(
    repo_id=REPO_ID,
    repo_type="model",
    private=True,
    exist_ok=True
)

# Chargement de la Model Card
card = ModelCard.load("model_card.md")

# Push sur le Hub
card.push_to_hub(
    REPO_ID,
    token=token
)

print("Model Card publiée avec succès.")
