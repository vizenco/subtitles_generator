from modules import extract_speeches as extractor
from modules import model

from os import path as p

init_path = p.realpath("..")+r"\data\model\HELSINKI_NLP"
print(init_path)
e = model.Translator(init_path)

#m = model.Translator()
