from transformers import MarianMTModel, MarianTokenizer






class Translator:

    def __init__(self, model_path) -> None:
        
        self.model = MarianMTModel.from_pretrained(model_path, from_flax=True)
        self.tokenizer = MarianTokenizer.from_pretrained(model_path)

        print("modele chargé. Lnagues prises en charge: ", self.model.supported_languages_codes)

