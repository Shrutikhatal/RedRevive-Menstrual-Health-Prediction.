from flask import Flask , render_template ,jsonify, request , url_for
import pickle

app=Flask(__name__)
#load model
model=pickle.load(open('savemodel.pkl','rb')) #predict

@app.route('/')
def home():
    result = ''
    return render_template('index_deploy1.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    cramps =float (request.form['cramps'])
    severity_cramps=float(request.form['severity_cramps'] )
    mindset = float( request.form[' mindset'])
    mood=float(request.form[' mood'])
    prediction=int(model.predict([[cramps,severity_cramps, mindset, mood]])[0])
    if prediction == 0:
       
        suggestions = ["severity low, cramps low\n","Stay hydrated: Drinking plenty of water can help reduce bloating and other symptoms of menstruation.", "Exercise: Light to moderate exercise during menstruation can help improve mood and reduce cramps. \n", "Heat therapy: Using a heating pad or taking a warm bath can help alleviate mild cramps and promote relaxation.\n","Rest and relaxation: Getting plenty of rest and relaxation during your period can help reduce stress and improve overall well-being.\n"]
    elif prediction == 1:
        
        suggestions = ["Cramps high, severity high, mood high\n","Pain relief: Over-the-counter pain relievers such as ibuprofen or naproxen can help reduce cramps and menstrual pain. If you prefer a natural remedy, heat therapy like a heating pad or warm bath can also provide relief.\n", " Exercise: Regular exercise, especially low-impact activities like yoga or swimming, can help reduce cramps and improve mood.\n", "Supplements: Some women find relief from menstrual symptoms by taking supplements like magnesium or vitamin B6.\n","Birth control: Hormonal birth control methods like the pill, patch, or IUD can help regulate periods and reduce cramps.\n"]
    # else:
    #     suggestions = ["Suggestion 1 for 2", "Suggestion 2 for 2", "Suggestion 3 for 2"]
    return render_template('results1.html', prediction=prediction, suggestions=suggestions)


if __name__=='__main__':
    app.run(port=3005,debug=True)