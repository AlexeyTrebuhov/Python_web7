# 2.	Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

#    Это пакет для массового переименования файлов в выбранной директории


import glob, os

def rename(dir):
    _count = 1
    _start_name = "Muz"      # задаем первую часть конечного имени файла
    _a = 3                   # задаем количество цифр для второй части конечного имени файла
    _second_name = 10**_a     # это будет вторая часть конечного имени файла
    _new_ext = ".mp4"        # задаем расширение для итоговых файлов
    _point_start = 3             # диапазон сохраняемого имени, начальная точка
    _point_finish = 6             # диапазон сохраняемого имени, конечная точка



    for pathAndFilename in glob.iglob(os.path.join(dir, "*.mp3")):  # применяем пеоеименование только для файлов mp3

        if _count > _second_name -1:                                  # добавляем ноли, чтобы число имело четыре знака
            numberStr = str(_count)

        elif _count > (_second_name/10 -1) and _count < _second_name:
            numberStr = "0"*(_a-3) + str(_count)

        elif _count > (_second_name/100 -1) and _count < _second_name/10:
            numberStr = "0"*(_a-2) + str(_count)

        elif _count < _second_name/100:
            numberStr = "0"*(_a-1) + str(_count)

        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        new_filename = title[_point_start:_point_finish] + _start_name + "_" + numberStr             # добавляем порядковый номер к имени файла
        os.rename(pathAndFilename, os.path.join(dir, new_filename + _new_ext))
        _count = _count + 1

rename(r'D:\Audio') # размещение папки с файлами для переименования

if __name__ == "__main__":
    print()