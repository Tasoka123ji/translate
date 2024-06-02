# from googletrans import Translator
# import time
# translator = Translator()
# with open('main.txt', 'r', encoding='utf-8') as file:
#     text_to_translate = file.read()
#     text = text_to_translate.split('\n')
#     # for i in text:
#     #     translated = translator.translate(i, dest='hy')
#     #     time.sleep(0.1)
#     #     print(f"Original: {i}")
#     #     print(f"Translated: {translated.text}")
#     #     print(i)

# with open('tetr.txt','a') as file:
#     j = 0
#     for i in text:
#         translated = translator.translate(i, dest='hy')
#         time.sleep(0.1)
#         trans = str(j) + ' ' + i + ' - ' + translated.text + '\n'
#         file.write(trans)
#         j += 1
#         print(j)
        
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    words = []
    i = 0
    with open('tetr.txt', 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(' - ')
            i+=1
            if len(parts) == 2:
                word_info = parts[0].split(' ')
                word_number = i
                english_word = ' '.join(word_info[1:])
                armenian_word = parts[1]
                words.append((word_number, english_word, armenian_word))
                print(word_number,english_word,armenian_word)
    return render_template('index.html', words=words)

if __name__ == '__main__':
    app.run(debug=True)
