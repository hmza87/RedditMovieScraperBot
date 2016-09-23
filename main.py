from decorator import getfullargspec

from hz import *
import sys, time, praw
from datetime import datetime



def work():
    for post in posts.get_new(limit=mv.post_limit):
        if post.title.lower().__contains__('[movie]') and not isDone(post.id) :
            try:

                print('From work() -> Working with : ' + post.id)
                m= movie(getTitle(post.title)[0], getTitle(post.title)[1])
                print "------- " + post.title
                print "------- " +m.json['Title'] + " ("+m.json["Year"]+")"
                print "------- https://www.reddit.com/r/megalinks/comments/"+post.id
                print "------- Commenting.."
                #print m.formated_reply
                try:

                    post.add_comment(m.formated_reply)
                    print "------- Comment added."
                    setDone(post.id)
                    print "------- Finished with "+post.id

                    cc = coni.cursor()
                    cc.execute("SELECT count(*) FROM history")
                    d = cc.fetchall()[0][0]
                    print '#History size=\'{v}\' \n'.format(v=d)
                    LASTPOST = datetime.now()
                    return

                except praw.errors.RateLimitExceeded as er:
                    e = er.sleep_time
                    now = datetime.datetime.now()
                    whn = now + datetime.timedelta(seconds=e)
                    print "Sleeping for " + str(e) +" as requested from RateLimit..\nWill Continue at "+str(whn)
                    time.sleep(e)
            except:
                setDone(post.id)
                print sys.exc_info()














def slp(mins):
    cc = coni.cursor()
    cc.execute("SELECT count(*) FROM history")
    d = cc.fetchall()[0][0]
    print "last comment posted "+time_ag(LASTPOST)+" | History size "+str(d)
    time.sleep(mins*60)




while True:
    try:
        work()
    except:
        print sys.exc_info()

    slp(2)




