import sys
def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = parts[3].strip()
    return {"timestamp": timestamp, "level": level, "message": message}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Текстовий файл логів не знайдений")
    except Exception as e:
        print(f"Виникла помилка: {e}")    
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs)) 

def count_logs_by_level(logs: list) -> dict:
    log_counts = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARNING":0}
    for log in logs:
        log_counts[log["level"]] += 1
    return log_counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("----------------------------")
    for level, count in counts.items():
        print(f"{level}\t\t | {count}")
    
def display_logs(logs: list, level: str):    
    filter_logs = filter_logs_by_level(logs, level)
    if filter_logs:
        print(f"Деталі логів для рівня '{level}':")
        for log in filter_logs:
            print(f"{log['timestamp']} - {log['message']}")  
    else:
        print("Логи відсутні.")          
  
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Некоректна команда. Шаблон: python zacha_3 шлях до файлу логів [необов'язковий аргумент]")
    
    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) == 3:
        display_logs(logs, sys.argv[2].upper())

#python zadacha_3.pu /prohramyvania/projects/goit_algo_hw_05/example_log.txt
#Виникла проблема при запуску з консолі в наступному рядку виводить "Python" і все, більше нічого не відбувається. 
#Тому не впевнений що скрипт працює коректно.




