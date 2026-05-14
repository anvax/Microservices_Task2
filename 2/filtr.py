def filter_strings(lambdaf, strings):
    return [s for s in strings if lambdaf(s)]

test = ["apple", "banana", "hello world", "cat", "algorithm", "python", "A-node", " "]


no_spaces = filter_strings(lambda s: ' ' not in s, test)
print(f"Без пробелов: {no_spaces}")

no_starts_with_a = filter_strings(lambda s: not s.startswith('a'), test)
print(f"Не начинаются на A: {no_starts_with_a}")

long_enough = filter_strings(lambda s: len(s) >= 5, test)
print(f"Длина >= 5: {long_enough}")
