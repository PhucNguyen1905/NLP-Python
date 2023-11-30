from typing import List
from models.Const import *


def writeData(file: str, mode: str, data: str) -> None:
    with open(file, mode, encoding='utf8') as f:
        f.write(data)


def queryInfo(database: str, *filterData) -> List[str]:
    data = None
    with open('./data/{}.txt'.format(database), "r", encoding='utf8') as f:
        data = f.readlines()

    for key in filterData:
        if "?" not in key:
            data = list(filter(lambda x: key in x, data))

    return data

PHRASE = (
    ("máy bay", "máy_bay"),
    ("thời gian", "thời_gian"),
    ("thành phố", "thành_phố"),
    ("tp.", "thành_phố "),
    ("đà nẵng", "đà_nẵng"),
    ("nha trang", "nha_trang"),
    ("hồ chí minh", "hồ_chí_minh"),
    ("hà nội", "hà_nội"),
    ("hải phòng", "hải_phòng"),
    ("khánh hòa", "khánh_hòa"),
    ("mấy giờ", "mấy_giờ"),
    ("bao lâu", "bao_lâu"),
    ("xuất phát", "xuất_phát"),
    ("khởi hành", "khởi_hành"),
    ("hạ cánh", "hạ_cánh"),
    ("hãy cho biết", "hãy_cho_biết"),
)

def tokenize(text: str) -> List[str]:
    text = text.lower()
    text = text.replace(',', ' , ')
    
    for phrase, word in PHRASE:
        text = text.replace(phrase, word)
    tokens = text.split()
    if tokens[-1].endswith('?') and tokens[-1] != '?':
        last_element_parts = tokens[-1].split('?')
        tokens.pop()
        tokens.append(last_element_parts[0])
        tokens.append('?')
    return tokens


PLANES = set(map(lambda x: str.lower(x.split()[1]), queryInfo("plane")))

def getWordTypes(tokens: List[str]) -> List[str]:
    types = []

    for i, token in enumerate(tokens):
        if token in DICTIONARY:
            if isinstance(DICTIONARY[token], str):
                types.append(DICTIONARY[token])
            else:
                index = i
                while index > 0:
                    index -= 1
                    if types[index] == "Prep":
                        types.append(DICTIONARY[token][1])
                        break
                else:
                    types.append(DICTIONARY[token][0])    
        elif token in CITY:
            types.append("Name")
        else:
            types.append("ID" if token in PLANES else "Time")
                
    return types

