import telebot
import random
import datetime
from bs4 import BeautifulSoup
import requests

arr = ['\nКаждый твой выбор приведёт к гибели.\n', '\nМою хер, как пионер, чтоб поставить всем в пример.\n', '\nЛюдь! Жрать!\n', '\n — Ты иногда прямо... такая свинья, но я тебя... люблю, братик.\n— Геральт... Сука... Я сейчас расплачусь.\n', '\n — Ну и что, что судак чаще клюет, если на вкус он как говно в помоях?\n— Да это из тебя такой повар, как из козьего гузна кларнет. Вот я в прошлый раз взял свежего тимьянчику...\n— И на вкус было как тимьянчик с говном.\n', '\nС точки зрения пешки видны только товарищи по бокам и враги на той стороне поля. Король видит шахматную доску иначе. Злейшие враги окружают его. Собственные пешки могут запереть короля в западне. А тогда шах — и смерть. Шахматы, ведьмак, это искусство жертвовать собственными пешками.\n', '\nУ нас на дворе-подворье погода размакропогодилась.\n', '\nА в шахте ведь как на войне, то тут что-нибудь ***нет, то там ***анет.\n', '\nОднажды она сказала, что он ее жеребец. Лютик-то это за комплимент принял... но тут она вынула удила и сбрую и бедолага смылся через окно.\n', '\n — Есть минутка?\n— Минутки нет, есть только камни.\n', '\nА ты Золтан, как всегда, сапогом в гузно...\n', '\n — Называть Лугоса Безумным — оскорбление для безумцев. Он обычный долбошлеп.\n— Назови меня еще раз долбошлепом, и я отрежу тебе башку, насажу ее на кол и нассу в дырку от шеи.\n', '\nДождь? Вот такой у нас, сука, климат.\n', '\nБлагодать для тела и души. У тебя всегда будут еда и питье в изобилии... Твое тело будет ловким, как никогда. Мысли — быстрее молнии. Твоя страсть очарует любую женщину. Но прежде всего, я предлагаю тебе настоящее приключение. Ты испытаешь то, что дано пережить лишь избранным. Это не магический фокус-покус, это настоящее умение сделать нереальное реальностью.\n', "\n — Насчёт чудовищ мы не договаривались, это не честно.\n— Тебе понравилось? Ну, чем богаты, тем и рады.  Помни, тебе найти меня нужно, пока время не вышло. Скверно у тебя выходит. Помни. ты ещё можешь сдаться. Как мне кажется, ты меня не найдешь, никогда.\n— Чёрт бы тебя побрал О'Дим!\n— Ты же не думал. что разгадка будет настолько простой. Один — ноль в мою пользу.\n— Шум воды за стеной. Тише, тише. Если я разрушу стену, то она потечет сюда, в бассейн. Вот оно  Зеркало, Попался! Уходи, ты проиграл!\n", '\nВооот увидишь, я тебя выыыыы... Эх сука!\n', '\nСлушай свой инстинкты, даже если ты сделаешь дерьмо, то ты сделаешь это в согласии с собой.\n', '\n— Они хотят, чтобы мы х*рачились на сцене?\n— Нет, они хотят, чтобы вы х*рачились под сценой.\n', '\n — Ну, начнем.\n— Ой, да ты как лист трясешься! Погремушка — потаскушка!\n— Ну, давай уже драться что ли?\n— Главный на ринге шутник — это я, ты что не вякнешь, все выйдет херня!\n— Если шутки слабы, это видно всяко. В бою теперь сойдемся мы, однако?\n— Все твои фразы — пустая бравада. Станет победа мне лучшей наградой.\n— Скоро тебе будет доктора надо. Пусть поспешит и с тобой встанет рядом.\n— Доктор придет и, окинув все взглядом, кости твои заберет тебе на дом.\n— Лишний раз злить меня не надо. Кончится бой — и запросишь пощады.\n— Ну ты... Это... Того...\n', '\n — Я знал, что мы его завалим!\n— Ох, и ***ан ты, Виги!\n', '\n — Стража!\n— Бумага кончилась, ваше превосходительство?\n', '\nЧто-то бледный ты, как говно овсяное.\n', '\n — Загадка: много ест и много пьет. Ходит он большой и бьет.\n— Тролль, ясное дело.\n— Хорошо, тролль. Говори свою загадку.\n— Пусть легким бываю я, словно перо, быть долго и троллю со мной нелегко.\n— Э-э-э... пись-пись? Трудная загадка! Человек обманул!\n— Я выиграл честно.\n— Глупые загадки! Перо, троллю не легко... не пись-пись...\n', '\nЦелуй до старости жопу старосты.\n', '\nРемесло — оно ж как бабу трахать. Ритм слови и все то у тебя получится…\n', '\nХолодно тут, как у ледяного великана в жопе!\n', '\n — Это кто такой был? Почему сбежал?\n— Он суп на огне оставил.\n— Смотри, чтобы я тебя на огне не оставил, деловой.\n', '\nТишь на полях нильфгаардской страны. Эмгыр-император наделал в штаны.\n', '\nС нами лучше не балуй, лишь бы цел остался... ох, сука, я бы в рифму сказал, Геральт, да при даме не положено.\n', '\nГвинт — это как политика, только честнее.\n', '\nНе трогай форели, пока не отымели.\n', '\nДух тут тяжелый, вот у крестьян мозги и гниют!\n', '\nНе учи дедушку кашлять.\n', '\nВот ведь сходил в кабак!\n', '\nСплошные раритеты по доступным це... Ох, сука! Ты меня не видел!\n', '\nА девица из Виковара любит только за амбаром,\nУ второй из Виковаро не в чести ложиться даром,\nА у третьей нету правил, лишь бы кто-нибудь да вставил.\n', '\n — Мама папу лупит сковородкой за то, что он ходил на... бляшки.\n— На ***ки.\n', '\nВсе было так плохо? Надеюсь, это реакция не на меня?\n', '\nКто стоит без дела, считай зло творит...\n', '\nС опытом приходит мастерство.\n', '\nИзбыток власти убивает.\n', '\nДом — это вовсе не то место, где можно закрыться на ключ. Чтобы найти настоящий дом, иногда приходится пройти долгий путь.\n', '\nКакая прелесть — ты сохранил эту очаровательную способность удивляться миру! Хм, обычно она присуща только детям, бедным рыцарям и недоумкам.\n', '\n — Ты странный, брат! Все знают, что ведьмаки — выродки и ненормальные мутанты. А здесь порядочный бордель для шлюх с принципами. Говори начистоту: у тебя в штанах точно все, как у обычного мужика?\n— Когда последний раз проверял всё, вроде, было на своих местах.\n', '\n — Из всех созданий в этой округе самые занимательные — лошади. Ты интересуешься лошадьми?\n— Да я их не различаю. И всех зову Плотвами.\n', '\nХодят гули у дороги, съели руки, съели ноги. Скоро им жратвы не хватит. Так что ты смотри, приятель!\n', '\nТы что, хочешь превратить прекрасный акт альтруизма в дурацкий обмен услугами?\n', '\nНе всегда жизнь напоминает сказку, но надо же во что-то верить.\n', '\n — Знаешь, ты мне снилась.\n— Зная тебя, сон был неприличный.\n', '\nЛюбовь — не всегда поэзия. Порой она бывает удивительно прозаической. (Любовь — не всегда поэзия. Порой она бывает отвратительно прозаической.)\n', '\nНа вранье далеко не уедешь... Даже верхом.\n', '\n — Дикие собаки опаснее волков. Потому что волки охотятся, чтобы утолить голод... А дикие собаки убивают для забавы.\n— Совсем как люди.\n', '\n— А говорят, мутации лишают вас человечности и отнимают чувства.\n— Многие лишены человечности и без мутации.\n', '\n— Что, я, по-твоему, глупый?\n— Ты, по-моему, любопытный.\n— Моё любопытство кончается там, где начинается глупость.\n', '\nНужно во что-то верить. Иначе жить не хочется.\n', '\nЧеловеку иногда надо вкусить немного безумия, чтобы освежить вкус к жизни.\n', '\nЖить вечно не означает жить полной жизнью.\n', '\nСкажу тебе так: будь осторожен в своих желаниях, ведь они могут исполниться. А потом ты будешь бодаться с последствиями.\n', '\n — Я даю людям то, что они просят. Можно сказать, что я исполняю желания.\n— И втравливаешь людей в неприятности.\n— Это не я, а всего лишь их собственные желания во всей красе. Я честен. Я даю людям только то, что они хотят. Если они желают вещей недостойных, так лишь потому, что такова их гнилая натура.\n', '\nБолезнь можно вылечить, а вот если ты играешь со злом... Найти лекарство будет куда сложнее.\n']

