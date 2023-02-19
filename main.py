# https://infostart.ru/1c/articles/126363/
import glob
import os
import datetime
import shutil

# Настройки:
# Путь к основному каталогу откуда надо копировать
pathtodata = "C:/_from"
# Название каталогов, которые надо копировать с их содержимым:
whatbackup = ["Folder_01",
              "Folder_02",
              "Folder_03"]
# делаем каталог для копий по текущему времени
# по умолчанию должен быть создан каталог c:/_to/
dt = datetime.datetime.now()
# Можно использовать карнентдейт как название папки архива
currentdate = dt.strftime('%Y_%m_%d-%H%M')
# эта команда зачем-то создавала папку в корне диска "С"
#os.mkdir('c:/_to' + currentdate)

for org in whatbackup:
    print(org + " копирование...")
    # скопируем все каталоги в созданный каталог, копируем дерево (откуда - куда)
    shutil.copytree('' + pathtodata + '/' + org + '', 'c:/_to/' + currentdate + '/' + org + '/')

# заархивируем все что скопировано
names = glob.glob('c:/_to/' + currentdate + '/*')
for name in names:
    if os.path.isdir(name):
        # заархивировать все name используем 7zip
        print(name + " архивирование каталога...")
        # ключ -df удаляет скопированные каталоги после архивирования

        # r - ниже делает вывод сообщений архиватора в экран консоли. Пример: os.system(r'"C:\Program Files\
        ## os.system(r'"C:\Program Files\7-Zip\7z.exe"' +  zip_options + 'c:\_to\archive.zip c:\_from'' + name + ' ' + name + ' ')
        # os.system(r'"C:\Program Files\7-Zip\7z.exe" a -tzip -mx5 -r0 c:\_to\archive.zip c:\_from' + name + ' ' + name + ' ')
        # os.system('"C:\Program Files\7-Zip\7z.exe" a -tzip -mx5 -r0')

        zip_options = "a -tzip -mx5 -r0"
        zip_target_path = "c:/_to/" + currentdate
        # + ' ' - это добавлял т.к. без пробелов между опциями 7-зип выдавал ошибку
        os.system(r'"C:\Program Files\7-Zip\7z.exe"' + ' ' + zip_options + ' ' + zip_target_path + ' ' + pathtodata)

        # Рабочая строка. Ошибка на приписку name name, убрал - ошибка ушла
        # os.system(r'"C:\Program Files\7-Zip\7z.exe" a -tzip -mx5 -r0 c:\_to\archive.zip c:\_from')

        print("Name: ", name)
        print("Currentdate: ", currentdate)
        print("org: ", org)

# Готово!
print("Готово!")

#7z a -tzip -mx5 -r0 c:\_to\archive.zip c:\_from
# в данном примере мы создадим zip-архив с уровнем компрессии 5;
# в архив попадет все содержимое всех каталогов; название для файла
# c:\temp\archive.zip; запаковываем все содержимое папки c:\temp.
# 1. нужно всегда разделять логику и настройки, выделить настройки
# в какой-нибудь конфиг (txt, xml и т.д.) , тогда удобно будет менять параметры.

#-t	Тип архива. По умолчанию создаются файлы в формате 7z. Примеры, -tzip, -tgz
# https://www.dmosk.ru/miniinstruktions.php?mini=7zip-cmd - другие команды
