# 定义莫尔斯电码字典
# 打表法还是太强了
MORSE_CODE_DICT = {
    '·−': 'A', '−···': 'B', '−·−·': 'C', '−··': 'D', '·': 'E',
    '··−·': 'F', '−−·': 'G', '····': 'H', '··': 'I', '·−−−': 'J',
    '−·−': 'K', '·−··': 'L', '−−': 'M', '−·': 'N', '−−−': 'O',
    '·−−·': 'P', '−−·−': 'Q', '·−·': 'R', '···': 'S', '−': 'T',
    '··−': 'U', '···−': 'V', '·−−': 'W', '−··−': 'X', '−·−−': 'Y',
    '−−··': 'Z',
    '·−−−−': '1', '··−−−': '2', '···−−': '3', '····−': '4', '·····': '5',
    '−····': '6', '−−···': '7', '−−−··': '8', '−−−−·': '9', '−−−−−': '0'
}


def morse_to_text(morse_code: str) -> str:
    # 按单词分割（三个空格）
    words = morse_code.strip().split('   ')
    decoded_words = []

    for word in words:
        # 按字符分割（一个空格）
        letters = word.strip().split(' ')
        decoded_letters = [MORSE_CODE_DICT.get(letter, '?') for letter in letters]
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)


# 示例用法
example = '···· · −··− ·−−−   ·−− ·− ··· −'
print(morse_to_text(example))  # 输出: HEXO AXST