bot = telebot.TeleBot('5260837416:AAF46-pKmq29vQF2xqOQWkzQ-6JSkldiJZA')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m, 'Киберпанк наступил')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    msg =  message.text.lower()
    date = datetime.datetime.now()
    names = ['Миха', 'Некит Сукманов', 'Некит Величко', 'Куцык', 'Светка', 'Тоха', 'Димас', 'Перк', 'Шиша']
    names_r = ['Михи', 'Некита Сукманова', 'Некита Величко', 'Куцыка', 'Светки', 'Тохи', 'Димаса', 'Перка', 'Шиши']

    alco = ['Пиво Hollandia светлое 4.8%, 450мл 39,9₽', 'Пиво Pilsner Urquell светлое фильтрованное 4.4%, 330мл 69,9₽', 'Напиток пивной Corona Extra 4.5%, 330мл 104,9₽', 'Пиво Жигули Барное светлое 4.9%, 450мл 59,9₽', 'Пиво Velkopopovicky Kozel резаное светлое 4.7% жестяная банка, 450мл 69,9₽', 'Пиво Spaten Мюнхен хелл светлое 5.2%, 500мл 114,9₽', 'Пиво Otto Von Schrodder Премиум лагер светлое фильтрованное 4.9%, 500мл 69,9₽', 'Пиво Pilsner Urquell светлое 4.4%, 500мл 129,9₽', 'Пиво Bud Лайт светлое 4.1%, 450мл 73,9₽', 'Пиво Жигули Барное светлое фильтрованное 4.9%, 450мл 65,9₽', 'Пиво Paulaner Мюнхенское хелль светлое 4.9%, 500мл 99,9₽', 'Пиво Krusovice Империал светлое 5%, 500мл 99,9₽', 'Пиво Heineken светлое 4.8%, 470мл 79,9₽', 'Пиво Paulaner Хефе-вайссбир светлое нефильтрованное 5.5%, 500мл 99,9₽', 'Пиво Hollandia светлое 4.8%, 450мл 39,9₽', 'Пиво Heineken светлое 4.8%, 430мл 91,9₽', 'Пиво Жигули Барное Пшеничное светлое нефильтрованное 4.9% жестяная банка, 450мл 59,8₽', 'Пиво Жигули Барное экспорт светлое фильтрованное 4.8%, 1.3л 149,0₽', 'Пиво Жигули ИПА светлое нефильтрованное 4.5%, 450мл 71,9₽', 'Пиво Жигули Барное экспортное светлое 4.8%, 450мл 65,9₽', 'Пиво Hoegaarden Белое нефильтрованное 4.9%, 450мл 64,9₽', 'Пиво Халзан светлое фильтрованное 4.5%, 450мл 55,6₽', 'Пиво Жигулевское светлое 4.6%, 1.5л 109,9₽', 'Пиво Velkopopovicky Kozel светлое 4%, 450мл 64,9₽', 'Пиво Балтика №7 Экспортное светлое 5.4%, 450мл 53,9₽', 'Пиво Oettinger Вайсс светлое нефильтрованное 4.9%, 450мл 77,9₽', 'Пиво Хамовники Чешское светлое 3.7%, 450мл 46,9₽', 'Пиво Carlsberg светлое 4.6%, 450мл 46,9₽', 'Пиво Старый мельник из бочонка Мягкое светлое 4.3%, 450мл 60,9₽', 'Пиво Балтика Мягкое №7 светлое 4.7%, 440мл 68,8₽', 'Пиво Krusovice Краловский Оригинал светлое 4.2%, 500мл 89,9₽', 'Пиво Bud светлое 5%, 450мл 64,9₽', 'Пиво Stella Artois светлое 5%, 450мл 69,9₽', 'Пиво Spaten Мюнхен хелл светлое 5.2%, 500мл 149,9₽', 'Пиво Wolpertinger Натуртрубес хефевайсбир светлое нефильтрованное 5.4%, 500мл 84,9₽', 'Пиво Heineken Премиум светлое 4.8%, 5л 1 199,9₽', 'Пиво Prazecka Чешское классическое 4%, 500мл 92,9₽', 'Пиво Wolpertinger Традиционное светлое 4.9%, 500мл 84,9₽', 'Пиво Kronenbourg 1664 Blanc Блан 4.5%, 450мл 114,9₽', 'Пиво Schlitz Премиум хеллес светлое 5%, 500мл 85,9₽', 'Пиво Eboshi светлое фильтрованное 4.9%, 500мл 129,9₽', 'Пиво Harp светлое 5%, 450мл 81,9₽', 'Пиво Staropramen светлое фильтрованное 4.2%, 430мл 97,9₽', 'Напиток пивной Amsterdam Навигатор 7%, 450мл 75,9₽', 'Пиво Lowenbrau Оригинальное светлое 5.4%, 450мл 79,9₽', 'Пиво Волковская Пивоварня Светлячок светлое нефильтрованное 5%, 450мл 87,9₽', 'Пиво Жигули Барное экспортное светлое 4.8%, 450мл 65,9₽', 'Пиво Хамовники Мюнхенское светлое фильтрованное 5.5%, 450мл 46,9₽', 'Пиво 387 Особая Варка светлое 6.8%, 450мл 51,9₽', 'Напиток пивной Redds светлый 4.5%, 330мл 63,9₽', 'Пиво Жигули Барное Пшеничное светлое нефильтрованное 4.9%, 450мл 59,8₽', 'Пиво Budweiser Budvar светлое 5%, 500мл 174,9₽', 'Пиво Krusovice Светле светлое 4.2%, 450мл 73,9₽', 'Пиво Grossmeister светлое фильтрованное 4.8%, 500мл 79,9₽', 'Напиток пивной Schofferhofer Грейпфрут 2.5%, 330мл 94,9₽', 'Пиво Faxe Премиум светлое 4.9%, 450мл 71,9₽', 'Пиво Velkopopovicky Kozel Премиум лагер светлое 4.6%, 500мл 89,9₽', 'Пиво Velkopopovicky Kozel резаное светлое 4.7%, 450мл 69,9₽', 'Пиво Волковская пивоварня ИПА светлое нефильтрованное 5.9%, 450мл 87,9₽', 'Пиво Grolsch Премиум лагер светлое фильтрованное 5%, 450мл 219,0₽', 'Пиво Хамовники Венское светлое 4.5%, 470мл 46,9₽', 'Пиво Bud Лайт светлое пастеризованное, 440мл 63,9₽', 'Пиво Lowenbrau Оригинальное светлое 5.4%, 1.3л 149,9₽', 'Пиво Афанасий Ремесленное светлое нефильтрованное 4.5%, 1л 249,0₽', 'Пиво Grolsch Премиум лагер светлое 4.9%, 450мл 87,9₽', 'Напиток пивной Somersby Блэкберри на основе пива 4.6%, 400мл 83,8₽', 'Пиво Балтика Мягкое №7 светлое 4.7%, 450мл 68,8₽', 'Пиво Aldaris Гайсайс светлое 5%, 568мл 114,9₽', 'Пиво Bayreuther Hell светлое 4.9%, 500мл 209,0₽', 'Пиво Velkopopovicky Kozel светлое 4%, 4x450мл 214,9₽', 'Пиво Хамовники Венское светлое 4.5%, 450мл 46,9₽', 'Пиво Allgauer Око бир био светлое 5.2%, 500мл 349,0₽', 'Пиво Панк ипа светлое фильтрованное 5.4%, 500мл 299,0₽', 'Напиток пивной Hoegaarden Розе нефильтрованный 3%, 250мл 119,9₽', 'Напиток пивной Essa Лимон-мята 6.5%, 450мл 71,9₽', 'Пиво Faxe Премиум светлое 4.9%, 900мл 119,9₽', 'Пиво Krombacher Вайцен светлое пшеничное нефильтрованное 5.3%, 500мл 154,9₽', 'Пиво Bear Beer Стронг лагер светлое 8.3%, 450мл 63,9₽', 'Пиво Липецкпиво Немецкий рецепт светлое нефильтрованное 4.7%, 920мл 89,9₽', 'Пиво Peterhof Живое светлое нефильтрованное 4.6%, 1л 104,9₽', 'Пиво Holsten Премиум светлое 4.8%, 450мл 89,9₽', 'Пиво Franziskaner Хефе-вайссе 5%, 500мл 139,9₽', 'Пиво Хамовники Пильзенское светлое 4.8%, 450мл 46,9₽', 'Пиво Peroni Настро адзурро светлое 5.1%, 330мл 139,9₽', 'Пивной напиток Hoegaarden Белое нефильтрованное 4.9%, 440мл 64,9₽', 'Напиток пивной Schofferhofer Грейпфрут нефильтрованный 2.5%, 500мл 209,0₽', 'Пиво Grolsch Премиум пилснер 5%, 500мл 129,9₽', 'Пивной напиток Хугарден грейпфрут нефильтрованный 4.6%, 440мл 64,9₽', 'Пиво Leffe Блонде светлое 6.6%, 500мл 159,9₽', 'Пиво Хамовники Пильзенское светлое 4.8%, 470мл 46,9₽', 'Пиво Budweiser Budvar светлое 5%, 500мл 129,9₽', 'Пиво Stella Artois светлое 5%, 440мл 69,9₽', 'Пиво Hacker Pschorr Мюнхнер золотое светлое 5.5%, 500мл 159,9₽', 'Напиток пивной Essa ананас-грейпфрут 6.5%, 450мл 71,9₽', 'Пиво Warsteiner Премиум светлое фильтрованное 4.8%, 500мл 154,9₽', 'Пиво Золотая Бочка Классическое светлое 5.2%, 450мл 55,9₽', 'Пиво Золотая Бочка светлое 4.7%, 450мл 55,9₽', 'Пиво Хамовники Пшеничное светлое нефильтрованное 4.8%, 450мл 46,9₽', 'Пиво Балтика №7 Экспортное 5.4%, 470мл 65,9₽', 'Пиво Kronenbourg 1664 Блан 4.5%, 460мл 114,9₽', 'Напиток пивной Волковская Пивоварня Мишенька под вишенкой нефильтрованный 4.8%, 450мл 95,9₽', 'Пиво Wolters Пилсенер светлое 4.9%, 500мл 119,9₽', 'Пиво Boddingtons Паб эль светлое 4.6%, 500мл 119,9₽', 'Пиво Волковская Пивоварня Бланш де мазай светлое нефильтрованное 5.9%, 450мл 87,9₽', 'Пиво Efes Пилсенер светлое 5%, 450мл 54,9₽', 'Пиво Bud светлое 5%, 4x450мл 249,0₽', 'Пиво Franziskaner Пшеничное светлое, 5л 1 199,0₽', 'Пиво Carlsberg светлое 4.6%, 450мл 46,9₽', 'Пиво Оболонь светлое фильтрованное 4.5%, 900мл 109,9₽', 'Напиток пивной Чехов Вишневый эль нефильтрованный 6.3%, 750мл 239,0₽', 'Пиво Grolsch Премиум лагер светлое 4.9%, 500мл 87,9₽', 'Пиво Фон вакано, 500мл 75,9₽', 'Напиток пивной Miller Дженюин Драфт 4.7%, 470мл 81,9₽', 'Пиво Zlata Praha светлое фильтрованное 4.7%, 500мл 89,9₽', 'Напиток пивной Inedit Damm нефильтрованный 4.8%, 500мл 134,9₽', 'Пиво Paulaner Мюнхенское хелль светлое 4.9%, 500мл 144,9₽', 'Напиток пивной Somersby Уотермелон 4.6%, 400мл 83,8₽', 'Пиво Stanley Cooper светлое 4.9%, 500мл 114,9₽', "Напиток пивной Seth and Riley's Garage Хард черная вишня 4.6%, 440мл 75,9₽", 'Пиво Tuborg Green Грин светлое 4.6%, 450мл 75,9₽', 'Пиво Wychwood Хобгоблин голд светлое фильтрованное 4.2%, 500мл 199,9₽', 'Пиво Белый Медведь светлое 5%, 1.3л 109,9₽']
    alco.extend(['Коньяк Киновский 3-летний российский 40%, 500мл 499,9₽', 'Коньяк Ной Араспел 3-летний армянский 40% в подарочной упаковке, 500мл 999,0₽', 'Коньяк Сокровище Тифлиса 3-летний грузинский, 500мл 559,9₽', 'Коньяк Три звёздочки трехлетний 40%, 250мл 249,0₽', 'Коньяк Старейшина Трэвел 3-летний 40%, 500мл 589,0₽', 'Коньяк Ной Традиционный 3-летний 40%, 500мл 649,9₽', 'Коньяк Киновский 3-летний российский 40%, 350мл 429,0₽', 'Коньяк Ной Араспел 3-летний армянский 40% в подарочной упаковке, 700мл 1 299,0₽', 'Коньяк Арарат 3 звезды армянский 40%, 700мл 1 159,0₽', 'Коньяк Арарат 3 звезды армянский 40%, 500мл 829,0₽', 'Коньяк Три звёздочки трехлетний 40%, 500мл 489,0₽', 'Коньяк Старейшина 3-летний российский 40%, 1л 1 299,0₽', 'Коньяк Российский Три звёздочки 3-летний 40%, 250мл 249,0₽', 'Коньяк Киновский 3-летний российский 40%, 250мл 369,0₽', 'Коньяк Три звёздочки 3-летний 40%, 500мл 619,0₽', 'Коньяк Армянский 3-летний 40%, 250мл 289,0₽', 'Коньяк Армянский 3-летний 40%, 500мл 480,0₽', 'Коньяк Российский Три звёздочки 40%, 500мл 480,0₽', 'Коньяк Киновский 3-летний 40%, 100мл 144,9₽', 'Коньяк Армянский Старый купаж 1903 3-летний 40%, 250мл 240,0₽', 'Коньяк Армянский 3 звезды 40%, 500мл 599,0₽', 'Коньяк Прасковейский 3-летний 40%, 500мл 599,0₽', 'Коньяк Роро Российский 3-летнийфляжка, 250мл 229,0₽', 'Коньяк Талант Сомелье 3-летний 40%, 500мл 499,0₽', 'Коньяк Три звезды 3-летний 40%, 500мл 499,0₽', 'Коньяк Ваше Высочество 3-летний российский 40%, 500мл 499,0₽', 'Коньяк Российский Три звёздочки 3-летний 40%, 500мл 499,0₽', 'Коньяк Суворов Российский 3-летний 40%, 500мл 659,0₽', 'Коньяк Белый Агат Российский 3-летний, 500мл 1 199,0₽', 'Коньяк Страна Камней №3 3-летний 40%, 100мл 209,0₽', 'Коньяк Черноморский Российский 3 звезды 3-летний, 500мл 639,0₽', 'Коньяк Терра Армена 3 звезды 40%, 500мл 739,0₽', 'Коньяк Картвели Грузинский 3 звезды 3-летний 40%, 500мл 959,0₽', 'Коньяк Вечерний Тбилиси Грузинский 3-летний 40%, 500мл 1 249,0₽', 'Коньяк Асканели Грузинский 3-летний 40%, 500мл 1 049,0₽', 'Коньяк Саят Нова 3 звезды 3-летний 40% в подарочной упаковке, 500мл 959,0₽', 'Коньяк Кивер Шако 3 звезды российский 40%, 500мл 499,0₽', 'Коньяк Саят Нова Три звезды армянский 40%, 500мл 759,0₽', 'Коньяк Российский 3 звезды 40%, 500мл 480,0₽', 'Коньяк Три звёздочки 3-летний российский 40%, 500мл 459,0₽', 'Коньяк 3 Звёздочки 3-летний российский 40%, 500мл 579,0₽', 'Коньяк Арарат 3 звезды армянский 3-летний 40%, 250мл 479,0₽', 'Коньяк Samarkand 3 звезды узбекский 40%, 250мл 309,0₽', 'Коньяк Прасковейский 3-летний 40%, 250мл 339,0₽', 'Коньяк Прасковейский 3-летний 40%, 100мл 179,9₽', 'Коньяк Армянский 3-летний 40%, 500мл 480,0₽', 'Коньяк КВС 3 звёздочки 3-летний российский 40%, 250мл 299,0₽', 'Коньяк Кизлярский 3 звезды российский 40%, 500мл 480,0₽', 'Коньяк Marsharan Маршаран 3-летний российский 40%, 500мл 559,0₽', 'Коньяк Три звёздочки 3-летний российский 40%, 250мл 240,0₽', 'Коньяк Три звёздочки 3-летний 40%, 500мл 659,0₽', 'Коньяк Прасковейский 3 звезды 40%, 500мл 639,0₽', 'Коньяк Гран-При 3-летний 40%, 500мл 579,0₽', 'Коньяк Жемчужина Ставрополья 3 звезды российский 40%, 500мл 499,0₽', 'Коньяк Армэл 3-летний армянский 40%, 500мл 480,0₽', 'Коньяк Shustoff 3-летний 40%, 500мл 579,0₽', 'Коньяк ОДЕССКИЙ 3* 40%, 500мл 480,0₽', 'Коньяк Страна Камней №3 3-летний армянский 40%, 350мл 499,0₽', 'Коньяк Дживан армянский 40%, 500мл 839,0₽', 'Коньяк Избербаш 3-летний российский-дагестанский 40%, 500мл 519,0₽', 'Коньяк Остров Крым 3-летний российский 40%, 500мл 499,0₽', 'Коньяк Кремлевский 3-летний российский 40%, 500мл 519,0₽', 'Коньяк Армянский 3-летний 40%, 250мл 240,0₽', 'Коньяк 3-летний армянский 40%, 250мл 240,0₽', 'Коньяк Гугули 3-летний грузинский 40%, 500мл 480,0₽', 'Коньяк Три звёздочки 3-летний российский 40%, 500мл 489,0₽', 'Коньяк Три звёздочки российский 40%, 100мл 114,9₽', 'Коньяк Samarkand 3 звезды узбекский 40%, 500мл 599,0₽', 'Коньяк Beretta 3 звезды 40%, 250мл 249,0₽', 'Коньяк Аранаит 3-летний 40%, 500мл 939,0₽', 'Коньяк Древний Дагестан 3-летний российский 40%, 500мл 699,0₽', 'Коньяк Людовик 3-летний 40%, 500мл 559,0₽', 'Коньяк Избербаш Три звёздочки 40%, 500мл 589,0₽', 'Коньяк Аргус 3-летний грузинский 40%, 500мл 879,0₽', 'Коньяк Армянское Золото 3-летний 40%, 500мл 719,0₽', 'Коньяк 3-летний армянский 40%, 500мл 639,0₽', 'Коньяк Три звёздочки 3-летний российский 40%, 250мл 249,0₽', 'Коньяк Старый купаж Дагестанский 3-летний 40%, 250мл 329,0₽', 'Коньяк Старый купаж Дагестанский 3-летний 40%, 500мл 599,0₽', 'Коньяк Старейшина Трэвел 3-летний 40%, 100мл 124,0₽', 'Коньяк Вершина Армении 3-летний армянский 40%, 500мл 529,0₽', 'Коньяк Три звёздочки 3-летний российский 40%, 100мл 119,9₽', 'Коньяк Тавинко 3-летний армянский 40%, 250мл 349,0₽', 'Коньяк Shato Arno Купаж №3 3-летний 40%, 500мл 639,0₽', 'Коньяк Шахназарян 3-летний армянский 40%, 500мл 699,0₽', 'Коньяк Бахчисарай 3-летний 40%, 500мл 839,0₽', 'Коньяк КВС Три звёздочки 3-летний российский 40%, 500мл 480,0₽', 'Коньяк Армянский Коньяк 3-летний 40%, 500мл 639,0₽', 'Коньяк Старый Купаж 1903 3 звезды армянский 40%, 500мл 480,0₽', 'Коньяк Три звёздочки 3-летний российский 40%, 500мл 480,0₽', 'Коньяк Вершина Армении 3-летний 40%, 500мл 619,0₽', 'Коньяк Дагвино Российский 3 звезды 40%, 500мл 519,0₽', 'Коньяк Усовский 3 звезды российский 40%, 500мл 480,0₽', 'Коньяк Sarajishvili 3-летний 40%, 500мл 849,0₽', 'Коньяк Stone Land №3 3-летний армянский 40%, 500мл 739,0₽', 'Коньяк Сокровище Тифлиса 3-летний грузинский 40%, 500мл 859,0₽', 'Коньяк Старейшина 3-летний российский 40%, 500мл 699,0₽', 'Коньяк Старый Кёнигсберг 4-летний 40%, 250мл 379,0₽', 'Коньяк Старый Крым Чёрный дуб 4-летний российский 40%, 500мл 569,9₽', 'Коньяк Старый Кёнигсберг 4-летний российский 40%, 500мл 739,0₽', 'Коньяк Старый Кёнигсберг 4-летний 40%, 700мл 1 049,0₽', 'Коньяк Старый Кёнигсберг 4-летний российский 40%, 375мл 559,0₽', 'Коньяк Старый Кёнигсберг 4-летний 40%, 100мл 149,9₽', 'Коньяк Courvoisier Наполеон 40% в подарочной упаковке, 700мл 6 399,0₽', 'Коньяк Кавказ 4-летний 40%, 500мл 480,0₽', 'Коньяк Старый Кенигсберг 4-летний 40% в фляжке, 500мл 779,0₽', 'Коньяк Московский 4 звезды российский 40%, 500мл 619,0₽', 'Коньяк Гордый Севастополь 4 звезды 40%, 500мл 899,0₽', 'Коньяк Командирский 4 звезды российский 40%, 500мл 519,0₽', 'Коньяк Коблево 4 звезды 40%, 500мл 519,0₽', 'Коньяк Коктебель 4-летний российский 40%, 500мл 589,0₽', 'Коньяк Трофейный 4-летний российский 40%, 250мл 349,0₽', 'Коньяк Shustoff 4-летний российский 40%, 500мл 699,0₽', 'Коньяк Старый Кёнигсберг 4-летний 40%, 1л 1 299,0₽', 'Коньяк Русский Манеръ 4-летний российский 40%, 250мл 279,0₽', 'Коньяк Старый Кёнигсберг 4-летний российский 40% в подарочной упаковке, 500мл 799,0₽', 'Коньяк Старый Тильзит 4-летний российский 40%, 500мл 679,0₽', 'Коньяк Золотая Выдержка 4-летний российский 40%, 1л 1 149,0₽', 'Коньяк Апшерон 4-летний российский 40%, 500мл 539,0₽', 'Коньяк Трофейный 4-летний российский 40%, 500мл 659,0₽', 'Коньяк Московский 4-летний 40%, 500мл 549,0₽', 'Коньяк Александр Бержерак 4-летний российский 40%, 500мл 679,0₽', 'Коньяк Старый Кёнигсберг 4-летний 40%, 100мл 159,9₽'])
    if msg == 'красавчик':
        bot.send_message(message.chat.id, 'Подобен своему создателю')
    elif msg == 'ебани фразу':
        bot.send_message(message.chat.id, random.choice(arr))
    elif msg == 'шишка':
        bot.send_message(message.chat.id, 'Здарова ёптить')
    elif msg == 'где сегодня бухич?':
        if date.day == 6 and date.month == 3:
            bot.send_message(message.chat.id, 'У Ивакова')
        if date.day == 7 and date.month == 3:
            bot.send_message(message.chat.id, 'У Никитосика') 
    elif msg == 'где завтра бухич?':
        if date.day == 6 and date.month == 3:
            bot.send_message(message.chat.id, 'У Никитосика')    
        else:
            bot.send_message(message.chat.id, 'Бухаловы закончились') 
    elif msg == 'кто будет блевать?':
        ind = random.randint(1, 3)
        
        first = random.choice(names)
        names.remove(first)
        second = random.choice(names)
        
        first_r = random.choice(names_r)
        names_r.remove(first_r)
        second_r = random.choice(names_r)
        
        phrases = {
            1: f'{first} немного пообнимается с унитазом, ну а {second} будет стрелять как из миномета',
            2: f'Все будут в адеквате кроме {first_r}, которого вполне могут выкинуть из хаты',
            3: f'Обдристаются все кроме {first_r} и {second_r}, которые будут на страже закона адекватности',
        }
        
        bot.send_message(message.chat.id, phrases[ind]) 
    elif msg == 'посоветуй бухло':
        bot.send_message(message.chat.id, random.choice(alco))
    elif msg == 'рифма к' or msg == 'рифма к ': 
        bot.send_message(message.chat.id, 'К чему? Дурачок')
    elif msg.startswith('рифма к'): 
        msg = msg.replace('рифма к', '', 1)
        req = requests.get(f'https://double-rhyme.com/?hl=ru&s={msg}')
        
        soup = BeautifulSoup(req.text, 'lxml')

        divs = soup.find_all('div', class_='td')
        riphme = [i.text for i in divs if i.text.rstrip()]
        text = random.choice(riphme) if riphme else 'Такое рифмовать не умею'
        
        bot.send_message(message.chat.id, text)
    elif 'курс сюда' in msg: 
        req = requests.get(f'https://ru.investing.com/currencies/usd-rub')
        soup = BeautifulSoup(req.text, 'lxml')
        
        rus = soup.find('span', class_='text-2xl').text
        
        req = requests.get(f'https://ru.investing.com/currencies/usd-rub?cid=962711')
        soup = BeautifulSoup(req.text, 'lxml')
        
        forex = soup.find('span', class_='text-2xl').text
        
        bot.send_message(message.chat.id, f'Москва: {rus}₽\nФорекс: {forex}₽')

bot.polling(none_stop=True, interval=0)
