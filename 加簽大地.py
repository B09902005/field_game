import random

class course():
    def __init__(self):
        self.credit = 0
        self.way = '有前往加簽者皆可成功加簽'
        self.time = '一早'
        self.grade = ['A+','A+','A+','A+','A+','A+']
        self.number = 0
        self.code = 0

class player():
    def __init__(self):
        self.name = '你'
        self.good = '身份'
        self.bad = '身份'
        self.timetable = [[],[],[],[],[],[],[],[],[],[]]
        self.green = []
        self.choose = [False,False,False,False,False,False,False,False,False,False]

empty = course()
empty.credit = 0
empty.grade = '                                    '
empty.number = 'csee'

forest = course()
forest.credit = 3
forest.grade = ['A-','A-','A ','A ','A+','A+']
forest.number = 99999

def rule():
    print('遊戲說明：想看故事背景請輸入1。想看遊戲流程請輸入2。想看選課系統介紹請輸入3。'
          '想看課程介紹請輸入4。想看玩家被動效果介紹請輸入5。想看作者的話請輸入6。想退出說明請輸入0。')
    a = input()
    if (a == '0'):
        return
    if (a not in {'0','1','2','3','4','5','6'}):
        return rule()
    print('-------------------------------------以下是說明----------------------------------')
    if (a == '1'):
        print('| 故事背景：                                                                    |')
        print('|    你和你幾個朋友（啊我忘了你沒有朋友。那就拿ＮＰＣ代替吧）在選課初選時，因為錯過了選課的時間 |')
        print('| ，因此都只有選上那些必帶的必修課程。為了把不夠的學分補足，你們必須在開學前兩週去跑加簽大地，想 |')
        print('| 辦法簽到更多課程。當然，也不是所有課都能選，你還是需要藉由有智慧的選課，來保持你這學期的GPA。 |')
        print('| 這場遊戲最後會以大家的GPA以及學分數來綜合評斷哪位玩家勝出。（希望這個遊戲能讓你以後不要玩到現 |')
        print('| 實世界中的加簽大地~                                                             |')
    if (a == '2'):
        print('| 以下為遊戲大致流程：開局階段、加簽階段、結算成績。                                    |')
        print('|  開局階段：分配玩家(總共五位)分別的的正面、負面效果，還有必修課的時間。                   |')
        print('|  加簽階段：玩家要想辦法去搶課，好讓自己能夠得到一張夠好的課表。                          |')
        print('|  結算成績：公布玩家在選到的每門課中，得到的學期成績。                                  |')
        print('| 這場遊戲的勝利條件，是要在遊戲中贏得最高的遊戲分數，遊戲分數最高者勝出。                   |')
        print('| (遊戲分數的計算方式為：(100 * GPA) + (2 * 學分數)。)                               |')
        print('| (舉例來說，若某玩家總共修了20學分的課，且最終的GPA是3.70，那麼該玩家拿到的分數就是 410 分。 |\n')
        a = input('|                                 按enter鍵以繼續                               |\n')
        print('| 以下詳細介紹開局階段：                                                          |')
        print('|  一開始，每個人都會隨機分配到一種正面效果和一種負面效果(關於效果的資訊詳見被動效果介紹)。    |')
        print('|  接下來，就會開始分配每個人必修課的時間。原則上一個人會有兩門必修課，除非玩家有免修或者重修。 |')
        print('|  每個人的課表中，會有十個時段，分別是一週五天的早上和下午，必修課會被隨機分配在其中兩個時段。 |')
        print('| (必修課是固定的，在遊戲中沒辦法去退選它，此外你也不能在有必修課的時段跑去搶其他課程的授權碼。)|')
        print('| (這兩門必修課都是3學分，而這兩門的等第欄分別為 B-,B-,B,B,B+,B+ 及 A-,A-,A,A,A+,A+。) |')
        print('| (關於等第欄的詳細說明，詳見課程介紹。)                                             |\n')
        a = input('|                                 按enter鍵以繼續                               |\n')
        print('| 以下詳細介紹加簽階段：                                                          |')
        print('|  加簽階段的行程共有兩週，並被分成二十個部分(共兩週，一週有五天，一天分為早上和下午)。       |')
        print('|  在這兩週的時間，玩家必須想盡辦法在一、二、三類加簽的課程中，搶到盡可能多的好課並填入課表中。 |')
        print('| 以下介紹三種加簽方式的進行模式：                                                  |')
        print('| 二類加選：這二十段時間，每段時間都會釋出兩門課程，並且公佈該課程的學分數、加簽方式與等第欄，  |')
        print('|         玩家可依據這些資訊，來決定自己要去搶哪一門課的授權碼(兩門最多選一門，或者都不選)。  |')
        print('|         每位玩家決定好後，便按照所公布的加簽方式來做分發，決定哪一些玩家能夠成功搶到授權碼。 |')
        print('|         玩家在搶到授權碼後，到選課系統加選這門課，就能讓這門課進入玩家的課表中。          |')
        print('| 一、三類加選：一、三類加選的課程，會公佈在選課系統，玩家可以到選課系統上面查詢，            |')
        print('|            玩家可以依據選課系統上公布的學分數與等第欄，來決定自己要不要加選這些課。       |')
        print('|            一類加簽的課程加選後，會直接進入到玩家的課表，                            |')
        print('|            三類加簽的課程加選後，會在選課系統分發(詳見選課系統介紹)時，概率性進入玩家課表。|')
        print('| 在這二十段時間結束後，玩家對自己的課表進行最後的統整，並讓選課系統做第四次(最後一次)的分發，  |')
        print('| 分發完後的課表，就是玩家這個學期的最終課表(啥？你說人工加簽？這個遊戲沒再跟你搞這個的啦！)。  |\n')
        a = input('|                                 按enter鍵以繼續                               |\n')
        print('| 以下詳細介紹成績結算：                                                           |')
        print('| 在加簽階段結束後(第四次分發完後)，所有人這學期的課表就已經確定。接著時間很快的來到了學期末。  |')
        print('| 學期末，會公布每位玩家在各門課拿到的學期成績。學期成績會依照課程的等第欄來給(詳見課程屬性介紹) |')
        print('| 根據玩家的課表及各科成績，就可以算出每位玩家再這場遊戲中拿到的分數。                      |')
        print('| 首先，如果有人修的學分數不到15，那他得到的分數就是0分。(因為這個遊戲是不給低修的qq)         |')
        print('| (然而，因為這個遊戲是允許超修的，所以修的學分數是可以超過25的。)                         |')
        print('| 其他人的遊戲分數則為：(100 * GPA) + (2 * 學分數)。                                 |')
        print('| (舉例來說，若某玩家總共修了20學分的課，且最終的GPA是3.70，那麼該玩家拿到的分數就是 410 分。)|')
        print('| 算出每位玩家的遊戲分數後，分數最高者勝出。                                           |\n')
    if (a == '3'):
        print('| 選課系統介紹：                                                                 |')
        print('| 在加簽階段中，玩家都能登入選課系統。以下介紹選課系統的功能(應該跟現實世界的選課系統差不多)：  |')
        print('| 課程加選：一類加選：輸入課程流水號即可加選課程。                                      |')
        print('|         二類加選：輸入課程流水號與授權碼即可加選課程。                               |')
        print('|         三類加選：在課程網將課程加入選課志願，並在分發時以一定的概率成功加選。            |')
        print('|         (附註：三類加簽的課程中，每門課每次分發選上的概率皆在10%以下，且越甜的課機率越低。) |')
        print('|         (附註：遊戲中，總共有四次分發，時間跟台大選課系統一樣(兩個禮拜的週三與週六)。)     |')
        print('| 課程退選：玩家可以藉由輸入課程流水號，把課表中覺得不滿意或是被衝堂的非必修課程退選掉。       |')
        print('| 查看時間表：玩家可以在選課系統中查看自己目前的課表，以及已經放入志願的三類加選課程。         |')
    if (a == '4'):
        print('| 課程介紹：                                                                    |')
        print('| 每個課程可能具有以下的資料：                                                      |')
        print('| 課程流水號 ： 會是一個隨機的五位數。在課程網加退選課程的時候會需要輸入流水號。             |')
        print('| 課程時間  ： 基本上都會在禮拜一到禮拜五的早上或下午(共10種時段)，只有森多概在禮拜六。       |')
        print('| 學分數    ： 每門課的學分數會落在1到4區間(學分數是2或3的課最常出現)。                   |')
        print('| 加簽方式  ： 有很多種，選上的機率也不見得一樣。在二類加簽時你可以藉此評估選上課程的難易度。   |')
        print('|            (基本上加簽的方式有兩類：一是固定人數，從選該課的玩家中發出固定數量的授權碼。   |')
        print('|                                二是固定難度，讓玩家骰骰子，骰出夠大數字者得到授權碼。) |')
        print('| 等第欄    ： 等第欄中會有六個等第，由低排到高，代表你修這門課有可能會拿到的學期成績。       |')
        print('|             在學期末(結算成績)時，會從六個等第中抽出一個，表示你在這門課實際拿到的學期成績。|')
        print('|            (舉例來說，如果等第欄上寫著[A-,A-,A,A,A+,A+]，在沒有相關被動效果的情況之下， |')
        print('|             玩家有2/6的機率會拿到A-，2/6的機率會拿到A，2/6的機率會拿到A+。)           |')
        print('|            (呈上例，若玩家有好學生效果，表示該玩家分別有2/4的機率拿A，和2/4的機率拿A+。)  |')
    if (a == '5'):
        print('| 玩家被動效果介紹：                                                              |')
        print('| 遊戲共五位玩家(你和四個ＮＰＣ)。你們五個在開局的時候，會各自隨機分配到一個正面效果與一個負面效 |')
        print('| 果。你們五個人得到的效果都不會重複。                                                |\n')
        a = input('|                                 按enter鍵以繼續                               |\n')
        print('| 以下介紹各種可能出現的正面效果：                                                   |')
        print('|  免修仔：開局階段時，分配到的必修課門數減一(剩下 A-,A-,A,A,A+,A+ 的那門必修課)。         |')
        print('|  甜課仔：開局階段時，分配到的必修課等第欄分別改為 B,B,B,B+,B+,B+ 和 A,A,A,A+,A+,A+。   |')
        print('|  森多概：開局階段時，多獲得一門課(3學分，時間在禮拜六，等第欄是 A-,A-,A,A,A+,A+ )。      |')
        print('|  加簽王：加簽階段中，只要遇到需要骰骰子的環節，都不會骰到1。                            |')
        print('|  好學生：成績結算時，每一門課都不會抽到等第欄中，最左邊的兩個等第。                       |\n')
        a = input('|                                 按enter鍵以繼續                               |\n')
        print('| 以下介紹各種可能出現的負面效果：                                                   |')
        print('|  重修仔：開局階段時，分配到的必修課門數加一(要多修一門 B-,B-,B,B,B+,B+ 的必修課)。       |')
        print('|  人品差：加簽階段中，凡是三類加簽的課程一定選不上。                                    |')
        print('|  睡過頭：加簽階段中，只要遇到星期一早上與星期五早上都會睡過頭，無法去搶授權碼。             |')
        print('|  八面骰：加簽階段中，用的骰子會是八面骰，八個面分別是-1、0、1、2、3、4、5、6。            |')
        print('|  不用功：成績結算時，每一門課都不會抽到等第欄中，最右邊的兩個等第。                       |')
    if (a == '6'):
        print('| 作者的話：                                                                    |')
        print('|    這款遊戲是由一個資工系的可悲魯蛇所製作，因為他開學的時候總是飽受地獄加簽大地所苦，所以基於 |')
        print('| 興趣(才不是！)，無聊的他決定利用暑假閒閒沒事做的時間來製作這個遊戲，也順便用這遊戲來發洩自己  |')
        print('| 心中的深厚怨念，並看看能不能藉此消點業障，好讓他下學期開學時可以人品爆發，不用再去跑加簽大地。 |')
    print('-------------------------------------說明結束。---------------------------------\n')
    return rule()

