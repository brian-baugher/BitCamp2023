from django.shortcuts import render

# Create your views here.


def friends_list_view(request):
    # print(request.headers)
    return render(request, "friend.html", {})
