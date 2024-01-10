from django.shortcuts import render

# Create your views here.
def add_view(request, first_num, second_num):
    answer = [first_num + second_num, f'{first_num} + {second_num} =']
    return render(request, 'calculator/index.html', {'answer':answer})

def subtract_view(request, first_num, second_num):
    answer = [first_num - second_num, f'{first_num} - {second_num} =']
    return render(request, 'calculator/index.html', {'answer':answer})

def divide_view(request, first_num, second_num):
    answer = [first_num / second_num, f'{first_num} / {second_num} =']
    return render(request, 'calculator/index.html', {'answer':answer})

def multiply_view(request, first_num, second_num):
    answer = [first_num * second_num, f'{first_num} * {second_num} =']
    return render(request, 'calculator/index.html', {'answer':answer})