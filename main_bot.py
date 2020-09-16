from instapy import InstaPy
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browser = r'C:\Program Files\Mozilla Firefox\firefox.exe'

try:
    session = InstaPy(username="jutahx", password="Stanley1322", browser_executable_path=browser)

    session.login()
except ValueError:

    print(ValueError)

session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                              peak_likes_daily=585,
                               peak_comments_hourly=21,
                               peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)


session.like_by_tags(["OnlineLearning", "Programming", "datascience", "python"])
#session.dont_like(["naked", "nsfw"])
session.set_do_follow(enabled=True, percentage=3)
session.set_do_comment(enabled=True, percentage=3)
session.set_comments(["Nice!", "Awesome!", "WOW :😎😎😎:"])
session.end()