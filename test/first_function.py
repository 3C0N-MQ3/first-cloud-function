import requests

def main():
    r = requests.post('http://localhost:8080/', data='123456789')
    result = r.json()
    
    print(result)
    
if __name__ == '__main__':
    main()