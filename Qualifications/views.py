from django.shortcuts import render

# Create your views here.
def qualifications(request):
    context = {
    }
    return render(request, "Qualifications.html", context)