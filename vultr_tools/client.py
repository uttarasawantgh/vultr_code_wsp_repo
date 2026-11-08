import os
from openai import OpenAI

class VultrInferenceClient:
    """
    Client wrapper for Vultr Serverless Inference serving models via an OpenAI-compatible REST API.
    """
    def __init__(self):
        self.api_key = os.getenv("VULTR_SERVERLESS_INFERENCE_API_KEY")
        self.base_url = os.getenv("VULTR_BASE_URL", "https://api.vultrinference.com/v1")
        
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key
        )

    def generate_code_patch(self, prompt: str, model_name: str = "llama-3.3-70b-instruct") -> str:
        """
        Synthesizes weight-patching or code execution scripts via Vultr Serverless.
        """
        response = self.client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system", 
                    "content": "You are an expert AI weight-surgeon and Python developer. Output clean executable code blocks."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0.2
        )
        return response.choices[0].message.content