init:
    $ mods["rfe_prologue"] = u"Готов ко всему."
    image bg uni = "uni.jpg"
    $ pav = Character(u'Павел', color="#380")
    $ mav = Character(u'Мать', color="480")
    image bg gym = "mods/bg/gym.jpg"
    image bg gym2 = "mods/bg/gym2.jpg"
    image bg gym3 = "mods/bg/gym3.jpg"
label rfe_prologue:
    play ambience ambience_medium_crowd_indoors_1 fadein 0
    window hide
    scene black
    window show
    play music music_list["into_the_unknown"] fadein 3 #ДОБАВИТЬ ЗВУКИ ударов
    "Остро наточенный топор, ловя лезвием солнечные блики, взмывает вверх. {w}Удар. {w}Еще удар. {w}Желтая щепа от здоровенного бревна, вкопанного вертикально в землю, брызгами разлетается в стороны."
    "Прямой удар.{w} Боковой. {w}Удар обухом снизу. {w}Смещение в сторону, уход от предполагаемой атаки и сразу же быстрая ответная серия." #ДОБАВИТЬ ЗВОН БУДИЛЬНИКА
    scene bg gym with dissolve
    "Звон будильника, стоящего на старой тумбочке возле истоптанной поляны с несчастным бревном, дребезжащей трелью напоминает о конце тренировки. "
    "Худощавый парень, на вид лет семнадцати, одетый в одни шорты, опускает свое орудие и делает несколько глубоких вдохов. {w}Потом резким движением метает топор в стоящее неподалеку дерево, с нарисованной на нем белой масляной краской мишенью."
    "Совершив несколько оборотов, тот втыкается в середину цели, занимая свое место среди уже воткнутых самодельных метательных ножей, грубо выточенных сюрикенов, одной саперной лопатки и даже пары вилок."
    "Взяв лежащую на шезлонге рубашку с красным галстуком парень медленно побрел прочь."
    "Выйдя на небольшую площадку с расположенными на ней общими умывальниками, он поднимает стоящее рядом цинковое ведро и, наполнив его до краев водой, опрокидывает его на себя."
    "Ледяная вода смывает пот, сводя судорогой разгоряченные мышцы."
    "Если бы поблизости оказался какой-нибудь нечаянный наблюдатель, от увиденной картины он бы ужаснулся – тело парня, словно свитое из мышц и сухожилий, покрывали многочисленные шрамы и рубцы, да так густо, что казались какой-то чудовищной татуировкой."
    "Что удивительно, но лицо его оставалось без каких-либо отметок."
    "Ополоснувшись, он надел рубашку на мокрое тело, небрежно завязал галстук и так же медленно побрел дальше. {w}Вытоптанная в земле дорожка привела его к небольшому зданию с табличкой библиотека. {w}Войдя внутрь, он плюхнулся за стол и осмотрел лежащие стопкой книги."
    "\"Боевая армейская система\", \"Психологический контроль человека\", \"Гипноз\", \"Взрывчатые вещества\", \"Управление наземным транспортом\", \"Акупунктура\", \"Стрелковое оружие\", \"Выживание\", \"Расширенный английский\". {w}Вытащив из стопки \"Управление наземным транспортом\" он углубился в чтение."
    scene bg gym2 with dissolve
    "Раздавшийся за спиной треск заставил его оторваться от чтения. {w}В углу комнаты появилась черная щель, висящая в воздухе. Она медленно расходилась вширь образуя своеобразный проход, достаточный, что бы туда мог пролезть взрослый человек."
    "Парень отложил книгу, рывком поднялся со стула и двинулся к аномалии.{w} Проходя мимо стоящего около стены стенда, он мельком бросил на него взгляд. {w}Дойдя до потрескивающего прохода, он остановился и, оскалившись, рявкнул в черноту:"
    me "- Ну давай! Давай, гнида!"
    scene bg gym3 with dissolve
    "Проход засветился темно-фиолетовым светом и парень без всякой опаски шагнул внутрь. {w}Щель сомкнулась, оставив комнату пустой. Порыв сильного ветра, возникший при схлопывании заставил всколыхнутся пять приколотых к стенду листов."
    "На каждом из них было написано имя – \"Славя\", \"Ульяна\", \"Алиса\", \"Лена\", \"Мику\". {w}И множество крестов под именами, начерканных красной ручкой, чей цвет чернил так сильно походил на запекшуюся кровь…"
    jump rfe_part1
