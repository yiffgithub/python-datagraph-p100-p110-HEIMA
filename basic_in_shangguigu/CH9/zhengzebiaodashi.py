import re

# 匹配数字序列
numbers_pattern = r'\d+'
number_string = '1234234234'
match_numbers = re.match(numbers_pattern, number_string)
print(match_numbers.group(0)) if match_numbers else print('No match')

# 匹配包含字母和数字的字符串
alphanum_pattern = r'\w+'
alphanum_string = 'a8'
match_alphanum = re.match(alphanum_pattern, alphanum_string)
print(match_alphanum.group(0)) if match_alphanum else print('No match')

# 匹配空白字符
space_pattern = r'\s+'
space_string = '   '
match_space = re.match(space_pattern, space_string)
print('Matched whitespace') if match_space else print('No match')
