# Задача: 
# Сохранить резервную копию excel-таблицы. (Для восстановления после сбоя)
#   I. В csv
    # 1.
#   II. В pg

# Замечания:
# Для смерженных ячеек значение остаётся только в правой-верхней.
    # Как проверить наличие смержа для ячейки?
    #   1. Считать минимальную пустую область под правой-верхней ячейкой
    #      (если это не конец листа)
    #      областью этой ячейки.

# Ранг (максимальный квадратный диапазон) sheet.calculate_dimension()
import openpyxl
wb = openpyxl.load_workbook('./resources/test_wb.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

# 1. Найти ячейки ФИО, Дата --проверить уникальность на ПРОДе 
# 2. Найти ячейки ФИО, Дата --проверить уникальность на ПРОДе 
h_counter = 0
while True:
    header = sheet.cell(row=1, column=1)
    h_counter = h_counter + 1
    if header.value is None:
        h_counter
