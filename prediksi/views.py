from django.shortcuts import render
from django.http import HttpResponse

def categorize_bmi(bmi):
    if bmi < 16:
        return 'XXS'
    elif 16 <= bmi < 18.5:
        return 'S'
    elif 18.5 <= bmi < 24.9:
        return 'M'
    elif 25 <= bmi < 29.9:
        return 'L'
    elif 30 <= bmi < 34.9:
        return 'XL'
    elif 35 <= bmi < 39.9:
        return 'XXL'
    else:
        return 'XXXL'

def size_predictor(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        height = int(request.POST.get('height'))
        weight = int(request.POST.get('weight'))
        bmi = weight / ((height / 100) ** 2)
        bmi_category = categorize_bmi(bmi)
        return HttpResponse(f"Ukuran baju yang cocok adalah: {bmi_category}")

    return render(request, 'size_predictor.html')
