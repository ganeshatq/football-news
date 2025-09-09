from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406425640',
        'name': 'Ganesha Taqwa',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
