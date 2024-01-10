from django.shortcuts import render

# Create your views here.
def index(request):
    blogs = [
        {
            'title': 'The Benefits of Morning Walks',
            'content': 'In the hustle and bustle of modern life, taking a moment for ourselves is crucial. One simple and effective way to do this is by incorporating a morning walk into your routine. Not only does it provide a refreshing start to the day, but it also boosts mood, improves cardiovascular health, and enhances creativity. So, set your alarm a bit earlier, lace up those sneakers, and step into a healthier, happier day!',
            'author': 'Joe'
        },
        {
            'title': 'The Magic of Mindful Breathing',
            'content': 'In a world filled with constant stimuli, finding moments of tranquility can be challenging. Enter mindful breathing—a practice that requires nothing but your attention. By focusing on each breath, you can alleviate stress, improve concentration, and foster a sense of inner peace. Whether it is a quick break at work or a few minutes before bedtime, mindful breathing is a simple yet powerful tool to bring calmness into your daily life.',
            'author': 'Greg'
        },
        {
            'title': 'Rediscovering the Joy of Reading',
            'content': 'In the age of digital distractions, there is something enchanting about turning the pages of a good book. Reading not only offers an escape from reality but also stimulates the imagination and broadens perspectives. Whether it is fiction, non-fiction, or poetry, the world of literature is a treasure trove waiting to be explored. So, dust off that bookshelf, pick up a novel, and rediscover the joy that comes with getting lost in a good story.',
            'author': 'Lily'
        }
    ]
    return render(request, 'simpleblog/index.html', {'blogs': blogs})