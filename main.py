import flask
import json
import re
import functions_framework

@functions_framework.http
def first_cloud_function(request: flask.Request) -> flask.typing.ResponseReturnValue:
    """
    Handles HTTP requests and performs different actions based on the request method.
    
    Args:
        request (flask.Request): The HTTP request object.
        
    Returns:
        flask.typing.ResponseReturnValue: A tuple containing the response message and status code.
        
    - If the request method is 'GET', returns a 501 status code indicating the feature is not implemented yet.
    - If the request method is 'POST', processes the request data to sum numbers and returns the result as a JSON string.
    - If the request method is neither 'GET' nor 'POST', returns a 405 status code indicating the method is unsupported.
    """
    if request.method == 'GET':
        return 'Not implemented yet. Check later...', 501
    elif request.method == 'POST':
        return sum_numbers(request.data.decode("utf-8"))
    else:
        return 'Unsupported method.', 405
    
def sum_numbers(data: str) -> str:
    """
    Sums all the numeric digits found in the input string.
    
    Args:
        data (str): The input string containing numeric digits.
        
    Returns:
        str: A JSON string containing the concatenated numbers and their sum.
        
    Raises:
        AssertionError: If the input data is not a string.
        
    - Extracts all numeric digits from the input string.
    - If no digits are found, returns a message indicating no numbers were received.
    - Calculates the sum of the extracted digits and returns a JSON string with the original digits and their sum.
    """
    assert isinstance(data, str), 'Data must be a string.'
    
    numbers = ''.join(re.findall(r'\d+', data))
    if numbers == '':
        return 'No numbers received. Testing new build...'
    
    result = sum([int(x) for x in numbers])
    
    return json.dumps({'numbers': numbers, 'sum': result})
