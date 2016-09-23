from datetime import datetime
import psycopg2
import re
from elbot import MoviesScraperBot
db_host ="ec2-107-22-250-212.compute-1.amazonaws.com"
db_db = "d3aq122buq7e8u"
db_user ="zxboeoclsugjdi"
db_pass = "X-YpaJ4j4Cm_At0zPwYrGhemkl"
coni = psycopg2.connect("dbname='"+db_db+"' user='"+db_user+"' host='"+db_host+"' password='"+db_pass+"'")
print "Setting up everything..."
years=[]
xs=False
LASTPOST = datetime.now()
lastTime=datetime.now()
for y in range(1900,datetime.today().year+6):
    years.append(y)


mv=MoviesScraperBot()
r=mv.login()
posts=r.get_subreddit(mv.subreddit)#praw.Reddit(user_agent).get_subreddit(subreddit)









def isDone(id):
    c=coni.cursor()
    c.execute('SELECT count(id) FROM history WHERE id = \'{id}\''.format(id=id))
    if c.fetchall()[0][0] > 0:
        return True
    else:
        return False

def setDone(id):
    try:
        c = coni.cursor()
        c.execute('INSERT INTO history VALUES (\'{v}\')'.format(v=id))
        coni.commit()
    except:
        print "Error when setting "+str(id)+" done."




def getTitle(text):
    text=text.lower()
    text = text.replace('.', ' ')
    title=""
    year=""
    type="" #0=movie, 1 = tv show FROM Post title tag
    t=re.findall(r'\d+',text)
    for tt in t:
        if len(tt)==4 and isYear(tt):
            year=tt
            break
    if text.__contains__('[movie]'):
        type=0
    elif text.__contains__('[tv]'):
        type=1
    try:
        t1=""
        t2=""
        if type==0:
            t1='[movie]'
        elif type==1:
            t2='[tv]'
        if text.__contains__('('+year+')'):
            t2='('+year+')'
        elif text.__contains__('['+year+']'):
            t2='['+year+']'
        else:
            if len(year)>0:
                t2=year


        start = text.rindex(t1) + len(t1)
        end = text.rindex(t2, start)
        text=text[start:end]
        text=re.sub(' +',' ',text)
        if text[-1:]==' ':
            text = text[:(len(text) - 1)]
        if text[:1] == ' ':
            text = text[1:]







        return [text, year]
    except ValueError:
        return []


    return year

def isYear(y):

    for i in years:

        if i == int(y):

            return True


    return False

def time_ag(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"

class movie:
    Title=""
    Year=""
    Rated=""
    Released=""
    Runtime=""
    Genre=""
    Director=""
    Writer=""
    Actors=""
    Plot=""
    Language=""
    Country=""
    Awards=""
    Poster=""
    Metascore=""
    imdbRating=""
    imdbVotes=""
    imdbID=""
    Type=""
    Response=""
    json=[]
    formated_reply=""
    

    def __init__(self, title, year):

        import urllib, json
        url = "http://www.omdbapi.com/?t="+title+"&y="+year+"&plot=short&r=json"

        response = urllib.urlopen(url)
        data = json.loads(response.read())
        self.json=data
        self.formated_reply="**["+data["Title"]+"](http://www.imdb.com/title/"+data["imdbID"]+") ("+data["Year"]+")**\n\n" \
"^"+data["Year"]+" ^~ ^"+data["Genre"].replace(' ', ' ^')+" ^~ ^"+data["Runtime"].replace(' ', ' ^')+"\n\n" \
"> "+data["Plot"]+"\n\n" \
". | _ \n" \
":--------|:--------:\n" \
"imdb Rating | **"+data["imdbRating"]+"** ^(from "+data["imdbVotes"]+" user)\n" \
"Release date | "+data["Released"]+"\n" \
"Rated | "+data["Rated"]+"\n" \
"Director| "+data["Director"]+"\n" \
"Writer| "+data["Writer"]+"\n" \
"Actors | "+data["Actors"]+"\n" \
"Awards | "+data["Awards"]+"\n" \
"___________\n" \
"^this ^is ^a ^simple ^movie ^scraper ^bot, ^please ^downvote ^this ^comment ^if ^you ^find ^it ^inaccurate."











