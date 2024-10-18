from django.shortcuts import render
from .fibo import fibonacci

def fibonacci_view(request):
    result = None  # Default to no result
    error = None   # Default to no error message

    if request.method == 'POST':
        number = request.POST.get('number')

        try:
            n = int(number)
            result = fibonacci(n)
        except ValueError:
            error = "Please enter a valid integer."

    return render(request, 'fibonacci_app/fibonacci.html', {'result': result, 'error': error})