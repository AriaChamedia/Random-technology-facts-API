import requests

def generate_fact():
    url="https://uselessfacts.jsph.pl/random.json"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        print(data["text"])
        
        



if __name__ == "__main__":
    print("Welcome to random useless facts genterator!")
    print("Press Enter to generate a new fact and 'q' to quit: ")
    while True:
        choice=input()
        if choice=='q':
            break
        else:
            generate_fact()