def initialize(attribute):
    array = []
    if (attribute == 'good'):
        return ['森多概','好學生','加簽王','免修仔','甜課仔']
    if (attribute == 'bad'):
        return ['重修仔','睡過頭','人品差','八面骰','不用功']
    if (attribute == 'credit'):
        for i in range (5):
            array.append(1)
        for i in range (15):
            array.append(2)
        for i in range (25):
            array.append(3)
        for i in range (5):
            array.append(4)
        return array
    if (attribute == 'way'):
        for i in range (1):
            array.append('有前往加簽者皆可成功加簽      ')
        for i in range (6):
            array.append('骰一次骰子，骰到4以上即成功加簽 ')
        for i in range (6):
            array.append('骰一次骰子，骰到5以上即成功加簽 ')
        for i in range (8):
            array.append('骰一次骰子，骰到6以上即成功加簽 ')
        for i in range (2):
            array.append('骰兩次骰子，加總11以上即成功加簽')
        for i in range (2):
            array.append('骰兩次骰子，加總12以上即成功加簽')
        for i in range (12):
            array.append('在加簽者中，選出恰好一人可加簽  ')
        for i in range (3):
            array.append('在加簽者中，選出恰好兩人可加簽  ')
        return array
    if (attribute == 'grade'):
        for i in range (3):
            array.append(['A+','A+','A+','A+','A+','A+'])
        for i in range (3):
            array.append(['A ','A ','A ','A+','A+','A+'])
        for i in range (3):
            array.append(['A ','A ','A ','A ','A ','A '])
        for i in range (3):
            array.append(['A-','A-','A-','A ','A ','A '])
        for i in range (3):
            array.append(['A-','A-','A-','A-','A-','A-'])
        for i in range (5):
            array.append(['A-','A-','A ','A ','A+','A+'])
        for i in range (5):
            array.append(['B+','B+','B+','A-','A-','A-'])
        for i in range (2):
            array.append(['B+','B+','B+','B+','B+','B+'])
        for i in range (2):
            array.append(['B ','B ','B ','B+','B+','B+'])
        for i in range (2):
            array.append(['B ','B ','B ','B ','B ','B '])
        for i in range (2):
            array.append(['B-','B-','B-','B ','B ','B '])
        for i in range (2):
            array.append(['B-','B-','B-','B-','B-','B-'])
        for i in range (5):
            array.append(['B-','B-','B ','B ','B+','B+'])
        for i in range (2):
            array.append(['F ','A+','A+','A+','A+','A+'])
        for i in range (2):
            array.append(['C+','C+','C+','B-','B-','B-'])
        for i in range (2):
            array.append(['C+','C+','C+','C+','C+','C+'])
        for i in range (2):
            array.append(['C ','C ','C ','C ','C ','C '])
        for i in range (2):
            array.append(['C-','C-','C-','C-','C-','C-'])
        return array
    return array

