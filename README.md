## Парсер данных с FTP сервера Госзакупки
  
  Аннотация: _В работе анализируется единая информационная система в сфере закупок. Разработан парсер FTP сервера. Для анализа данных ЕИС авторами создан соответствующий программный комплекс. В данном программном решении выгрузка и обработка данных с FTP сервера осуществлялась с помощью языка программирования Python с последующей загрузкой данных в СУБД PostgreSQL. Выяснилось, что имеющееся в открытых источниках описание структуры FTP сервера не соответствует действительности._

  Для решения вышеперечисленных проблем было принято решение дополнить разработанный авторами программный комплекс следующим функционалом:
 - набором API для предоставления исследователям данных ЕИС в машиночитаемом виде;  
 - разработка прототипа информационной системы для пользователей и исследователей университета, обеспечивающей более релевантный поиск по закупкам.
 
  В структуре сервера выделяются различные группы файлов в зависимости от стадии закупочного процесса: извещения, протоколы, планы, завершенные закупки, отмененные закупки и т.д. Для упрощения анализа в данной работе рассмотрены только извещения о закупке. 
  
   В ходе анализа структуры выявлено, что формирование файловой системы менялось в зависимости от времени. Файлы в некоторые директории перестали загружаться после 01 июля 2018 года, когда вступили в силу поправки к ФЗ-223. Ряд директорий содержит файлы только за 2012-2013 годы, когда изначально начала формироваться ЕИС в сфере закупок.  Таким образом, группа файлов по извещениям о закупке представлена 11 различными форматами закупок такими, как «Открытый конкурс», «Открытый аукцион», «Закупка у единственного поставщика» и «Иные способы». 
   
   В ходе разработки были осуществлены следующие этапы: 
   
   - Загрузка архивов с FTP сервера
   - Распаковка xml файлов из архивов
   - Анализ предметной области. Определение необходимых данных
   - Проектирование базы данных 
   - Парсинг xml файлов
   - Загрузка распарсенных данных в базу данных 
   
   Результатом проекта является загрузка данных по региону - г. Москва (информация более чем о 2 миллионах закупках по 223-ФЗ) 
   
   Контакты для связи: AABudantsev@mephi.ru 
