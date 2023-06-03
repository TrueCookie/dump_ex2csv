import openpyxl
import csv
import os, sys
from datetime import datetime

SOURCE_FILE =       'C:/dev/__bite_dev/sc_meta/ex2pg/files/source.xlsx'
DUMP_DIR  =         'C:/dev/__bite_dev/sc_meta/ex2pg/files/dump/'
DUMP_STATE_FILE =   'C:/dev/__bite_dev/sc_meta/ex2pg/files/dump/.dump.state'
LOG_PATH =          'C:/dev/__bite_dev/sc_meta/ex2pg/files/save2csv.log'
EMERGENCY_PATH =    'C:/log'

source_file = ""
dump_dir  = ""
dump_state_file = ""
log_path = ""

# Записать лог
def log(level: str, message: str, path=None):
    if path is None:
        path = log_path

    time = datetime.now().strftime('%H:%M:%S')
    message = f"{time} {level}: {message}\n"

    # в файл
    with open(path, 'a', encoding='utf-8') as f:
        f.write(message)

    # в вывод
    print(message)

def emergency_log(msg: str):
    log("ERROR", f"Произошла ошибка: {msg}", EMERGENCY_PATH)

# Сохранить дамп
def dump_save(source: str, dump_dir: str):
    DUMP_FILENAME = 'dump'
    
    wb = openpyxl.load_workbook(source)
    sh = wb.active  #wb['Sheet1']

    
    savetime = datetime.now().strftime('%d.%m.%Y - %H.%M')
    dump = dump_dir + DUMP_FILENAME + '_' + savetime + '.csv'

    with open(dump, 'w', newline='', encoding='utf-8') as f:
        f_writer = csv.writer(f)
        for row in sh.rows:
            f_writer.writerow([cell.value for cell in row])

    log("INFO", f"Записан новый файл дампа: {dump}")

# Очистить дамп
def dump_cleanup(dump_dir: str):
    file_list = [file for file in os.listdir(dump_dir)]
    file_list.remove('.dump.state')

    if len(file_list) > 30:
        file_list.sort()
        os.remove(dump_dir + file_list[0])

        log("INFO", "Дамп очищен")

# Обновить .dump.state
def dump_update(source_file: str, dump_dir: str, dump_state_file: str):
    # file_state получили 
    file_state = datetime.fromtimestamp(
                    os.path.getmtime(source_file)
                ).strftime('%Y.%m.%d - %H.%M')
    
    # сравнили
    with open(dump_state_file, 'r', encoding='utf-8') as f:
        last_state = f.read()

    # если не равны
    if last_state is None or file_state != last_state:
        # 1.сохранили dump
        dump_save(source_file, dump_dir)

        # 2.записали новый last_state
        with open(dump_state_file, 'w', encoding='utf-8') as f:
            f.write(file_state)
    else:
        log("INFO", "Отслеживаемый Excel-файл не обновлялся")

    # исполнить dump policy (очистить дамп)
    dump_cleanup(dump_dir)

# Создать директории для файлов утилиты
def dump_prep(source, work_dir):
    global source_file
    global dump_dir
    global dump_state_file
    global log_path

    if source == "" and work_dir == "":
        source_file = SOURCE_FILE
        dump_dir  = DUMP_DIR
        dump_state_file = DUMP_STATE_FILE
        log_path = LOG_PATH
        log("INFO", f"РЕЖИМ ОТЛАДКИ")
    else:
        if not os.path.exists(source):
            raise FileNotFoundError("Указан неверный путь к отслеживаемому файлу (\"source\").")
        
        source_file = source
        dump_dir = work_dir + "/dump/"
        dump_state_file = work_dir + "/dump/.dump.state"
        log_path = work_dir + "/save2csv.log"

        if not os.path.exists(work_dir):
            os.mkdir(work_dir)
            os.mkdir(dump_dir)
            open(dump_state_file, 'a').close()
            open(log_path, 'a').close()
            log("INFO", f"Создана директория для файлов утилиты: {work_dir}")

def main(source, work_dir):    
    dump_prep(source, work_dir)
    dump_update(source_file, dump_dir, dump_state_file)


if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except Exception as ex:
            emergency_log(str(ex))
