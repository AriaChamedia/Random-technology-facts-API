import requests

def generate_fact():
    url="https://opentdb.com/api.php?amount=10&category=17"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        score=0
        for i, q in enumerate(data["results"]):
            print(f"Q{i+1}: {q["question"]}")
            options=q["incorrect_answers"] + [q["correct_answer"]]
            options=sorted(options)
            for j,opt in enumerate(options):
                print(f" {j+1}- {opt}")
            answer=int(input("Enter your answer in the range given: "))
            try:
                if options[answer-1]==q["correct_answer"]:
                    print("Correct")
                    score=score+1
                else:
                    print(f"Wrong! The correct answer is: {q['correct_answer']}") 
            except(IndexError, ValueError):
                print("Invalid input")    
                    
                           
        
        
        



if __name__ == "__main__":
    print("Welcome to random useless facts genterator!")
    print("Press Enter to generate a new fact and 'q' to quit: ")
    while True:
        choice=input()
        if choice=='q':
            break
        else:
            generate_fact()