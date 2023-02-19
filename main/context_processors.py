

def searchFunction(request):
    context = {}
    if "search" in request.GET:
        query = request.GET.get("q")
        print("\n\n\n"+query)

    return context
