from django.contrib.gis.feeds import Feed
from django.core.paginator import Paginator
from django.shortcuts import render

from zhigeng_Blog.follow.models import Follow


def follow(from_user, to_user):
    Follow(follower=from_user,
           followed=to_user).save()


def unfollow(from_user, to_user):
    f = Follow.objects.filter(follower=from_user, followed=to_user).all()
    if f:
        f.delete()  # 取关


def user_followed(from_user):
    followeders = Follow.objects.filter(follower=from_user).all()
    user_followed = []
    for followeder in followeders:
        user_followed.append(followeder.followed)
    return user_followed


def FEEDS_NUM_PATES(args):
    pass


def followed(request):
    user = request.user
    all_feeds = Feed.get_feeds().filter(user__in=Follow.user_followed(user))
    paginator = Paginator(all_feeds, FEEDS_NUM_PATES)
    feeds = paginator.page(1)
    from_feed = -1
    if feeds:
        from_feed = feeds[0].id
    return render(request, 'mypoint.html', {
        'feeds': feeds,
        'from_feed': from_feed,
        'page': 1,
    })

