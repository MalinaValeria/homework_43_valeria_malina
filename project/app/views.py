from django.shortcuts import render


def index_view(request):
    context = None
    symbol = None
    result = None
    if request.method == 'POST':
        data = request.POST
        first_number = int(data.get('first_number'))
        second_number = int(data.get('second_number'))
        match data.get('gridRadios'):
            case 'add':
                symbol = '+'
                result = first_number + second_number
            case 'subtract':
                symbol = '-'
                result = first_number - second_number
            case 'multiply':
                symbol = '*'
                result = first_number * second_number
            case 'divide':
                symbol = '/'
                result = first_number / second_number
        context = {
            'first': first_number,
            'second': second_number,
            'symbol': symbol,
            'result': result
        }
    return render(request, 'index.html', context=context)
