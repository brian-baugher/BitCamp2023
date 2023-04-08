from django.shortcuts import render

# Create your views here.

friends = [     # database
    {
        'name': 'Tony Matar',
        'status' : 'Working',
        'progress' : '50%',
    },
    {
        'name': 'Aarya Dubhashi',
        'status' : 'Chillin',
        'progress' : '25%',
    },
    {
        'name': 'Brian',
        'status': 'on his grind',
        'progress': '10%'
    }
]


def friends_list_view(request):
    context = {
        'friends' : friends
    }
    # print(request.headers)
    return render(request, "friend.html", context)
