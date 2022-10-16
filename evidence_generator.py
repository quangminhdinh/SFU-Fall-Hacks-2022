from dotenv import load_dotenv
import os
import replicate
load_dotenv()

class EvidenceGenerator:

    def __init__(self):
        self.REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
    
    def acquire_evidence(self):
        model = replicate.models.get("stability-ai/stable-diffusion")
        return model.predict(prompt="doctor in a hospital room, with anime style")[0]