# Папка посвещена работе с ОКВЭД
_Note:_ Общероссийский классификатор видов экономической деятельности (сокращ. ОКВЭД)

> В течение 2014 года осуществляется переход на ОКВЭД 2 ОК 029—2014 (КДЕС Ред. 2), но продолжают действовать до 1 января 2017 г. ОКВЭД ОК 029—2001 (КДЕС Ред. 1) и ОКВЭД ОК 029—2007 (КДЕС Ред. 1.1). В настоящее время на территории РФ действуют три версии ОКВЭД: ОК 029—2001 (КДЕС Ред. 1), ОК 029—2007 (КДЕС Ред. 1.1) и ОК 029—2014 (КДЕС Ред. 2) в актуальных на 28.05.2014 года редакциях.
_Источник:_ Википедия, руссикй язык
_Resume:_ До 2014 года был ОКВЭД, с 2014 осуществляется переход на ОКВЭД 2, но другие классификаторы тоже действуют.

## CURRENT СТРУКТУРА ПАПКИ

Сейчас используется скрипт ```okved_full_table_prettifier.ipynb``` из ```..\..\notebook\```

```
├── classify             		<- Part of BOO (Bugalterskaya Otchetnost Organizatcii) module
│   └── __init__.py 
│   └── okved.py				<- some preprocessing scriptura
│   └── okved_full.txt			<- raw okved data, copied from an assistance system to work with the legislation of Russia
│   └── okved_full_table.json 	<- prepared json file of okved (not okved 2) data
│   └── README.md
```

## PLANNED СТРУКТУРА ПАПКИ

```
├── classify             		<- Part of BOO (Bugalterskaya Otchetnost Organizatcii) module
│   └── __init__.py 
│   └── okved.py
│   └── another classifiers
│   └── README.md
```