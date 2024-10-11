import qrcode
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# List of questions and answers
questions = [
    {
        "question": "Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?",
        "options": ["Solicitor General", "Attorney General", "Cabinet Secretary", "Chief Justice"],
        "correct_answer": "Attorney General"
    },
    {
        "question": "Who, in 1978, became the first person to be born in the continent of Antarctica?",
        "options": ["Emilio Palma", "James Weddell", "Nathaniel Palmer", "Charles Wilkes"],
        "correct_answer": "Emilio Palma"
    },
    {
        "question": "Who is the first woman to successfully climb K2, the world’s second highest mountain peak?",
        "options": ["Junko Tabei", "Wanda Rutkiewicz", "Tamae Watanabe", "Chantal Mauduit"],
        "correct_answer": "Wanda Rutkiewicz"
    },
    {
        "question": "Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the ‘Dastan-e-Ghadar’, a personal account of the 1857 revolt?",
        "options": ["Mir Taqi Mir", "Mohammad Ibrahim Zauq", "Zahir Dehlvi", "Abul-Qasim Ferdowsi"],
        "correct_answer": "Zahir Dehlvi"
    }
]

@app.route('/generate_qr')
def generate_qr():
    qr_data = url_for('show_questions', _external=True)  # Ensure this points to the correct endpoint
    img = qrcode.make(qr_data)
    img.save('static/images/qr_code.png')
    return render_template('index.html', qr_code='static/images/qr_code.png')

@app.route('/questions', methods=['GET', 'POST'])
def show_questions():  # Ensure this function name is consistent with URL generation
    if request.method == 'POST':
        user_answers = request.form.to_dict()
        score = sum(1 for i, q in enumerate(questions) if user_answers.get(f"question{i}") == q['correct_answer'])
        return redirect(url_for('result', score=score))

    return render_template('questions.html', questions=questions, range=range(len(questions)))  # Pass the range for enumeration

@app.route('/result/<int:score>', methods=['GET', 'POST'])
def result(score):
    total_questions = len(questions)
    if score == total_questions:
        result_message = f"Congratulations! You answered all {total_questions} questions correctly!"
    else:
        result_message = f"You scored {score} out of {total_questions}. Better luck next time!"
    
    return render_template('result.html', result_message=result_message)

if __name__ == '__main__':
    app.run(debug=True)