def players_test(players):
    week = ['禮拜一','禮拜二','禮拜三','禮拜四','禮拜五','星期六']
    best = {'森多概':'開局階段時，多獲得一門課(3學分，時間在禮拜六，等第欄是 A-,A-,A,A,A+,A+ )。',
            '好學生':'成績結算時，每一門課都不會抽到等第欄中，最左邊的兩個等第。',
            '加簽王':'加簽階段中，只要遇到需要骰骰子的環節，都不會骰到1。',
            '免修仔':'開局階段時，分配到的必修課門數減一(剩下 A-,A-,A,A,A+,A+ 的那門必修課)。',
            '甜課仔':'開局階段時，分配到的必修課等第欄分別改為 B,B,B,B+,B+,B+ 和 A,A,A,A+,A+,A+。'}
    worst = {'重修仔':'開局階段時，分配到的必修課門數加一(要多修一門 B-,B-,B,B,B+,B+ 的必修課)。',
             '睡過頭':'加簽階段中，只要遇到星期一早上與星期五早上都會睡過頭，無法去搶授權碼。',
             '人品差':'加簽階段中，凡是三類加簽的課程一定選不上。',
             '八面骰':'加簽階段中，用的骰子會是八面骰，八個面分別是-1、0、1、2、3、4、5、6。',
             '不用功':'成績結算時，每一門課都不會抽到等第欄中，最右邊的兩個等第。'}
    for i in range (5):
        print('----------------------------------以下是',players[i].name,'的資料。-----------------------------------')
        print('')
        print('名字：',players[i].name)
        print('好效果：' ,players[i].good,'：',best[players[i].good])
        print('壞效果：' ,players[i].bad,'：',worst[players[i].bad])
        print()
        print ('              早上                                   下午')
        print ('     學分              等第                  學分             等第')
        for j in range (5):
            print (week[j],players[i].timetable[2*j].credit,players[i].timetable[2*j].grade,players[i].timetable[2*j+1].credit,players[i].timetable[2*j+1].grade)
        if (players[i].good == '森多概'):
            print (week[5],forest.credit,forest.grade)
        print('')
        print('----------------------------------以上是',players[i].name,'的資料。-----------------------------------')
        a = input('按enter以繼續')
    return

