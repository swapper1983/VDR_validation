# VDR_validation - это утилита проверки на соответствие оформления заголовков VDR документов и формирования выходной таблицы данных для пользователя
Vendor Document Register (Перечень Документов Поставщика) - эти документы, полученные от вендоров(поставщиков) требуют валидации
перед загрузкой их в БД СУИД. Для оптимизации проверки данных была разработанна эта утилита, которая путём валидации проверяет
все ли заданные заголовки присутствуют в документах, и далее если нет ошибок формирует Excel документы на выходе, без лишних данных и форматирования.
А уже эти Excel документы в последствии будут грузится администратором в БД СУИД.

## Обязательные требования к VDR документам
- команда инженерных данных предоставляет вендору/поставщику VDR шаблон для заполнения;
- документы VDR это исключительно Excel файлы, которые должны иметь расширения: xlsx или xls;
- структура шаблона VDR не должна изменяться вендором/поставщиком;
- для работы VDR_validation утилиты, каждый VDR документ должнен содержать минимум два листа (sheet) с названиями:
	- Cover sheet_VD;
	- Vendor Document Register.

## Как устроена утилита VDR_validation
- VDR_validation имеет несколько рабочих директорий:
	- /config, в этой папке в файле config.xlsx, пользователю необходимо задать конфигурацию проверяемых заголовков, пример конфигурации в config_example.xlsx;
	- /input, в эту папку пользователь должен загрузить VDR документ(ы) для обработки;
	- /output, это папка результатов с обработанными файлами;
	- /log, в данной папке храниться файл лога, с результатами работы утилиты;
- перед стартом утилиты, необходимо задать кофигурацию заголовков в /config/config.xlsx и разместить VDR документы в папке /intput;
- утилита логирует свою работу в файл в папке /logs, где можно посмотреть результаты по обработке файлов;
- результаты работы утилиты вы сможете найти в папке /output.

## Запуск проекта (скрипта)
1. Клонируйте репозиторий:
```
git clone git@github.com:swapper1983/VDR_validation.git
cd VDR_validation
```

2. Создайте виртуальное окружение:
```
python -m venv venv
```
3. Активируйте виртуальное окружение
* для Linux/Mac:
```
source venv/bin/activate
```

* для Windows:
```
source venv/Scripts/activate
```

4. Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

5. В директории с файлом main.py выполните команду: 
* для Linux:
```
main.py
```

* для Windows:
```
python main.py
```
Скрипт обработает файлы в папке /input, результаты будут размещены в папке /output.
Результаты скрипта соберутся в лог файл - папка /log.


# Дополнительные данные:
	Автор: Максим Филатов
	Контакт: swapper1983@yandex.ru
	Если у вас есть вопросы или пожелания по проекту, вы можете написать мне. 
[GitHub](https://github.com/swapper1983)