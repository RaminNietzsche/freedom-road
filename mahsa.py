from instagrapi import Client

ACCOUNT_USERNAME = "USER_NAME"
ACCOUNT_PASSWORD = "PASSWORD"

MAX_MSG = 100
MAX_LIKE = 100
BIO = "Freedom in Jail"
MAKE_IT_PRIVATE = True

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

# Delete Directs
for direct in cl.direct_threads(MAX_MSG):
    cl.direct_thread_hide(direct.id)

# Make Account Private
if MAKE_IT_PRIVATE:
    cl.account_set_private()

# Change Account BIO
cl.account_set_biography(BIO)

# Account Name
for like in cl.liked_medias(amount=MAX_LIKE):
    cl.media_unlike(like.id)