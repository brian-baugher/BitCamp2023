from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserFriends
from to_do_list_app.models import Task

# Create your views here.

users = [     # database
    {
        'id' : '1',
        'first_name': 'Tony',
        'last_name' : 'Matar',
        'status' : 'Working',
        'progress' : '50',
    },
    {
        'id' : '2',
        'first_name': 'Your',
        'last_name' : 'Mom',
        'status' : 'Chillin',
        'progress' : '30',
    },
    {
        'id' : '3',
        'first_name': 'Brian',
        'last_name' : 'Baugher',
        'status' : 'On His Grind',
        'progress' : '25',
    }
]

tasks = [
    {
        'id' : 'a',
        'title': 'task1',
        'description': 'testing data',
        'complete': True,
        'user_id': '1',

    },
    {
        'id' : 'b',
        'title': 'task2',
        'description': 'testing data',
        'complete': True,
        'user_id': '1',

    },
    {
        'id' : 'c',
        'title': 'task3',
        'description': 'testing data',
        'complete': False,
        'user_id': '1',

    },
    {
        'id' : 'd',
        'title': 'task4',
        'description': 'testing data',
        'complete': False,
        'user_id': '1',

    },
    {
        'id' : 'e',
        'title': 'task5',
        'description': 'testing data',
        'complete': True,
        'user_id': '2',

    },
    {
        'id' : 'f',
        'title': 'task6',
        'description': 'testing data',
        'complete': False,
        'user_id': '2',

    },
    {
        'id' : 'g',
        'title': 'task7',
        'description': 'testing data',
        'complete': False,
        'user_id': '2',

    },
    {
        'id' : 'h',
        'title': 'task8',
        'description': 'testing data',
        'complete': False,
        'user_id': '2',

    },
    {
        'id' : 'i',
        'title': 'task9',
        'description': 'testing data',
        'complete': True,
        'user_id': '3',

    },
    {
        'id' : 'j',
        'title': 'task10',
        'description': 'testing data',
        'complete': True,
        'user_id': '3',

    },
    {
        'id' : 'k',
        'title': 'task11',
        'description': 'testing data',
        'complete': True,
        'user_id': '3',

    },
    {
        'id' : 'l',
        'title': 'task12',
        'description': 'testing data',
        'complete': True,
        'user_id': '3',

    },

]

user_friends = [
    {
        'user_id' : '1',
        'friend_id' : '2',
    },
    {
        'user_id' :'1' ,
        'friend_id' :'3',
    },
    {
        'user_id' : '2',
        'friend_id' :'3',
    }


]


friends = [[] for k in range(len(users))]
for user in range(len(users)):      # this is just a query normally
    for friend in user_friends:
        if friend['user_id'] == users[user]['id']:
            friends[user].append(friend['friend_id'])

progs = [{'name':'one', 'progress' : '20'},{'name':'two', 'progress' : '50'},{'name':'three', 'progress' : '10'}]
names = []
for i in range(3):
    names.append((progs[i]['name'], progs[i]['progress']))

class FriendAdd(CreateView):
    model = UserFriends
    fields = ['friend', 'user']
    success_url = reverse_lazy('friends')

def friends_list_view(request):
    curr_id = request.user.id
    model = UserFriends
    taskModel = Task

    friendos = list(model.objects.filter(user=curr_id).values())
    #print(friendos)
    friend2 = []
    for x in friendos:
        friend2.append(x['friend'])
    taskos = list(taskModel.objects.filter(user_id__in=friend2).values())
    usys = list(User.objects.filter(id__in=friend2).values())
    #print(usys)

    ratios = {}
    for usy in usys:
        num_complete = 0
        new_taskos = list(taskModel.objects.filter(user_id=usy['id']).values())
        num_tasks = len(new_taskos)
        for task in new_taskos:
            if task['complete']:
                num_complete += 1
            ratio = int((float(num_complete)/float(num_tasks)) * 100)
            ratios[task['user_id']] = ratio


    list2 = []
    for g in range(len(ratios)):
        list1 = {}
        list1['username'] = usys[g]['username']
        list1['ratio'] = ratios[usys[g]['id']]
        list2.append(list1)
        #list1.append((usys[g], ratios[usys[g]['id']]))
    #print(list2)





    #print(taskos)
    list2 = sorted(list2, key= lambda x:x['ratio'], reverse=True)
    context = {
        'friends' : list2,
    }
    # print(request.headers)
    return render(request, "friend.html", context)
