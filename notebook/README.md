# Анализ отчетности

Этот файл описывает использование отчетности, которую можно 
получить через `boo.read_dataframe(year)`

Наш набор данных:
- [ ] воспроизводит известные списки крупнейших российских компаний
- [ ] группирует компании по фактическим отраслям 
- [ ] используется для обучения финансовому анализу на основе реальных данных
- [ ] находится в открытом доступе, может скачиваться разными способами

## Задачи в работе:

- [x] данные состыкованы с отраслевым классификатором
- [x] показывается объем активов и продажи по компаниям
- [x] выгрузка крупнейших компаний по отраслям
- [ ] взять 1-2 интересную подотрасль для анализа
- [ ] перевести компании в "свои отрасли" (особенно `46 торговля`)
- [ ] дать примеры, что могут считать студенты на этом датасете
- [ ] формат свобного материала (html? )
- [ ] рекламный материал для датасета (напрмер, страница gh-pages 
      или интерактивная старница ipython / plotly)


## Трудоемкие задачи (отложены)

- coverage (соотвествие базы отчетности окаймляющим из других источников)
- стыковка с другими наборами данных
- анализ малых и средних предприятий

## Известные [ ] / решенные [x] проблемы

- [x] задвоение строк
- [ ] неравенство частей отчтености
- [ ] холдинги
- [ ] "призраки" (крупные неизвестные компании)
- [ ] нулевой объем продаж
- [ ] "не свои" отрасли

## Правила:

- [x] начинаем с канонического набора данных `pick.make_df()`


## Файлы

- [TODO.md](TODO.md) - "длинный" список задач
- [NOTES.md](NOTES.md) - пояснения и справочная информация
- [pick.py](pick.py) - "канонический" набор данных и функции к нему
- [up.bat](up.bat) - запуск Jupiter Lab на Windows из текущего каталога

Дополнительно:
- [company.py](company.py) - текстовый интерфейс для представления баланса компании,
                 в том числе показывает случайную компанию
- [play.ipynb](play.ipynb) - основные свойства набора данных (вводный просмотр)
- [play.py](play.py) - взять функции отрисовки, разобрать и удалить   
