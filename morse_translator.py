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