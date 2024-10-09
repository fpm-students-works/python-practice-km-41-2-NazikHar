Якщо ви бачите цей текст — то ви вдало створили свій репозиторій для практичних занять з дисципліни Програмування-1.

## Що далі?
Перш за все, клонуйте цей репозиторій на свій робочий комп'ютер:
```shell
git clone <посилання на ваш репозиторій>
```

(Тут і далі `<такий текст>` потрібно заміняти на власні значення.)

Посилання ви можете отримати з адресного рядку вашого браузера чи натиснувши зелену кнопку Code вище.

Також вам потрібно налаштувати ваш локальний репозиторій аби отримувати оновлення з репозиторію викладача:
```shell
git remote add upstream <посилання на репозиторій викладача>
git fetch upstream
```

Оскільки ваш репозиторій є форком (fork) репозиторію викладача — ви можете бачити посилання на нього під іменем вашого репозиторію відразу після фрази `forked from`. Як посилання у команду вище вам потрібно вказати саме посилання на нього. Ви можете отримати його від викладача чи перейшовши за посиланням під назвою вашого репозиторію.

Детальніше про налаштування форків можна прочитати [тут](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork) (англ). 

## Як отримувати нові завдання?
Щотижня ви будете отримувати нові завдання виконуючи синхронізацію із віддаленим репозиторієм викладача. Це можна зробити двома способами:

### 1. Через вебінтерфейс
1. Натиснути кнопку 🔄 Sync fork вище. Це синхронізує ваш віддалений репозиторій із репозиторієм викладача.
2. Синхронізувати ваш локальний репозиторій, виконавши команди:
```shell
git checkout main
git pull origin
```

### 2. Через термінал
Виконайте наступні команди:
```shell
git checkout main
git merge upstream/main
git push origin
```

Якщо ви бачите помилки, то переконайтеся, що ви налаштували ваш локальний репозиторій як описано вище.

Детальніше про синхронізації форків можна прочитати [тут](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) (англ).

## Як виконувати завдання?
Перед виконанням кожного завдання вам необхідно виконати наступне:

1. Перейдіть на гілку `main` та синхронізуйтеся із репозиторієм викладача. Це має завантажити нове завдання.
```shell
git checkout main
```

2. Створіть нову гілку:
```shell
git checkout -b <branch_name>
```

3. Виконайте роботу.

4. Відправте роботу у віддалений репозиторій:
```shell
git push --set-upstream origin <branch_name>
```

5. Створіть пулл-реквест (pull-request) у свій репозиторій у вебінтерфейсі Гітхабу.
