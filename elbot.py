
class MoviesScraperBot:
    APP_ID = ""
    APP_SECRET = ""
    APP_URI = "https://127.0.0.1:65010/authorize_callback"
    app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
    APP_REFRESH = ""
    user_agent =""
    app_account_code=""
    subreddit = ""
    user_agent = "SimpleMoviesParser (en-us) PyLionz/0.0.2 (Beta)B"
    post_limit = 10



    def login(self):
        import praw
        r = praw.Reddit(self.user_agent)
        r.set_oauth_app_info(self.APP_ID, self.APP_SECRET, self.APP_URI)
        r.refresh_access_information(self.APP_REFRESH)
        return r