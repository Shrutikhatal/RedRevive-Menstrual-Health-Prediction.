from flask import Flask , render_template ,jsonify, request , url_for
import pickle

app=Flask(__name__)
#load model
model=pickle.load(open('savemodel6.pkl','rb')) #pred4

@app.route('/')
def home():
    result = ''
    return render_template('index_deploy6.html')

@app.route('/pred4', methods=['POST','GET'])
def pred4():
    societal_myths =float (request.form['societal_myths '])
    depression_or_anxiety=float(request.form['depression_or_anxiety'] )
    mindset =float(request.form['mindset '] )
    prediction=int(model.predict([[societal_myths ,depression_or_anxiety,mindset ]])[0])
    if prediction == 0:
       
        suggestions = ["Social Myths\n","Menstruating women are impure: In some cultures, menstruation is considered dirty or impure. However, menstruation is a natural bodily function and does not make a woman impure.\n", "Menstruating women should not touch plants: Some cultures believe that menstruating women should not touch plants as it can harm the plants. There is no scientific evidence to support this belief.\n","Menstruating women should not bathe: It is a myth that women should not bathe during menstruation. In fact, maintaining good hygiene during menstruation is important to prevent infections.\n"]
    elif prediction == 1:
        
        suggestions = ["Depression, High Mindset\n","Seek support: Talking to friends or family members about your feelings can help you feel less isolated and may provide you with support and comfort. You can also consider seeing a mental health professional, such as a therapist, who can provide you with additional support and resources.\n", "Exercise regularly: Exercise can help boost your mood by releasing endorphins, which are natural mood boosters. Try to engage in moderate physical activity for at least 30 minutes a day, such as walking, cycling, or swimming.\n","If your depression symptoms persist or worsen, it is important to seek professional help from a qualified mental health provider.\n"]

    return render_template('results5.html', prediction=prediction, suggestions=suggestions)


if __name__=='__main__':
    app.run(port=3030,debug=True)