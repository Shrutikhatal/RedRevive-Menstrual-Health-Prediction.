from flask import Flask , render_template ,jsonify, request , url_for
import pickle

app=Flask(__name__)
#load model
model=pickle.load(open('savemodel1.pkl','rb'))  #pred1

@app.route('/')
def home():
    result = ''
    return render_template('index_deploy2.html')

@app.route('/pred1', methods=['POST','GET'])
def pred1():
    management_of_menstrual_cycle=float (request.form['management_of_menstrual_cycle'])
    menstrual_product= float( request.form['menstrual_product'])
    area =float(request.form['area '])
    mindset =float(request.form['mindset '] )
    consulted =float(request.form['consulted '] )
    
    prediction=int(model.predict([[management_of_menstrual_cycle, menstrual_product, area ,mindset ,consulted  ]])[0])
    if prediction == 0:
        suggestions = ["High mindset, not consulted need to use proper products.\n","Keep track of your menstrual cycle: Keep a calendar or use an app to keep track of your menstrual cycle. Knowing when to expect your period can help you prepare and manage any symptoms.\n", "You can also use telemedicine platforms like Teladoc or Amwell to find a healthcare provider who can offer online consultations. It's important to do your research and choose a reputable healthcare provider who is licensed and experienced in menstrual management.\n"]
    elif prediction == 1:
        suggestions = [" Low mindset, Rural area.\n","Practice self-care: Take some time for yourself to do something you enjoy, whether it's reading a book, taking a warm bath, or watching a movie. This can help you feel more relaxed and improve your mood. \n", "Get enough sleep: Make sure you're getting enough restful sleep, as lack of sleep can make mood swings worse.\n"]
    return render_template('results2.html', prediction=prediction, suggestions=suggestions)

if __name__=='__main__':
    app.run(port=3010,debug=True)