from django.shortcuts import render

# Create your views here.

friends = [     # database
    {
        'name': 'Tony Matar',
        'status' : 'Working',
        'progress' : '50',
    },
    {
        'name': 'Aarya Dubhashi',
        'status' : 'Chillin',
        'progress' : '25',
    },
    {
        'name': 'Brian',
        'status': 'on his grind',
        'progress': '10'
    }
]

progs = sorted(friends, key=lambda x:x['progress'], reverse=True)
names = []
for i in range(3):
    names.append((progs[i]['name'], progs[i]['progress']))


def friends_list_view(request):
    context = {
        'friends' : friends,
        'names' : names
    }
    # print(request.headers)
    return render(request, "friend.html", context)