def attribute(good,bad):
    time = ['禮拜一早上','禮拜一下午','禮拜二早上','禮拜二下午','禮拜三早上','禮拜三下午',
                '禮拜四早上','禮拜四下午','禮拜五早上','禮拜五下午']
    players = [player() for i in range (5)]
    players[0].name = '你自己'
    players[1].name = '對手一'
    players[2].name = '對手二'
    players[3].name = '對手三'
    players[4].name = '對手四'

    for i in range (5):
        players[i].timetable = [empty for i in range (10)]

    best = {'森多概':'開局階段時，多獲得一門課(3學分，時間在禮拜六，等第欄是 A-,A-,A,A,A+,A+ )。',
            '好學生':'成績結算時，每一門課都不會抽到等第欄中，最左邊的兩個等第。',
            '加簽王':'加簽階段中，只要遇到需要骰骰子的環節，都不會骰到1。',
            '免修仔':'開局階段時，分配到的必修課門數減一(剩下 A-,A-,A,A,A+,A+ 的那門必修課)。',
            '甜課仔':'開局階段時，分配到的必修課等第欄分別改為 B,B,B,B+,B+,B+ 和 A,A,A,A+,A+,A+。'}
    worst = {'重修仔':'開局階段時，分配到的必修課門數加一(要多修一門 B-,B-,B,B,B+,B+ 的必修課)。',
             '睡過頭':'加簽階段中，只要遇到星期一早上與星期五早上都會睡過頭，無法去搶授權碼。',
             '人品差':'加簽階段中，凡是三類加簽的課程一定選不上。',
             '八面骰':'加簽階段中，用的骰子會是八面骰，八個面分別是-1、0、1、2、3、4、5、6。',
             '不用功':'成績結算時，每一門課都不會抽到等第欄中，最右邊的兩個等第。'}
    a = input('遊戲開始。按enter以分配玩家正面效果：')
    for i in range (5):
        a = random.randint(0,4-i)
        players[i].good = good[a]
        print (players[i].name,' ： ',good[a],'：',best[good[a]])
        good.pop(a)
    print ('\n')
    a = input('按enter以分配玩家負面效果：')
    for i in range (5):
        a = random.randint(0,4-i)
        players[i].bad = bad[a]
        print (players[i].name,' ： ',bad[a],'：',worst[bad[a]])
        bad.pop(a)
    print ('\n')
    
    require_num = [2,2,2,2,2]
    for i in range (5):
        if (players[i].good == '免修仔'):
            require_num[i] = require_num[i] - 1
        if (players[i].bad == '重修仔'):
            require_num[i] = require_num[i] + 1
    a = input('按enter以以分配必修課時間：')
    for i in range (5):
        a = [0,1,2,3,4,5,6,7,8,9]
        required_list = []
        for j in range (require_num[i]):
            b = random.randint(0,9-j)
            players[i].timetable[a[b]] = course()
            players[i].timetable[a[b]].credit = 3
            players[i].timetable[a[b]].way = '必修'
            players[i].timetable[a[b]].time = time[a[b]]
            temp3 = 0
            while (repeated(required_list,temp3)):
                temp3 = random.randint(10000,99998)
            players[i].timetable[a[b]].number = temp3
            required_list.append(temp3)
            if (players[i].good == '甜課仔'):
                if (j in {1,2}):
                    players[i].timetable[a[b]].grade = ['B ','B ','B ','B+','B+','B+']
                else:
                    players[i].timetable[a[b]].grade = ['A ','A ','A ','A+','A+','A+']
            else:
                if (j in {1,2}):
                    players[i].timetable[a[b]].grade = ['B-','B-','B ','B ','B+','B+']
                else:
                    players[i].timetable[a[b]].grade = ['A-','A-','A ','A ','A+','A+']
            a.pop(b)
        if (players[i].good == '森多概'):
            players[i].timetable.append(forest)
    a = input('必修課已分配完畢，以下是五位玩家分配到的效果與必修課時間(按enter以繼續)：')
    return (players,required_list)

def repeated(course_list,temp3):
    if (temp3 == 0):
        return True
    for i in range (len(course_list)):
        if (course_list[i] == temp3):
            return True
    return False

