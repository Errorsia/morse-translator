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

def translate(self, input_string: str):

    preparing_str = input_string.strip().replace('.', '·').replace('-', '−')

    elements = self.get_elements(input_string)

    if not self.contain_valid_element_number(elements):
        sys.exit('Invalid element number')

    if not elements == {'·', '−'}:
        preparing_str = self.element_reassignment(list(elements), preparing_str)
    print(preparing_str)

    print(self.detect_morse_format(preparing_str))

    print(self.morse_to_text(preparing_str))

    # 示例用法
    # example = '···· · −··− ·−−−   ·−− ·− ··· −'
    # print(self.morse_to_text(example))  # 输出: HEXO AXST
    # if not self.is_valid_code(input_string):
    #     sys.exit('Unsupported format')

@staticmethod
def get_elements(s):
    chars = s.replace(' ', '')
    unique_chars = set(chars)
    return unique_chars

@staticmethod
def contain_valid_element_number(element_set):
    return len(element_set) == 1 or len(element_set) == 2

@staticmethod
def element_reassignment(element_set, preparing: str):
    asking = \
        f"""
    Which relationship is you want: 
    1. {element_set[0]} for - , {element_set[1]} for · ;
    2. {element_set[1]} for - , {element_set[0]} for ·
    """
    ans = input(asking)
    if ans == '1':
        preparing = preparing.replace(element_set[0], '−').replace(element_set[1], '·')
    elif ans == '2':
        preparing = preparing.replace(element_set[1], '−').replace(element_set[0], '·')
    else:
        sys.exit('Enter Something')
    return preparing

@staticmethod
def detect_morse_format(morse_str: str) -> str:
    """
    自动识别莫尔斯电码的格式：
    - 返回 'compact' 表示紧凑格式（字母信号无间隔）
    - 返回 'spaced' 表示分隔格式（信号之间有空格）
    - 返回 'invalid' 表示格式不明或不合规
    """

    morse_str = morse_str.strip()
    if not morse_str:
        return 'invalid'

    valid_signals = {'·', '−'}

    # 尝试按分隔格式分析
    if '       ' in morse_str and '   ' in morse_str:
        # 分隔格式应具备字母间3空格、单词间7空格，并且字母内部使用1空格分隔信号
        words = morse_str.split('       ')
        for word in words:
            letters = word.strip().split('   ')
            for letter in letters:
                signals = letter.strip().split(' ')
                if not all(all(ch in valid_signals for ch in sig) for sig in signals):
                    return 'invalid'
        return 'spaced'

    # 尝试按紧凑格式分析
    elif '   ' in morse_str:
        # 紧凑格式中，字母为连续信号，字母间1空格，单词间3空格
        words = morse_str.split('   ')
        for word in words:
            letters = word.strip().split(' ')
            if not all(all(ch in valid_signals for ch in letter) for letter in letters):
                return 'invalid'
        return 'compact'

    else:
        return 'invalid'

@staticmethod
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

@staticmethod
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


morse_code_module = MorseCode()
morse_code_module.translate(input())
