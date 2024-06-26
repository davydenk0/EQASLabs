**Пункт 1**
>В новій версії функції дані про особу передаються як один кортеж person_info, а оцінки передаються як список scores. Це робить код більш читабельним і полегшує його обслуговування.

**Пункт 2**
>У першій версії класу User, тип користувача представлений числовим значенням (type_engineer та type_manager). Це може бути не так очевидно при використанні класу, а також при зміні цих значень в майбутньому. Також, в методі print_details() телефонний код та номер телефону з'єднані напряму, що може ускладнити зміну формату в майбутньому.

>Другий варіант коду має кілька переваг порівняно з першим:
Краще розуміння коду: Використання стрічкових констант, таких як ENGINEER та MANAGER, робить код більш зрозумілим для інших розробників, які можуть працювати з ним пізніше.
Більш гнучка валідація типу: У другому варіанті тип користувача перевіряється за допомогою методу _validate_user_type, що дозволяє забезпечити більш гнучку та легшу виправлення помилок в майбутньому. У першому варіанті така валідація відсутня.
Менше шансів на помилку: Використання констант для типів користувачів зменшує шанси на помилки при введенні значень, порівняно з числовими константами у першому варіанті.
Краща підтримка коду: Якщо в майбутньому з'явиться потреба в зміні констант або додаткових типів користувачів, то другий варіант дозволить це зробити з меншими змінами в коді, порівняно з першим варіантом, де числові константи можуть викликати проблеми.
Отже, другий варіант коду є кращим, оскільки він забезпечує більшу зрозумілість, гнучкість і стабільність у роботі програми.

Таким чином, рефакторинг вдосконалив читабельність та гнучкість коду.