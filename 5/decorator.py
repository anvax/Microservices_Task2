import time
import functools
import os

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнена за {execution_time:.6f} сек")
        return result
    return wrapper


@timer_decorator
def sum_and_print(a, b):
    result = a + b
    print(f"Результат сложения {a} + {b} = {result}")


@timer_decorator
def sum_from_file(input_path, output_path):
    try:
        with open(input_path, 'r') as f:
            data = f.read().split()
            a, b = map(int, data)
        
        result = a + b
        
        with open(output_path, 'w') as f:
            f.write(str(result))
        
        print(f"Считано из {input_path}, результат {result} записан в {output_path}")
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_path} не найден.")
    except ValueError:
        print("Ошибка: В файле должны быть два целых числа через пробел.")


if __name__ == "__main__":
    with open(os.path.join("5", "input.txt"), "w") as f:
        f.write("350 250")

    print("Запуск первой функции:")
    sum_and_print(10, 20)

    print("\nЗапуск второй функции:")
    sum_from_file(os.path.join("5", "input.txt"), os.path.join("5", "output.txt"))
