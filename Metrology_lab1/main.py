import re
from collections import Counter


def count_operators_and_operands(file):
    with open(file, 'r') as f:
        code = f.read()
    # Операторы
    operators = ['+', '-', '*', '/', '%', '++', '--', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '->', '.']
    # Операнды
    operands = []
    # Используем регулярные выражения для поиска операндов
    pattern = re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*\b')
    for line in code.splitlines():
        # Удаляем комментарии и строки
        line = re.sub(r'//.*', '', line)
        line = re.sub(r'".*?"', '', line)
        line = re.sub(r"'.*?'", '', line)
        matches = pattern.findall(line)
        operands.extend(matches)
    operator_counts = Counter(filter(lambda x: x in operators, code))
    operand_counts = Counter(operands)
    return operator_counts, operand_counts
#
# def count_nesting(file):
#     with open(file, 'r') as f:
#         code = f.read()
#     nesting_level = 0
#     stack = []
#     # Используем регулярные выражения для поиска блоков условных операторов
#     pattern = re.compile(r'\b(if|else|for|while)\b')
#     for line in code.splitlines():
#         matches = pattern.findall(line)
#         for match in matches:
#             if match in ['if', 'else']:
#                 stack.append(match)
#             elif match in ['for', 'while']:
#                 stack.append(match)
#                 nesting_level += 1
#             # Добавляем проверку, что стек не пустой
#             elif match == '}' and stack:
#                 last_match = stack.pop()
#                 if last_match in ['if', 'else']:
#                     if not stack or stack[-1] not in ['if', 'else']:
#                         nesting_level += 1
#                 elif last_match in ['for', 'while']:
#                     nesting_level -= 1
#     return nesting_level

def count_nesting(file):
    with open(file, 'r') as f:
        code = f.read()
    # Используем стек для отслеживания уровня вложенности
    stack = []
    max_nesting = 0
    for line in code.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('{'):
            stack.append('{')
            if len(stack) > max_nesting:
                max_nesting = len(stack)
        elif line.startswith('}'):
            try:
                stack.pop()
            except Exception as e:
                pass
    # Возвращаем максимальный уровень вложенности
    return max_nesting

def count_variables(file):
    with open(file, 'r') as f:
        code = f.read()
    # Используем регулярные выражения для поиска объявлений переменных
    variable_pattern = re.compile(r'\b(int|float|double|char|bool|string)\s+\w+\b')
    variables = variable_pattern.findall(code)
    # Возвращаем словарь с количеством переменных каждого типа
    var_count = {}
    for var in variables:
        var_type = var.split()[0]
        if var_type in var_count:
            var_count[var_type] += 1
        else:
            var_count[var_type] = 1
    return var_count

def count_classes_and_objects(file):
    class_counts = {}
    object_counts = {}
    with open(file, 'r') as f:
        for line in f:
            if line.strip().startswith('class '):
                class_name = line.strip().split()[1]
                class_counts[class_name] = class_counts.get(class_name, 0) + 1
            elif 'new ' in line:
                for class_name in class_counts:
                    if class_name in line:
                        object_counts[class_name] = object_counts.get(class_name, 0) + 1
    return class_counts, object_counts

file = 'example.cpp'
max_nesting = count_nesting(file)
file = 'example.cpp'
var_count = count_variables(file)
print(f"Количество переменных каждого типа: {var_count}")
print(f"Максимальный уровень вложенности: {max_nesting}")

operator_counts, operand_counts = count_operators_and_operands(file)
print('Operators:')
for operator, count in operator_counts.items():
    print(f'{operator}: {count}')
print('Operands:')
for operand, count in operand_counts.items():
    print(f'{operand}: {count}')

class_counts, object_counts = count_classes_and_objects(file)
print('Classes:')
for class_name, count in class_counts.items():
    print(f'{class_name}: {count}')
print('Objects:')
for class_name, count in object_counts.items():
    print(f'{class_name} objects: {count}')
