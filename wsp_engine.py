# wsp_engine.py
import torch
import torch.nn as nn
import os
import shutil
from datetime import datetime

class QwenAdapterTarget(nn.Module):
    """
    Simulated target layer representing Qwen 0.5B attention/projection weights
    targeted for direct Weight-Space Programming (WSP) modification.
    """
    def __init__(self):
        super().__init__()
        self.proj = nn.Linear(8, 4, bias=True)

    def forward(self, x):
        return self.proj(x)

def save_initial_weights(path="model_weights.pt"):
    """Resets the model weights to clean baseline for demo consistency."""
    model = QwenAdapterTarget()
    torch.save(model.state_dict(), path)
    print(f"[WSP] Baseline model weights initialized at {path}")

def apply_safe_tensor_delta(weight_key: str, scale_factor: float, bias_shift: float, weights_path="model_weights.pt"):
    """
    Air-gapped safe WSP runner with timestamped artifact logging for demo recordings.
    """
    if not os.path.exists(weights_path):
        save_initial_weights(weights_path)
        
    state_dict = torch.load(weights_path)
    
    if weight_key in state_dict:
        # Apply deterministic tensor math
        state_dict[weight_key] = state_dict[weight_key] * scale_factor
        
        bias_key = weight_key.replace("weight", "bias")
        if bias_key in state_dict:
            state_dict[bias_key] = state_dict[bias_key] + bias_shift
            
        # Save current state
        torch.save(state_dict, weights_path)
        
        # CREATE TIMESTAMPED SNAPSHOT FOR DEMO AUDIT TRAIL
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_path = f"model_weights_{timestamp}.pt"
        shutil.copy(weights_path, snapshot_path)
        
        # Calculate updated tensor norms
        tensor_summary = {k: v.norm().item() for k, v in state_dict.items()}
        return {
            "status": "SUCCESS", 
            "mode": "Air-Gapped Numerical Delta Applied",
            "snapshot_saved": snapshot_path,
            "tensor_norms": tensor_summary
        }
    
    return {"status": "ERROR", "message": f"Target weight key '{weight_key}' not found."}

if __name__ == "__main__":
    save_initial_weights()