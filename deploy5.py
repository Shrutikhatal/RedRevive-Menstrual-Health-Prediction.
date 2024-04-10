from flask import Flask , render_template ,jsonify, request , url_for
import pickle

app=Flask(__name__)
#load model
model=pickle.load(open('savemodel5.pkl','rb'))  #pred

@app.route('/')
def home():
    result = ''
    return render_template('index_deploy5.html')

@app.route('/pred', methods=['POST','GET'])
def pred():
    weakness_during_periods =float (request.form['weakness_during_periods '])
    duration=float(request.form['duration'] )
    pain_in_abdomen_Idysmenorrheal = float( request.form['pain_in_abdomen_Idysmenorrheal '])
    mindset =float(request.form['mindset '])
    prediction=int(model.predict([[weakness_during_periods ,duration, pain_in_abdomen_Idysmenorrheal , mindset ]])[0])
    if prediction == 0:
        suggestions = ["Iron-rich foods: Iron is important for maintaining healthy blood cells and can help prevent anemia. Include foods like red meat, chicken, fish, beans, lentils, spinach, and fortified cereals in your diet.\n", "Vitamin B6-rich foods: Vitamin B6 is important for maintaining energy levels and can help alleviate PMS symptoms. Include foods like bananas, chickpeas, salmon, and potatoes in your diet.\n","Magnesium-rich foods: Magnesium can help alleviate muscle cramps and fatigue. Include foods like spinach, almonds, avocados, and dark chocolate in your diet. \n","Fiber-rich foods: Fiber can help regulate digestion and prevent bloating and constipation. Include foods like fruits, vegetables, whole grains, and beans in your diet. \n"]
    elif prediction == 1:
        suggestions = ["Over-the-counter pain relief: Nonsteroidal anti-inflammatory drugs (NSAIDs), such as ibuprofen, can help reduce menstrual cramps and relieve pain.\n", "Dietary changes: Avoiding caffeine, alcohol, and fatty foods can help reduce menstrual pain. Eating a healthy and balanced diet that is rich in fruits, vegetables, and whole grains can also help.\n", "Relaxation techniques: Techniques such as deep breathing, yoga, and meditation can help reduce stress and alleviate menstrual pain.\n"]
    return render_template('results1.html', prediction=prediction, suggestions=suggestions)

if __name__=='__main__':
    app.run(port=3025,debug=True)