label rfe_part1:
    stop music
    play music music_list["orchid"] fadein 3
    scene black #заменить на качели
    "Старые несмазанные качели тихонько поскрипывали. Сидящая на них Лена тяжело вздохнула. Уже давно стемнело, но идти домой совсем не хотелось. {w}Опять пьяный отчим, запуганная и замученная мать."
    "Но идти надо. Сейчас пора подготовки к экзаменам, осталось совсем немного.{w} Надо выучить хотя бы еще пару билетов."
    "Поднявшись с качелей, она подобрала лежащий рядом портфель и направилась к подъезду своей ненавистной пятиэтажки.{w} Поднявшись на третий этаж, она достала ключ и тихонько вставила его в замочную скважину."
    "Старый замок с разболтанной вставкой посопротивлялся, но, наконец щелкнув, открылся. Зайдя внутрь, девушка аккуратно сняла туфли и пошла по коридору в свою комнату."
    "Как назло, путь проходил мимо кухни, где, несмотря на поздний час, горел свет.{w} Неразборчиво бубнело радио. "
    "Лена попыталась тихо прошмыгнуть мимо, но грозный окрик \"Стой!\" пьяного отчима заставил ее замереть в проеме."
    "Он сидел за столом — грузный сорокалетний с хвостиком безработный мужик, в заляпанной майке и спортивных линялых штанах. {w}Рядом стояла почти пустая бутылка водки, граненый стакан и остатки дешёвой нарезанной колбасы. "
    "Мать, стоящая у раковины в домашнем халате и моющая посуду, испуганно вжала голову в плечи."
    pav "- Иди-ка сюда.{w}"
    "Косые припухшие глаза отчима злобно блеснули. {w}Лена молча зашла на кухню и остановилась."
    pav "Ты где шлялась? А?"
    mav "Пашенька, не надо… - тихонько начала мать."
    pav "Заткнись, Люда!" 
    "Резко оборвал ее муж. И продолжил."
    pav "Ну, чего молчишь?"
    un "Я была в библиотеке, готовилась."
    "Еле слышно ответила Лена. Как всегда в таких случаях ей становилось тяжело в груди, не хватало воздуха. Хотелось спрятаться под одеяло, как в детстве."
    "Отчим злобно зашипел:"
    pav "Все твои грёбаные библиотеки работают до 7 часов. {w}Где ты была остальное время? А? {w}Хахаля завела, небось? Ну-ка, на колени, быстро!"
    "Девушка послушно встала на колени."
    pav "Думаешь, школу заканчиваешь и всё – на родню насрать, творю что хочу?"
    un "Я готовилась…"
    pav "Нахер твою учебу. {w}Давно б уже бросила, девять классов есть и хватит. Вон — соседка твоя — Лилька, работает уже сколько на мясокомбинате, а ведь вы одногодки."
    "Отчим звучно отрыгнул и плеснул в стакан ещё водки."
    un "Я собираюсь в институт."
    "Тихо, но твердо сказала Лена. {w}Теперь, когда тяжесть в груди стала невыносима, она снова ощутила поднимающуюся откуда-то из глубины злобу, направленную на это пьяное ничтожество."
    pav "Че? Какой, в жопу, институт?"
    "Выпучил глаза отчим."
    un "Медицинский."
    "Сжимая руки в кулачки, прошептала девушка. Ногти впились в ладони, до крови."
    pav "Никаких грёбаных институтов!{w} Что, тебя еще пять лет на шее держать? Много хочешь.{w} Короче…"
    "Его понесло. Длинная, нудная, бессвязная, изрядно приправленная матом речь о том, как он — герой — их вообще терпит. Как надо делать, как не надо делать, как они должны, а он не должен."
    "Тяжесть в груди нарастала. Казалось, грудная клетка сейчас взорвется и забрызгает кухню кровью и осколками ребер."
    "Лена хихикнула. {w}Сначала тихо. {w}Потом громче.{w} А потом залилась истерическим хохотом. {w}Павел замолчал и с недоумением посмотрел на девушку."
    un "Заткнись…"
    play music music_list["doomed_to_be_defeated"] fadein 3
    pav "Что?"
    "Удивился мужик."
    un "- Заткнись… {w}Заткнись… {w}Заткнись! {w}Я сказала! ЗАТКНИСЬ! {w}Гребаный урод!"
    "Лена закричала, выхватывая нож из кармана школьной формы. {w}Годы издевательств над ней и матерью, проблемы в школе и прочее переполнили чашу терпения и злоба прорвалась наружу."
    "Девушка рванулась вперед, намереваясь ударить отчима ножом в живот, но тот от испуга вскочил, опрокинув стол, о который она и споткнулась. Вылетевший из руки нож залетел под холодильник."
    pav "Ах, ты ж сука!"
    "Первоначальный испуг мигом сменился яростью и мужик с криком бросился пинать ее ногами.{w} Подбежавшую жену он грубо оттолкнул в сторону, та ударилась затылком о стену и сползла вниз. "
    "Схватив Лену за волосы, отчим грубо вздернул ее вверх и принялся бить ее по лицу ладонью наотмашь. После пары ударов девушка потеряла сознание."
    pav "Я тебе покажу, тварь!"
    "Орал он исступлено, брызжа слюной."
    pav "Я тебя научу!"
    stop music
    play music music_list["faceless"] fadein 3
    "Занесенную для очередного удара руку вдруг рвануло назад, вырывая плечо из сустава. {w} Павел взвыл от боли и выпустил падчерицу. Пол и потолок мелькнули перед глазами, удар спиной о стенку коридора вышиб весь воздух из легких."
    "Отчим захрипел и выпучил глаза – перед ним стоял паренек лет 17-18 в пионерском галстуке, шортах и белой рубашке.{w} Пионер протянул руки к его горлу и легко оторвал его стокилограммовую тушу от пола. "
    "Из-под челки на Павла уставились горящие дикой яростью глаза. Он откинул голову назад и ударил мужчину лбом в переносицу, раз, другой, напрочь вышибая сознание из пьяного тела."
    "***"
    "Привязав мужика к стулу бельевыми веревками и заткнув ему рот грязным носком, пионер поднял на руки Лену и отнес ее в комнату. {w}Очнувшаяся мать следила за незнакомцем испуганным взглядом. {w}Тот поставил табуретку перед связанным, потом повернулся к матери Лены и сказал ей:"
    me "Сделай дочери холодный компресс, закрой дверь и сиди с ней. Если она очнется, не вздумай выпускать."
    "Та быстро закивала."
    me "На кухню не заходить, пока не скажу. Понятно?"
    "От его тихого голоса кровь стыла в жилах. Поскуливающая женщина, схватив полотенце выбежала из кухни. {w}Пионер повернулся к очухавшемуся мужику. "
    "Тот следил за ним расширившимися от ужаса глазами и пытался что-то мычать. {w}Он сразу заткнулся, когда страшный подросток обхватил его голову руками и приблизил к нему свое лицо."
    me "А теперь смотри мне в глаза, падаль. {w}Убил бы тебя, суку, но ты мне нужен."
    "Павел встретился с ним взглядом и обмяк. {w}Широко открытые глаза пионера, казалось, выворачивали душу наизнанку."
    me "С этого момента ты будешь жить только для Лены, твоя жизнь ничто по сравнению с её. {w}Итак, даю установку. {w}Один, два, три…"
    "***"
    stop music
    play music music_list["lightness"] fadein 3
    "Чья-то рука ласково гладила по волосам, давая ощущение тепла и защищенности. {w}Знакомое чувство, но Лена никак не могла вспомнить откуда она знает эти ощущения. {w}Прямо как тогда, в лагере, год назад… Она резко распахнула глаза."
    un"Семен?"
    "Ее комната. Она пуста. Больше никого. Показалось. Часы показывали 7 утра. В дверь постучали."
    mav "Леночка. Вставай, кушать пора."
    "Лена не желала выходить на кухню и встречаться с отчимом. Почему-то она не помнила, чем закончилось ссора, но, зная себя в ярости, а так же злобный характер отчима, вряд ли сейчас все будет нормально."
    un "Я не голодна."
    mav "Леночка, не бойся."
    "Голос матери был на удивление жизнерадостным. {w}Странно, когда Павел пьет, наутро он злой как собака и все его бесят."
    "А так как запой его затянулся, мать Лены пребывала в подавленном состоянии вот уже несколько недель, чуть свет убегая на работу. А тут завтрак!"
    mav "Все в порядке, выходи давай."
    "Встав с кровати, Лена пошла на кухню. Мать стояла около плиты и УЛЫБАЯСЬ готовила омлет. {w}Павел сидел за столом и пил{w} чай. {w}ЧАЙ!? {w}Кстати, выглядел он странно — исхудавший, словно сбросил за ночь десяток килограмм, глаза напуганные, заметно трясутся руки. "
    "Увидев Лену, он подскочил как ужаленный и бросился выдвигать для нее стул."
    pav "Садись, садись, Леночка!"
    "Та в ступоре смотрела на эту суету."
    pav "Ты главное не беспокойся, кушай, готовься к экзаменам, к институту. {w}Это для тебя сейчас самое важное, а я сейчас побегу, работу себе найду. {w}В лучший медицинский поступишь."
    "Протараторив это, он выбежал в коридор.{w} Лена удивленно смотрела ему вслед – перемена, случившаяся с отчимом, была поразительна. Она пожала плечами и принялась за еду."
    jump rfe_part2
label rfe_part2:
    
return