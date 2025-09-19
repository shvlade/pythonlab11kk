import re


def analyze_logs(log_text):
    results = {}

    # 1. Поиск IPv4 адресов
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = re.findall(ip_pattern, log_text)
    results['ip_addresses'] = ip_addresses

    # 2. Поиск временных меток
    timestamp_pattern = r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b'
    timestamps = re.findall(timestamp_pattern, log_text)
    results['timestamps'] = timestamps

    # 3. Поиск слов в UPPERCASE
    uppercase_pattern = r'\b[A-ZА-Я]{2,}\b'
    uppercase_words = re.findall(uppercase_pattern, log_text)
    results['uppercase_words'] = uppercase_words

    # 4. Замена email-адресов
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    protected_log = re.sub(email_pattern, '[EMAIL PROTECTED]', log_text)
    results['protected_log'] = protected_log

    return results


def main():

    log_text = """
2023-10-15 14:30:25 Сервер запущен. IP: 192.168.1.1
2023-10-15 14:35:40 Пользователь ADMIN вошел в систему с IP 10.0.0.45
2023-10-15 14:40:15 ОШИБКА: Соединение с 8.8.8.8 прервано
2023-10-15 14:45:30 Отправлено письмо на email: user@example.com
2023-10-15 14:50:00 Получено письмо от admin@server.com
2023-10-15 14:55:45 КРИТИЧЕСКАЯ ОШИБКА в модуле SECURITY
2023-10-15 15:00:10 DNS запрос к 1.1.1.1 неуспешен
2023-10-15 15:05:25 Пользователь TESTUSER вышел из системы
2023-10-15 15:10:40 Резервное копирование завершено УСПЕШНО
"""
    results = analyze_logs(log_text)
    
    print("\n1. Найденные IPv4 адреса:")
    for ip in results['ip_addresses']:
        print(f"   - {ip}")

    print("\n2. Найденные временные метки:")
    for timestamp in results['timestamps']:
        print(f"   - {timestamp}")

    print("\n3. Найденные UPPERCASE")
    for word in results['uppercase_words']:
        print(f"   - {word}")

    print("\n4. Лог с защищенными email-адресами:")
    print(results['protected_log'])


if __name__ == "__main__":
    main()