# import sys
#
#
# class MorseCode:
#     def __init__(self):
#         input_string = input()
#         if not self.is_valid_code(input_string):
#             sys.exit('Unsupported format')
#
#
#     @staticmethod
#     def get_elements(s):
#         chars = s.replace(' ', '')
#         unique_chars = set(chars)
#         return unique_chars
#
#
#     @staticmethod
#     def is_valid_code(s):
#         chars = s.replace(' ', '')
#         unique_chars = set(chars)
#         return len(unique_chars) == 1 or len(unique_chars) == 2
#
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