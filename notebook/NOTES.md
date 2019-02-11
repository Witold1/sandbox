# Обобщения по использованию данных

## Идеальная модель данных 

"Мы знаем все", если:

1. весь бизнес корпоратизирован, нет "серой" экономики
2. в базе есть отчетность по всем компаниям
3. отчетность "правильная" 
4. нет холдингов
5. компании моноотраслевые
6. компании отнесены к своим отраслям 
7. компании зарегистрированы в регионах, где они работают  
8. можем добавлять другие данные к отчетности

Эти критерии группируются вокруг:

- полноты
- "единичности"
- достоверности


## Кто пользователей отчетности?

- инвесторы в капитал (стоимость компании)
- кредиторы (вероятность дефолта, стоимость долга)
- антимонопольные органы (концентрация в отрасли)
- налоговые органы (налоговая нагрузка, уход от налогов)
- social planners (структура экономики, занятость, возможности роста)
- региональное планирование (городской транспорт, ЖКХ, TБО)
- менеджмент (эффективность бизнеса) 
- управление инвестициями (инвесторы, компании, государство) 

## Типы компаний

- Типы компаний (производственная, холдинговая, финансовая, торговая компания)
- Ситуации (рост, инвестиции, банкротство)
- Малые предприятия

## Рейтинги компаний

- [Эксперт](https://expert.ru/dossier/rating/expert-400)
- [Коммерсант](https://www.kommersant.ru/top-100)
- [РБК](https://www.rbc.ru/rbc500/)
- [Forbes](http://www.forbes.ru/rating/367067-200-krupneyshih-rossiyskih-chastnyh-kompaniy-2018-reyting-forbes)

## Смежные данные 

- [ ] котировальный список ММВБ
- [ ] данные по бондам
- [x] справочник ОКВЭД
- [ ] отрасли: официальная статистика
- [ ] отрасли: маркетинг, рейтинги коипаний
- [ ] данные региональной статистики
- [ ] аналогичные системы раскрытия информации за рубежом (EDGAR)

## Нет в отчетности

В приницпе нет в бухгалтерской отчетности:

  - занятость (но есть ФОТ)
  - все натуральные показатели
  - перекрестное владение, доли собственности

Могло бы быть, но нет:

  - амортизация
  - прочие налоги кроме прибыли
  - валютная структура (но может быть переоценка)

# Источники данных 

### Официальные источники

- [Классификаторы Росстата](http://www.gks.ru/metod/classifiers.html)
- [ОКВЭД-2](http://www.gks.ru/opendata/dataset/7708234640-ca-01-004)
- [Сервис Росстата по получению отчетности по ИНН](http://www.gks.ru/accounting_report)
- [Выписки из ЕГРЮЛ](https://egrul.nalog.ru/index.html)

### Он-лайн доступ  

- [sbis](https://sbis.ru/contragents/7825706086)
- [list-org](https://www.list-org.com/company/19562)

### Крупные провайдеры 

- [Спарк (Интерфакс)](http://www.spark-interfax.ru/ru/about)
- [БИР-Аналитик (Прайм)](https://bir.1prime.ru)
- [Скрин](https://kontragent.skrin.ru)
- [Фира-Про](https://pro.fira.ru)


## Выдача - форматы публикаций

*Простейшие варианты*

- [ ] markdown  
- [x] jupiter notebook

*Чуть более сложные варианты*
- [ ] pdf/latex
- [ ] pdf/reportlab
- [ ] react.js презенатция
- [ ] небольшой статичный сайт (jekyll)
- [ ] R bookdown
- [ ] asciidoc  
  
## Прочие ссылки

- [Как писать электронные книги](https://www.allendowney.com/blog/2018/12/27/how-to-write-a-book/)
- <https://gist.github.com/mrtns/da998d5fde666d6da26807e1f246246e>