def init_course(credit,grade,way):
    time = ['禮拜一早上','禮拜一下午','禮拜二早上','禮拜二下午','禮拜三早上','禮拜三下午',
                '禮拜四早上','禮拜四下午','禮拜五早上','禮拜五下午']
    aaa = [1,1,3,3,3,3,3,3,3,3]
    course_list = []
    for i in range (50):
        temp_course = course()
        temp1 = random.randint(0,len(credit)-1)
        temp2 = random.randint(0,len(grade)-1)
        temp3 = 0
        while (repeated(course_list,temp3)):
            temp3 = random.randint(10000,99998)
        temp4 = random.randint(1000000000,9999999999)
        if (i <= 39):
            temp_course.time = time[(i//2) % 10]
            temp5 = random.randint(0,len(way)-1)
            temp_course.way = way[temp5]
            way.pop(temp5)
        else:
            temp6 = random.randint(0,len(aaa)-1)
            temp_course.time = time[i-40]
            if (aaa[temp6] == 3):
                temp_course.way = '三類加選，概率性成功加簽       '
            else:
                temp_course.way = '一類加選，必定成功加簽         '
            aaa.pop(temp6)
        temp_course.credit = credit[temp1]
        temp_course.grade = grade[temp2]
        temp_course.number = temp3
        temp_course.code = temp4
        credit.pop(temp1)
        grade.pop(temp2)
        course_list.append(temp_course)
    require = len(course_list) - 50
    for i in range (require):
        course_list.pop(0)
    return course_list

def print_course(lesson,i):
    if (i == 0):#test
        print('課程編號：',lesson.number,'   時間：',lesson.time,
              '   學分數：',lesson.credit,'   授權碼：',lesson.code)
        print('加簽方式：',lesson.way,'  等第：',lesson.grade)
    if (i == 2):#two
        print('課程編號：',lesson.number,'   時間：',lesson.time,
              '   學分數：',lesson.credit,)
        print('加簽方式：',lesson.way,'  等第欄：',lesson.grade)
    if (i == 1):#green
        print('課程編號：',lesson.number,'   時間：',lesson.time,
              '   學分數：',lesson.credit,'   授權碼：',lesson.code,'  等第欄：',lesson.grade)    
    if (i == 3):#three
        print('課程編號：',lesson.number,'   時間：',lesson.time,
              '   學分數：',lesson.credit,'  等第欄：',lesson.grade)
    return

def sweet(course,player):
    gpa = 0
    possibility = 0
    for i in range (6):
        gpa += value(course.grade[i])
        possibility += 1
    if (player.good == '好學生'):
        gpa -= value(course.grade[0])
        gpa -= value(course.grade[1])
        possibility -= 2
    if (player.bad == '不用功'):
        gpa -= value(course.grade[5])
        gpa -= value(course.grade[4])
        possibility -= 2
    return gpa / possibility

def probability(course):
    if (course.way == '有前往加簽者皆可成功加簽      '):
        return 1
    if (course.way == '骰一次骰子，骰到4以上即成功加簽 '):
        return 1/2
    if (course.way == '骰一次骰子，骰到5以上即成功加簽 '):
        return 1/3
    if (course.way == '骰一次骰子，骰到6以上即成功加簽 '):
        return 1/6
    if (course.way == '骰兩次骰子，加總11以上即成功加簽'):
        return 1/12
    if (course.way == '骰兩次骰子，加總12以上即成功加簽'):
        return 1/36
    if (course.way == '在加簽者中，選出恰好一人可加簽  '):
        a = random.randint(1,5)
        return 1/a
    if (course.way == '在加簽者中，選出恰好兩人可加簽  '):
        a = random.randint(2,5)
        return 2/a

def better(course1,course2,player,x):
    when = what_time(course1)
    if (player.timetable[when].way == '必修'):
        return 0
    if (x == 2):
        if (when in {0,8}) and (player.bad == '睡過頭'):
            return 0
        ans = 0
        lesson = player.timetable[when]
        if (lesson != empty) and (sweet(lesson,player) > sweet(course1,player)):
            if (sweet(lesson,player) > sweet(course2,player)):
                ans = 0
            else:
                ans = 2
        elif (lesson != empty) and (sweet(lesson,player) > sweet(course2,player)):
            if (sweet(lesson,player) > sweet(course1,player)):
                ans = 0
            else:
                ans = 1
        else:
            if (sweet(course1,player) > sweet(course2,player)):
                if (probability(course1) >= probability(course2)):
                    ans = 1
                else:
                    ans = random.randint(1,2)
            elif (sweet(course1,player) < sweet(course2,player)):
                if (probability(course1) <= probability(course2)):
                    ans = 2
                else:
                    ans = random.randint(1,2)
            else:
                if (probability(course1) > probability(course2)):
                    ans = 1
                elif (probability(course1) < probability(course2)):
                    ans = 2
                else:
                    ans = random.randint(1,2)
            if (lesson == empty):
                temp = random.randint(1,10)
                if (ans == 1):
                    lesson = course1
                if (ans == 2):
                    lesson = course2
                if (sweet(lesson,player) <= 2.6):
                    if (temp <= 8):
                        ans = 0
                elif (sweet(lesson,player) <= 2.9):
                    if (temp <= 4):
                        ans = 0
                elif (sweet(lesson,player) <= 3.2):
                    if (temp <= 2):
                        ans = 0
        return ans
    elif (x == 3):
        ans = 0
        if (course2 == empty):
            ans = 1
            temp = random.randint(1,10)
            if (sweet(course1,player) <= 2.4):
                if (temp <= 8):
                    ans = 0
            elif (sweet(course1,player) <= 2.8):
                if (temp <= 4):
                    ans = 0
            elif (sweet(course1,player) <= 3.2):
                if (temp <= 2):
                    ans = 0
        elif (sweet(course1,player) > sweet(course2,player)):
            ans = 1
        elif (sweet(course1,player) < sweet(course2,player)):
            ans = 0
        elif (course1.credit > course2.credit):
            ans = 1
        else:
            ans = 0
        return ans
    return 0

def what_time(course):
    time = ['禮拜一早上','禮拜一下午','禮拜二早上','禮拜二下午','禮拜三早上','禮拜三下午',
                '禮拜四早上','禮拜四下午','禮拜五早上','禮拜五下午']
    when = 10
    for i in range (10):
        if (course.time == time[i]):
            when = i
    return when

def fight(two_course,players,which_to_choose):
    when = what_time(two_course[1])
    original = players[0].timetable[when]
    success = [[],[],[]]
    nobody = True
    for i in {1,2}:
        if (which_to_choose[i] == []):
            continue
        for j in which_to_choose[i]:
            temp = random.randint(1,6)
            tenp = random.randint(1,6)
            if (players[j].good == '加簽王') and (players[j].bad == '八面骰'):
                temp = random.randint(0,6)
                tenp = random.randint(0,6)
            elif (players[j].good == '加簽王'):
                temp = random.randint(2,6)
                tenp = random.randint(2,6)
            elif (players[j].bad == '八面骰'):
                temp = random.randint(-1,6)
                tenp = random.randint(-1,6)
            if (two_course[i].way == '有前往加簽者皆可成功加簽      '):
                players[j].timetable[when] = two_course[i]
                success[i].append(j)
            elif (two_course[i].way == '骰一次骰子，骰到4以上即成功加簽 '):
                if (temp >= 4):
                    players[j].timetable[when] = two_course[i]
                    success[i].append(j)
            elif (two_course[i].way == '骰一次骰子，骰到5以上即成功加簽 '):
                if (temp >= 5):
                    players[j].timetable[when] = two_course[i]
                    success[i].append(j)
            elif (two_course[i].way == '骰一次骰子，骰到6以上即成功加簽 '):
                if (temp >= 6):
                    players[j].timetable[when] = two_course[i]
                    success[i].append(j)
            elif (two_course[i].way == '骰兩次骰子，加總11以上即成功加簽'):
                if (temp + tenp >= 11):
                    players[j].timetable[when] = two_course[i]
                    success[i].append(j)
            elif (two_course[i].way == '骰兩次骰子，加總12以上即成功加簽'):
                if (temp + tenp >= 12):
                    players[j].timetable[when] = two_course[i]
                    success[i].append(j)
        if (two_course[i].way == '在加簽者中，選出恰好一人可加簽  '):
            temp = random.randint(0,len(which_to_choose[i])-1)
            players[which_to_choose[i][temp]].timetable[when] = two_course[i]
            success[i].append(which_to_choose[i][temp])
        elif (two_course[i].way == '在加簽者中，選出恰好兩人可加簽  '):
            temp = random.randint(0,len(which_to_choose[i])-1)
            players[which_to_choose[i][temp]].timetable[when] = two_course[i]
            success[i].append(which_to_choose[i][temp])
            which_to_choose[i].pop(temp)
            if (which_to_choose[i] != []):
                temp = random.randint(0,len(which_to_choose[i])-1)
                players[which_to_choose[i][temp]].timetable[when] = two_course[i]
                success[i].append(which_to_choose[i][temp])
        if (players[0].timetable[when] != original):
            players[0].timetable[when] = original
            players[0].green.append(two_course[i])
        for j in success[i]:
            if (i == 1):
                print('恭喜',players[j].name,'拿到上面的課程的授權碼')
            if (i == 2):
                print('恭喜',players[j].name,'拿到下面的課程的授權碼')
            nobody = False
    if (nobody == True):
        print ('很可惜，這兩門課都沒有人拿到授權碼。')
    a = input('                            輸入enter以繼續                          ')
    return players

def two(players, course_list, i):
    time = ['禮拜一早上','禮拜一下午','禮拜二早上','禮拜二下午','禮拜三早上','禮拜三下午',
                '禮拜四早上','禮拜四下午','禮拜五早上','禮拜五下午']
    when = what_time(course_list[2*i])
    print('\n\n\n第',i//10 + 1,'週，',time[when],'了。','按enter以繼續。')
    a = input()
    print('以下是這個時段你能去搶授權碼的兩堂課：')
    print('-------------------------------------------------------------------')
    print_course(course_list[2*i],2)
    print('-------------------------------------------------------------------')
    print_course(course_list[2*i+1],2)
    print('-------------------------------------------------------------------')
    correct = {'0','1','2'}
    if (players[0].timetable[when].way == '必修'):
        correct = {'0'}
    if (players[0].bad == '睡過頭') and (i in {0,8,10,18}):
        correct = {'0'}
    a = 'CS>EE'
    which_to_choose = [[],[],[]]
    while (a not in correct):
        if (a in {'1','2'}):
            if (players[0].timetable[when].way == '必修'):
                a = input('你的必修衝堂了，沒辦法去加簽，因此無法輸入1或2。\n')
            else:
                a = input('你睡過頭了，沒辦法去加簽，因此無法輸入1或2。\n')
        else:
            print('若想加簽上面的課，請輸入1，若想加簽下面的課，請輸入2，若都不想加簽或卡到必修課，請輸入0，')
            a = input('想查看玩家狀態，請輸入a。想查看可選的課程，請輸入b。想進入課程網，請輸入c．想複習規則，請輸入d。\n')
        if (a == 'd'):
            rule()
            a = 'b'
        if (a == 'c'):
            if (i in {4,5,14,15}):
                b = input ('進行分發作業中...選課系統暫不開放。(按enter以繼續)\n')
            else:
                print('-------------------------------------------------------------------')
                players[0] = website(players[0], course_list, 'CS>EE', '0')
                a = 'b'
        if (a == 'a'):
            players_test(players)
            a = 'b'
        if (a == 'b'):
            print('以下是這個時段你能去搶授權碼的兩堂課：')
            print('-------------------------------------------------------------------')
            print_course(course_list[2*i],2)
            print('-------------------------------------------------------------------')
            print_course(course_list[2*i+1],2)
            print('-------------------------------------------------------------------')
    which_to_choose[int(a)].append(0)
    for j in range(1,5,1):
        which_to_choose[better(course_list[2*i],course_list[2*i+1],players[j],2)].append(j)
    print('以下是五位玩家的選擇：')
    option = ['都不選','上面的課程','下面的課程']
    for k in range (5):
        for j in range (3):
            if (k in which_to_choose[j]):
                print(players[k].name,' ： ',option[j])
    a = input('                        分發課程中...輸入enter以繼續                      ')
    course = [0,course_list[2*i],course_list[2*i+1]]
    players = fight(course,players,which_to_choose)
    return players

def website(player,course_list,a,b):
    if (a == 'CS>EE'):
        while (a not in {'0','1','2','3','4','5'}):
            print('歡迎來到台大選課系統。     登記一、三類加簽的課請輸入1，加選二類加簽課程請輸入2，退選課程請輸入3，')
            a = input('                       查看時間表請按4，查看選課流程請按5，退出選課系統請輸入0。\n')
        return website(player,course_list,a,'head')
    elif (a == 'seeonly'):
        while (a not in {'0'}):
            a = input ('目前系統僅開放查詢分發結果。查詢分發結果請輸入4，退出選課系統請輸入0。')
            if (a == '4'):
                print('------------------------以下是你的課程時間表：------------------------')
                time = ['禮拜一早上','禮拜一下午','禮拜二早上','禮拜二下午','禮拜三早上','禮拜三下午',
                '禮拜四早上','禮拜四下午','禮拜五早上','禮拜五下午','禮拜六全天']
                for i in range (len(player.timetable)):
                    lesson = player.timetable[i]
                    if (lesson == empty):
                        print(time[i],'：沒課')
                    elif (lesson.way == '必修'):
                        print(time[i],'：課程編號：',lesson.number,'(必修)   學分數：',lesson.credit,'   等第：',lesson.grade)
                    else:
                        print(time[i],'：課程編號：',lesson.number,'(選修)   學分數：',lesson.credit,'   等第：',lesson.grade)                
                print('------------------------以上是你的課程時間表：------------------------')
        return player
    elif (a == '0'):
        print('-------------------------------------------------------------------')
        return player
    elif (a == '1') and (b == 'head'):
        while (b not in {'0','1','2','3'}):
            b = input ('(這裡是一、三類加選區)     新增志願請輸入1，移除志願請輸入2，查看一、三類的課程請輸入3，退出一三類加選請輸入0。\n')
        return website(player,course_list,a,b)
    elif (a == '1') and (b == '0'):
        return website(player,course_list,'CS>EE',0)
    elif (a == '1') and (b == '1'):
        a = 'CS>EE'
        while (a != '0'):
            exist = False
            a = input('\n請輸入想加入志願的課程編號，或輸入0回到上一頁。')
            if (a == '0'):
                break
            for i in range (10):
                if (str(course_list[40+i].number) == a):
                    exist = True
                    if (course_list[40+i].way == '一類加選，必定成功加簽         '):
                        if (player.timetable[what_time(course_list[40+i])] == empty):
                            player.timetable[what_time(course_list[40+i])] = course_list[40+i]
                            a = input('加選成功，課程已經直接進入你的課表裡。(按enter以繼續)')
                        else:
                            a = input ('和其他課衝堂了。請先將該課退選再加選此課。(按enter以繼續)')
                    else:
                        if (player.timetable[what_time(course_list[40+i])].way == '必修'):
                            a = input('可能不能加這門課耶...跟必修課衝堂了。(按enter以繼續)')
                        else:
                            player.choose[i] = True
                            a = input('加入志願成功，課程已經放入志願中。(請注意三類加選的課如果成功選上，會直接取代掉同一時段原有的課程。)(按enter以繼續)')
            if (exist == False):
                b = input ('無此課程，或此課程並非一、三類加選。按enter鍵以繼續。')
        return website(player,course_list,'1','head')
    elif (a == '1') and (b == '2'):
        a = 'CS>EE'
        while (a != '0'):
            exist = False
            a = input('\n請輸入想移出志願的課程編號，或輸入0回到上一頁。')
            if (a == '0'):
                break
            for i in range (10):
                if (str(course_list[40+i].number) == a):
                    exist = True
                    if (course_list[40+i].way == '一類加選，必定成功加簽         '):
                        a = input('退選失敗。一類加選課程請直接至退選區(課程網首頁輸入3)做退選。(按enter以繼續)')
                    else:
                        player.choose[i] = False
                        a = input('移除選擇成功，課程已經移出志願。(按enter以繼續)')
            if (exist == False):
                b = input ('無此課程，或此課程並非一、三類加選。按enter鍵以繼續。')
        return website(player,course_list,'1','head')
    elif (a == '1') and (b == '3'):
        print('以下是一、三類加簽可選的課：(按enter以繼續)')
        print('-----------------------------以下是三類加選，你已經放入志願的課----------------------------') 
        exist = False
        for i in range (10):
            if (player.choose[i] == True) and (course_list[40+i].way == '三類加選，概率性成功加簽       '):
                exist = True
                print_course(course_list[40+i],3)
        if (exist == False):
            print('無。') 
        print('\n-----------------------------以下是三類加選，你尚未放入志願的課----------------------------') 
        exist = False
        for i in range (10):
            if (player.choose[i] == False) and (course_list[40+i].way == '三類加選，概率性成功加簽       '):
                exist = True
                print_course(course_list[40+i],3)
        if (exist == False):
            print('無。')
        print('\n----------------------------------以下是一類加選的課---------------------------------') 
        for i in range (10):
            if (course_list[40+i].way == '一類加選，必定成功加簽         '):
                print_course(course_list[40+i],3)
        print('\n')
        return website(player,course_list,'1','head')
    elif (a == '2') and (b == 'head'):
        while (b not in {'0','1','2'}):
            b = input ('(這裡是二類加選區)     加選課程請輸入1，查看你有的授權碼請輸入2，退出二類加選請輸入0。\n')
        return website(player,course_list,'2',b)
    elif (a == '2') and (b == '0'):
        return website(player,course_list,'CS>EE','0')
    elif (a == '2') and (b == '1'):
        b = input ('請輸入你想加選的課程編號，或輸入0回到上一頁。\n')
        if (b == '0'):
            return website(player,course_list,'2','head')
        lesson = empty
        for i in range (40):
            if (str(course_list[i].number) == b):
                lesson = course_list[i]
                b = input ('請輸入授權碼。\n')
                if (b == str(lesson.code)):
                    if (player.timetable[what_time(lesson)] == empty):
                        player.timetable[what_time(lesson)] = lesson
                        b = input ('成功加選，可至課表查看。(按enter以繼續)')
                    else:
                        b = input ('和其他課衝堂了。請先將該課退選再加選此課。(按enter以繼續)')
                else:
                    b = input ('授權碼錯誤。(按enter以繼續)')
                break
        if (lesson == empty):
            b = input ('無此課程，或此課程並非二類加選。(按enter以繼續)')
        return website(player,course_list,'2','1')
    elif (a == '2') and (b == '2'):
        print('------------------------------以下是你所擁有的授權碼：------------------------------')
        if (player.green != []):
            for i in range (len(player.green)):
                print_course(player.green[i],1)
        else:
            print ('你目前手上沒有任何授權碼qq。')
        print('------------------------------以上是你所擁有的授權碼：------------------------------')
        a = input ('按enter以繼續。')
        return website(player,course_list,'2','head')
    elif (a == '3'):
        print('-----------------------------------以下是你的課程時間表：-----------------------------------')
        time = ['禮拜一早上','禮拜一下午','禮拜二早上','禮拜二下午','禮拜三早上','禮拜三下午',
                '禮拜四早上','禮拜四下午','禮拜五早上','禮拜五下午','禮拜六全天']
        for i in range (len(player.timetable)):
            lesson = player.timetable[i]
            if (lesson == empty):
                print(time[i],'：沒課')
            elif (lesson.way == '必修'):
                print(time[i],'：課程編號：',lesson.number,'(必修)   學分數：',lesson.credit,'   等第：',lesson.grade)
            else:
                print(time[i],'：課程編號：',lesson.number,'(選修)   學分數：',lesson.credit,'   等第：',lesson.grade)                
        print('-----------------------------------以上是你的課程時間表：-----------------------------------\n')
        t = 'CS>EE'
        while (t != '0'):
            t = input('(這裡是課程退選區)     輸入想退選的課的課程編號以退選，或輸入0回到上一頁。')
            exist = False
            if (t == '0'):
                break
            for i in range(10):
                if (t == str(forest.number)) and (player.good == '森多概'):
                    exist = True
                    b = input('別退森多概啦，好課欸。按enter鍵以繼續。')
                    break
                if (str(player.timetable[i].number) == t):
                    exist = True
                    if (player.timetable[i].way == '必修'):
                        b = input('遊戲規定不能退必修課啦！按enter鍵以繼續。')
                    elif (player.timetable[i] != empty):
                        b = '2'
                        while (b not in {'0','1'}):
                            b = input('是否確定退選此課程？是請輸入1，否請輸入0。(請注意三類加選的課在退選後有可能無法重新加入該課程)')
                        if (b == '1'):
                            player.timetable[i] = empty
                            b = input('退選成功。按enter鍵以繼續。')
                            return website(player,course_list,'3','head')
                        else:
                            b = input('取消退選。按enter鍵以繼續。')
            if (exist == False):
                b = input ('你的課表裡沒有此課程。按enter鍵以繼續。')
        return website(player,course_list,'CS>EE','0')
    elif (a == '4'):
        print('-----------------------------------以下是你的課程時間表：-----------------------------------')
        time = ['禮拜一早上','禮拜一下午','禮拜二早上','禮拜二下午','禮拜三早上','禮拜三下午',
                '禮拜四早上','禮拜四下午','禮拜五早上','禮拜五下午','禮拜六全天']
        for i in range (len(player.timetable)):
            lesson = player.timetable[i]
            if (lesson == empty):
                print(time[i],'：沒課')
            elif (lesson.way == '必修'):
                print(time[i],'：課程編號：',lesson.number,'(必修)   學分數：',lesson.credit,'   等第：',lesson.grade)
            else:
                print(time[i],'：課程編號：',lesson.number,'(選修)   學分數：',lesson.credit,'   等第：',lesson.grade)                
        print('-----------------------------------以上是你的課程時間表：-----------------------------------\n')
        print('-------------------------------以下是三類加選，你已經放入志願的課------------------------------') 
        exist = False
        for i in range (10):
            if (player.choose[i] == True) and (course_list[40+i].way == '三類加選，概率性成功加簽       '):
                exist = True
                print_course(course_list[40+i],3)
        if (exist == False):
            print('無。')
        print('-------------------------------以上是三類加選，你已經放入志願的課------------------------------')         
        a = input('按enter鍵以繼續。')
        return website(player,course_list,'CS>EE','0')
    elif (a == '5'):
        print('以下是加退選時程。')
        print('第一次加退選：第一週，禮拜一到禮拜二可加退選。(禮拜三進行分發作業，禮拜三下午完公布分發結果)')
        print('第二次加退選：第一週，禮拜四到禮拜五可加退選。(禮拜六進行分發作業，並立即公布分發結果)')
        print('第三次加退選：第二週，禮拜一到禮拜二可加退選。(禮拜三進行分發作業，禮拜三下午完公布分發結果)')
        print('第四次加退選：第二週，禮拜四到禮拜五可加退選。(禮拜六進行分發作業，並立即公布分發結果)')
        a = input('按enter鍵以繼續。')
        return website(player,course_list,'CS>EE','0')
    else:
        return website(player,course_list,'CS>EE','0')

def three(course):
    if (course.way == '一類加選，必定成功加簽         '):
        return True
    expensive = 0
    for i in range (6):
        expensive += value(course.grade[i])
    expensive = 10 * round(expensive,1) + 10 * course.credit
    num = (300 - expensive) // 3
    x = random.randint(0,300)
    if (x <= num):
        return True
    else:
        return False

def prewebsite(players, course_list, t):
    if (t == 19):
        a = 'CS>EE'
        print('加簽流程結束，請在選課系統把你的課表做最後的總整理。')
        while (a != '1'):
            a = 'CSEE'
            players[0] = website(players[0], course_list, 'CS>EE' ,'0')
            while (a not in {'0','1'}):
                a = input('是否確定登出選課系統？是請輸入1，否請輸入0。(登出後，第四次分發完的課表，就是你的最終課表。)')
    done = {5:1,9:2,15:3,19:4}
    if (t in done):
        for i in range (1,5,1):
            for j in range (10):
                when = what_time(course_list[40+j])
                if (better(course_list[40+j],players[i].timetable[when],players[i],3) == 1):
                    players[i].choose[j] = True
                else:
                    players[i].choose[j] = False
        for i in range (5):
            for j in range (10): ## three
                if (players[i].choose[j] == True):
                    if (course_list[40+j].way == '一類加選，必定成功加簽         '):
                        players[i].timetable[what_time(course_list[40+j])] = course_list[40+j]
                    else:
                        if (players[i].bad != '人品差') and (three(course_list[40+j]) == True):
                            players[i].timetable[what_time(course_list[40+j])] = course_list[40+j]
                players[i].choose[j] = False
    if (t in done):
        a = 'CS>EE'
        while (a not in {'0','1'}):
            print ('目前選課系統已經完成第',done[t],'次分發。')
            a = input ('是否進入選課系統查看分發結果？是請輸入1，否請輸入0。\n')
        if (a == '1'):
            print('-------------------------------------------------------------------')
            players[0] = website(players[0], course_list, 'seeonly', '0')
    return

def value(score):
    if (score == 'A+'):
        return 4.3
    if (score == 'A '):
        return 4.0
    if (score == 'A-'):
        return 3.7
    if (score == 'B+'):
        return 3.3
    if (score == 'B '):
        return 3
    if (score == 'B-'):
        return 2.7
    if (score == 'C+'):
        return 2.3
    if (score == 'C '):
        return 2
    if (score == 'C-'):
        return 1.7
    return 0

def final(players):
    print('加退選已經結束。以下是五位玩家的最終課表：')
    players_test(players)
    a = input('接下來你跟這幾位玩家要努力拚你們的GPA了。(輸入enter以繼續)')
    a = input('時間過得很快，期中考考完了。(輸入enter以繼續)')
    a = input('期末考也考完了。(輸入enter以繼續)')
    a = input('老師拖了快一個月終於送出你們的成績了。(輸入enter以繼續)')
    a = input('以下是你們五位這學期的各科成績：(輸入enter以繼續)')
    player_credit = [0,0,0,0,0]
    player_GPA = [0,0,0,0,0]
    player_score = [0,0,0,0,0]
    for i in range (5):
        print('--------------------------------以下是',players[i].name,'的遊戲結果：--------------------------------')
        time = ['禮拜一早上','禮拜一下午','禮拜二早上','禮拜二下午','禮拜三早上','禮拜三下午',
                '禮拜四早上','禮拜四下午','禮拜五早上','禮拜五下午','禮拜六全天']
        for j in range (len(players[i].timetable)):
            lesson = players[i].timetable[j]
            if (lesson == empty):
                print(time[j],'：沒課')
            else:
                mini = 0
                maxi = 5
                if (players[i].good == '好學生'):
                    mini = 2
                if (players[i].bad == '不用功'):
                    maxi = 3
                finalscore = random.randint(mini,maxi)
                finalscore = lesson.grade[finalscore]
                print(time[j],'：   學分數：',lesson.credit,'   等第欄：',lesson.grade,'   最終等第：',finalscore)
                player_credit[i] += lesson.credit
                player_GPA[i] += value(finalscore) * lesson.credit
        player_GPA[i] = round(player_GPA[i] / player_credit[i],4)
        if (player_credit[i] >= 15):
            player_score[i] = 100 * player_GPA[i] + 2 * player_credit[i]
            player_score[i] = round(player_score[i],4)
            print('\n',players[i].name,'的GPA為',player_GPA[i],'，總共修了',player_credit[i],'學分，遊戲總分為'
                  ' 100 *',player_GPA[i],'+ 2 *',player_credit[i],'=',player_score[i],'。')
        else:
            player_score[i] = 0
            print('\n',players[i].name,'的GPA為',player_GPA[i],'，總共修了',player_credit[i],'學分，'
                  '但由於學分數未達15學分的下限，因此遊戲總分為 0 分。')
        print('--------------------------------以上是',players[i].name,'的遊戲結果：--------------------------------')
        a = input ('按enter以繼續。')
    rank = ['第一名','第二名','第三名','第四名','第五名']
    pid = [0,1,2,3,4]
    for i in range (5):
        for j in range (4):
            if (player_score[j] < player_score[j+1]):
                temp = player_score[j]
                player_score[j] = player_score[j+1]
                player_score[j+1] = temp
                temp = pid[j]
                pid[j] = pid[j+1]
                pid[j+1] = temp
    for i in range (5):
        print(rank[i],'：',players[pid[i]].name,'分數：',player_score[i])
    print('遊戲結束，感謝你的遊玩。')
    return

print ('歡迎來到「加簽大地」。如需閱讀規則，請看以下指示。\n')
rule()
good = initialize('good')
bad = initialize('bad')
credit = initialize('credit')
way = initialize('way')
grade = initialize('grade')
(players,course_list) = attribute(good,bad)
course_list = init_course(credit,grade,way)
players_test(players)
for i in range (20):
    players = two(players, course_list, i)
    prewebsite(players, course_list, i)
final(players)
