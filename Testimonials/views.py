from django.shortcuts import render

# Create your views here.
def testimonials(request):
    context = {
    }
    return render(request, "testimonials.html", context)