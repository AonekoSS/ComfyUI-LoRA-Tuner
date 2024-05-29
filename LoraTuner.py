from folder_paths import get_filename_list
from nodes import LoraLoader

LORA_COUNT = 8

class LoraTuner:
    def __init__(self):
        self.loras = [LoraLoader() for _ in range(LORA_COUNT)]

    @classmethod
    def INPUT_TYPES(cls):
        args = { "model": ("MODEL",)}
        arg_lora_name = ([""] + get_filename_list("loras"),)
        arg_strength = ("FLOAT", {"default": 1.0, "min": -2.0, "max": 2.0, "step": 0.1, "display": "slider"})
        for i in range(LORA_COUNT):
            args["{}:lora".format(i)] = arg_lora_name
            args["{}:".format(i)] = arg_strength
        return {"required": args}

    def apply(self, model, **kwargs):
        for i in range(LORA_COUNT):
            lora_name = kwargs["{}:lora".format(i)]
            strength = kwargs["{}:".format(i)]
            if lora_name != "" and strength != 0:
                model = self.loras[i].load_lora(model, None, lora_name, strength, 0)[0]
        return (model,)

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "apply"
    CATEGORY = "utils"
