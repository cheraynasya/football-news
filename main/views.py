from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406437571',
        'name': 'Cheryl Raynasya Adenan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)