from .LoraTuner import LoraTuner

NODE_CLASS_MAPPINGS = {
    "LoraTuner": LoraTuner
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoraTuner": "LoRA Tuner"
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
