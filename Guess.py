
m word import Word

class Guess:
    def __init__(self, word):
        self.numTries = 0 # 실패한회수초기화
        self.guesses = [] # 사용한 글자 초기화
        self.guesses.append(guessedChars) # 사용한글자의집합에원소로추가.
        self.collectAnswer = '_'*len(word) # 현재까지맞춘글자상태초기화
        pass

    def display(self):
        print('Current :', collectAnswer)
        print('Tries:', numtries)
        pass
#현재까지맞춘글자상태,실패한회수정보를출력.

    def guess(self, character):
        Finished = False #위에서갱신한데이터가모든위치의글자를알아낸경우는True 아니면False 리턴
        while not Finished:
            for i in range(len(word)):
                if guessedChars[i] in word: #비밀단어안에있으면그위치를기록(현재까지맞춘글자)
                    collectAnswer = collectAnswer[:i] + guessedChar[i] + collectAnswer[i+1:]
                if guessedChars[i] not in word: #비밀단어안에없으면실패회수증가.
                    numTries += 1
            if collectAnswer == word:
                Finished = True
            if numTries == 6:
                Finished = True            
        pass









