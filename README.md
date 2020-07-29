def user_stats(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    most_predicted=File.objects.filter(userNamef=username).annotate(mc=Count('prediction')).order_by('-mc')[0].mc
    num_search=File.objects.filter(userNamef=username).count()
    correct=num_search.objects.filter(isCorrect=True)
    context = {
        "most_predicted": most_predicted,
        "num_search": num_search,
        "correct": correct
    }
    return render(request, 'eve/index.html', context)
