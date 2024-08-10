from typing import List
import re

def split_v1(string: str) -> List :
    result = []
    words = re.findall(r'\S+', string)
    for i in words:
        if(i != ''):
            result.append(i)
    return result

print(split_v1('Hola, mi nombre es Luis. ¿Cómo estás?'))
