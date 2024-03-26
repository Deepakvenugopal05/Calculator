from django.shortcuts import render


def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        if 'number' in request.POST:
            expression += request.POST['number']
        elif 'operator' in request.POST:
            expression += request.POST['operator']
        elif 'decimal' in request.POST:
            expression += request.POST['decimal']
        elif 'calculate' in request.POST:
            try:
                result = eval(expression)
                expression = result
            except Exception as e:
                expression = 'Error'
        elif 'clear' in request.POST:
            expression = ''
    else:
        expression = ''

    return render(request, 'calculate.html', {'expression': expression})
