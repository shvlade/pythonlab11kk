def safe_apply(func, data):
    results = []
    errors = []

    for element in data:
        try:
            # Пытаемся применить функцию к элементу
            result = func(element)
            results.append(result)
        except Exception as e:
            # Если возникло исключение, сохраняем элемент и ошибку
            errors.append((element, e))

    return results, errors

if __name__ == "__main__":
    # Лямбда-функция для вычисления квадратного корня
    sqrt_lambda = lambda x: float(x) ** 0.5

    test_data = ['4', '16', 'text', '-25', '9.0']
    results, errors = safe_apply(sqrt_lambda, test_data)

    print("Успешные результаты:")
    for i, (input_val, result) in enumerate(zip(test_data, results), 1):
        print(f"  {i}. ({input_val}) = {result}")

    print("\nОшибки:")
    if errors:
        for element, exception in errors:
            print(f"  Элемент: '{element}', Ошибка: {type(exception).__name__}: {exception}")
    else:
        print("Ошибок нет!")

    print("\nИтоговые данные:")
    print(f"  Results: {results}")
    print(f"  Errors: {errors}")