import functions_framework

@functions_framework.http
def example_get_post(request):
    # Procesa la solicitud HTTP
    if request.method == 'GET':
        return f
    elif request.method == 'POST':
        data = request.get_json()
        return f'Received data: {data}'
    else:
        return 'Unsupported method', 405
