import re
# from ..text.symbols import symbols
from g2pk3 import G2p
import ko2kana

import re
from jamo import h2j, j2hcj
from ..text.japanese import japanese_to_romaji_with_accent

# List of (hangul, hangul divided) pairs:
_hangul_divided = [(re.compile('%s' % x[0]), x[1]) for x in [
    ('ㅘ', 'ㅗㅏ'),
    ('ㅙ', 'ㅗㅐ'),
    ('ㅚ', 'ㅗㅣ'),
    ('ㅝ', 'ㅜㅓ'),
    ('ㅞ', 'ㅜㅔ'),
    ('ㅟ', 'ㅜㅣ'),
    ('ㅢ', 'ㅡㅣ'),
    ('ㅑ', 'ㅣㅏ'),
    ('ㅒ', 'ㅣㅐ'),
    ('ㅕ', 'ㅣㅓ'),
    ('ㅖ', 'ㅣㅔ'),
    ('ㅛ', 'ㅣㅗ'),
    ('ㅠ', 'ㅣㅜ')
]]

g2pk = G2p()

def divide_hangul(text):
    text = j2hcj(h2j(text))
    for regex, replacement in _hangul_divided:
        text = re.sub(regex, replacement, text)
    return text

def jke_cleaners(text):
    text = g2pk(text)
    text = divide_hangul(text)
    text = re.sub(r'([\u3131-\u3163])$', r'\1.', text).replace('ㅐ', 'ㅔ')
    return text


def japanese_cleaners(text):
    text = ko2kana.toKana(text)
    text = japanese_to_romaji_with_accent(text)
    text = re.sub(r'([A-Za-z])$', r'\1.', text).replace('ts', 'ʦ').replace('...', '…')
    return text