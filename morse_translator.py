import enum
import sys

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


# ···· · ·−·· ·−·· −−−   ·−− −−− ·−· ·−·· −··
# · · · ·   ·   · − · ·   · − · ·   − − −       · − −   − − −   · − ·   · − · ·   − · ·
class MorseCode:
    def __init__(self):
        # elements = None
        # input_string = None
        # is_short_code = None
        pass


class MorseCodeType(enum.Enum):
    INVALID = -1
    COMPACT = 1
    SPACED = 2
    STANDARD = 3


def translate(input_string: str):
    preparing_str = input_string.strip().replace('.', '·').replace('-', '−')
    # print(preparing_str)

    elements = get_elements(preparing_str)
    # print(elements)

    if not contain_valid_element_number(elements):
        sys.exit('Invalid element number')

    # print(elements == {'·', '−'})

    if not elements == {'·', '−'}:
        preparing_str = element_reassignment(list(elements), preparing_str)

    print(preparing_str)

    format_type = detect_morse_format(preparing_str)

    print(format_type)

    if format_type == MorseCodeType.INVALID:
        pass
    elif format_type == MorseCodeType.SPACED:
        preparing_str = convert_spaced_to_standard(preparing_str)
    elif format_type == MorseCodeType.COMPACT:
        preparing_str = convert_compact_to_standard(preparing_str)

    print(preparing_str)
    print(morse_to_text(preparing_str))

    # 示例用法
    # example = '···· · −··− ·−−−   ·−− ·− ··· −'
    # print(morse_to_text(example))  # 输出: HEXO AXST
    # if not is_valid_code(input_string):
    #     sys.exit('Unsupported format')


def get_elements(s):
    chars = s.replace(' / ', '').replace(' ', '')
    unique_chars = set(chars)
    return unique_chars


def contain_valid_element_number(element_set):
    return len(element_set) == 1 or len(element_set) == 2


def element_reassignment(element_list, preparing: str):
    if len(element_list) == 2:
        asking = \
            f"""
Which relationship is you want: 
1. {element_list[0]} for - , {element_list[1]} for · ;
2. {element_list[1]} for - , {element_list[0]} for ·
"""
        ans = input(asking)
        if ans == '1':
            preparing = preparing.replace(element_list[0], '−').replace(element_list[1], '·')
        elif ans == '2':
            preparing = preparing.replace(element_list[1], '−').replace(element_list[0], '·')
        else:
            sys.exit('Enter Something')
    else:
        asking = \
            f"""
Which relationship is you want: 
1. {element_list[0]} for - ;
2. {element_list[0]} for ·
"""
        ans = input(asking)
        if ans == '1':
            preparing = preparing.replace(element_list[0], '−')
        elif ans == '2':
            preparing = preparing.replace(element_list[0], '·')
        else:
            sys.exit('Enter Something')

    return preparing


def is_standard_format(s: str) -> bool:
    valid_signals = {'·', '−'}
    if '/' not in s:
        return False
    words = s.split('/')
    for word in words:
        letters = word.strip().split()
        for letter in letters:
            if not all(ch in valid_signals for ch in letter):
                return False
    return True


def is_spaced_format(s: str) -> bool:
    valid_signals = {'·', '−'}
    if '       ' in s and '   ' in s:
        words = s.split('       ')
        for word in words:
            letters = word.strip().split('   ')
            for letter in letters:
                signals = letter.strip().split(' ')
                if not all(all(ch in valid_signals for ch in sig) for sig in signals):
                    return False
        return True
    return False


def is_compact_format(s: str) -> bool:
    valid_signals = {'·', '−'}
    if '   ' in s:
        words = s.split('   ')
        for word in words:
            letters = word.strip().split(' ')
            if not all(all(ch in valid_signals for ch in letter) for letter in letters):
                return False
        return True
    return False


def detect_morse_format(morse_str: str) -> MorseCodeType:
    """
    自动识别莫尔斯电码的格式：
    - COMPACT：紧凑格式（信号无间隔，字母间1空格，单词间3空格）
    - SPACED：分隔格式（信号间1空格，字母间3空格，单词间7空格）
    - STANDARD：标准格式（信号无空格，字母间1空格，单词间用 '/' 分隔）
    - INVALID：格式不明或不合规
    """
    morse_str = morse_str.strip()
    if not morse_str:
        return MorseCodeType.INVALID

    if is_standard_format(morse_str):
        return MorseCodeType.STANDARD
    elif is_spaced_format(morse_str):
        return MorseCodeType.SPACED
    elif is_compact_format(morse_str):
        return MorseCodeType.COMPACT
    else:
        return MorseCodeType.INVALID


def convert_spaced_to_standard(raw: str) -> str:
    """
    将 SPACED 格式（信号之间有空格，字母间3空格，单词间7空格）转换为 STANDARD 格式。
    STANDARD 格式：字母之间1空格，单词之间使用 '/' 分隔
    """
    raw = raw.strip()
    words = raw.split('       ')  # 单词间7个空格
    result_words = []

    for word in words:
        letters = word.strip().split('   ')  # 字母间3个空格
        cleaned_letters = []
        for letter in letters:
            cleaned = letter.replace(' ', '')  # 去除信号间空格
            cleaned_letters.append(cleaned)
        result_words.append(' '.join(cleaned_letters))

    return ' / '.join(result_words)


def convert_compact_to_standard(raw: str) -> str:
    """
    将 COMPACT 格式（字母为连续信号，字母间1空格，单词间3空格）转换为 STANDARD 格式。
    STANDARD 格式：字母之间1空格，单词之间使用 '/' 分隔
    """
    raw = raw.strip()
    words = raw.split('   ')  # 单词间3个空格
    result_words = []

    for word in words:
        letters = word.strip().split(' ')  # 字母间1空格
        result_words.append(' '.join(letters))

    return ' / '.join(result_words)


def morse_to_text(morse_code: str) -> str:
    # 按单词分割（三个空格）
    words = morse_code.strip().split(' / ')
    decoded_words = []

    for word in words:
        # 按字符分割（一个空格）
        letters = word.strip().split(' ')
        decoded_letters = [MORSE_CODE_DICT.get(letter, '?') for letter in letters]
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)


def compress_morse(morse_str: str) -> str:
    """
    将分隔格式的莫尔斯电码转换为紧凑格式：
    - 每个字母由多个点/划组成，之间无空格
    - 字母之间保留3个空格，单词之间保留7个空格
    """

    result = []
    # 首先按单词分割（7个空格）
    words = morse_str.strip().split('       ')  # 分隔单词

    for word in words:
        compressed_letters = []
        # 按字母分割（3个空格）
        letters = word.strip().split('   ')
        for letter in letters:
            # 去掉字母中每个信号之间的空格
            compressed = letter.replace(' ', '')
            compressed_letters.append(compressed)
        # 将字母组合成单词（用3个空格连接）
        result.append('   '.join(compressed_letters))

    # 最终将单词组合起来（用7个空格连接）
    return '       '.join(result)


translate(input())
