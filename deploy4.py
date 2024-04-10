from flask import Flask , render_template ,jsonify, request , url_for
import pickle

app=Flask(__name__)
#load model
model=pickle.load(open('savemodel4.pkl','rb')) #pred3

@app.route('/')
def home():
    result = ''
    return render_template('index_deploy4.html')

@app.route('/pred3', methods=['POST','GET'])
def pred3():
    depression_or_anxiety=float (request.form['depression_or_anxiety'])
    mindset =float(request.form[' mindset'] )
    mood=float(request.form[' mood'])
    feelings= float( request.form['feelings'])
   
    prediction=int(model.predict([[depression_or_anxiety,mindset , mood, feelings]])[0])
    if prediction == 0:
       
        suggestions = ["Depressed, high mindset, low feelings.\n","Seek support: Talking to someone you trust, like a friend, family member, or healthcare provider, can help you feel supported and understood.\n", "Self-care: Take some time for yourself to do something you enjoy, whether it's reading a book, taking a warm bath, or watching a movie. This can help you feel more relaxed and improve your mood.\n","Mindfulness: Mindfulness meditation and deep breathing exercises can help you manage stress and improve your overall mood.\n"]
    elif prediction == 1:
        
        suggestions = ["Moderate depression, moderate mindset\n","Good, take self care and consult an expert if you feel too depressed. Talk to your parents and close friends. \n"]
    elif prediction == 2:
        suggestions = ["High Feelings, low depression, low mindset\n","Focus on self-compassion: Be kind to yourself and practice self-compassion. Treat yourself with the same kindness and understanding that you would offer to a close friend. \n", "Connect with others: Talk to someone you trust, like a friend or family member, about how you're feeling. Feeling connected to others can help improve your mood. \n", "Prioritize sleep: Getting enough sleep is important for both physical and mental health. Aim for at least 7-8 hours of sleep per night.\n"]
    return render_template('results4.html', prediction=prediction, suggestions=suggestions)

if __name__=='__main__':
    app.run(port=3020,debug=True)