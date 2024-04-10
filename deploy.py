from flask import Flask , render_template ,jsonify, request , url_for
import pickle

app=Flask(__name__)
#load model
# model=pickle.load(open('savemodel.pkl','rb')) #predict
# model=pickle.load(open('savemodel1.pkl','rb'))  #pred1
# model=pickle.load(open('savemodel3.pkl','rb')) #pred2
# model=pickle.load(open('savemodel4.pkl','rb')) #pred3
# model=pickle.load(open('savemodel5.pkl','rb'))  #pred
model=pickle.load(open('savemodel6.pkl','rb')) #pred4

@app.route('/')
def home():
    result = ''
    return render_template('index_deploy.html')






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
    return render_template('results.html', prediction=prediction, suggestions=suggestions)






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
    app.run(port=3000,debug=True)
    # if __name__=='__main__':
    #      app.run(debug=True)
