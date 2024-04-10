from flask import Flask , render_template ,jsonify, request , url_for
import pickle

app=Flask(__name__)
#load model
model=pickle.load(open('savemodel3.pkl','rb')) #pred2

@app.route('/')
def home():
    result = ''
    return render_template('index_deploy3.html')

@app.route('/pred2', methods=['POST','GET'])
def pred2():
    cycle_track=float (request.form['cycle_track'])
    management_of_menstrual_cycle=float(request.form['management_of_menstrual_cycle'] )
    prediction=int(model.predict([[cycle_track,management_of_menstrual_cycle]])[0])
    if prediction == 0:
       
        suggestions = ["Not tracked\n","Calendar method: Use a paper calendar or a digital calendar app to mark the start and end dates of your period. This will help you see how long your menstrual cycle is and predict when your next period may start. \n", "Period tracking apps: There are many period tracking apps available for download on smartphones. These apps allow you to enter the start and end dates of your period, track symptoms, and receive reminders for when your next period may start. \n","Basal body temperature method: This method involves taking your temperature every morning before getting out of bed. Your temperature will rise slightly after ovulation, which can help you predict when your next period will start.\n"]
    elif prediction == 1:
        
        suggestions = ["Tracked but for management.\n","Be prepared: Make sure you have an adequate supply of menstrual products, such as pads, tampons, menstrual cups. Keep some supplies in your purse or bag so you're prepared when your period starts unexpectedly. \n", "Manage symptoms: There are several symptoms that can come with your period, such as cramps, bloating, and fatigue. You can manage these symptoms by using over-the-counter pain relievers, applying heat to the affected area, and getting plenty of rest. \n","Practice good hygiene: Change your menstrual product regularly and practice good hygiene to avoid infections. Make sure to wash your hands before and after changing your menstrual product.\n"]

    return render_template('results3.html', prediction=prediction, suggestions=suggestions)

if __name__=='__main__':
    app.run(port=3015,debug=True)