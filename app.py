from flask import Flask,render_template,request
import pickle

app=Flask(__name__)




@app.route("/")
def home():
 return render_template("index.html")




@app.route('/result', methods=['POST'])
def result():
    ext1 = request.form['ext1']
    ext2 = request.form['ext2']
    ext3 = request.form['ext3']
    ext4 = request.form['ext4']
    ext5 = request.form['ext5']
    ext6 = request.form['ext6']
    ext7 = request.form['ext7']
    ext8 = request.form['ext8']
    ext9 = request.form['ext9']
    ext10 = request.form['ext10']


    est1=request.form['est1']
    est2=request.form['est2']
    est3=request.form['est3']
    est4=request.form['est4']
    est5=request.form['est5']
    est6=request.form['est6']
    est7=request.form['est7']
    est8=request.form['est8']
    est9=request.form['est9']
    est10=request.form['est10']


    agr1=request.form['agr1']
    agr2=request.form['agr2']
    agr3=request.form['agr3']
    agr4=request.form['agr4']
    agr5=request.form['agr5']
    agr6=request.form['agr6']
    agr7=request.form['agr7']
    agr8=request.form['agr8']
    agr9=request.form['agr9']
    agr10=request.form['agr10']


    csn1=request.form['csn1']
    csn2=request.form['csn2']
    csn3=request.form['csn3']
    csn4=request.form['csn4']
    csn5=request.form['csn5']
    csn6=request.form['csn6']
    csn7=request.form['csn7']
    csn8=request.form['csn8']
    csn9=request.form['csn9']
    csn10=request.form['csn10']

    opn1=request.form['opn1']
    opn2=request.form['opn2']
    opn3=request.form['opn3']
    opn4=request.form['opn4']
    opn5=request.form['opn5']
    opn6=request.form['opn6']
    opn7=request.form['opn7']
    opn8=request.form['opn8']
    opn9=request.form['opn9']
    opn10=request.form['opn10']
    with open("model.pkl", "rb") as f:
      model = pickle.load(f)
    y=[[ext1,ext2,ext3,ext4,ext5,ext6,ext7,ext8,ext9,ext10,est1,est2,est3,est4,est5,est6,est7,est8,est9,est10,agr1,agr2,agr3,agr4,agr5,agr6,agr7,agr8,agr9,agr10,csn1,csn2,csn3,csn4,csn5,csn6,csn7,csn8,csn9,csn10,opn1,opn2,opn3,opn4,opn5,opn6,opn7,opn8,opn9,opn10]]
    y=str(model.predict(y)[0])
    if(y)=='1':
      extroversion="100%"
      neuroticism="100%"
      agreeableness="100%"
      conscientiousness="100%"
      openness="100%"
    elif(y)=='2':
      extroversion="0%"
      neuroticism="52%"
      agreeableness="100%"
      conscientiousness="0%"
      openness="27%"
    elif(y)=='3':
      extroversion="58%"
      neuroticism="0%"
      agreeableness="35%"
      conscientiousness="21%"
      openness="0%"
    elif(y)=='4':
      extroversion="84%"
      neuroticism="95%"
      agreeableness="13%"
      conscientiousness="86%"
      openness="88%"
    elif(y)=='5':
      extroversion="36%"
      neuroticism="72%"
      agreeableness="55%"
      conscientiousness="39%"
      openness="58%"
    elif(y)=='6':
      extroversion="64%"
      neuroticism="85%"
      agreeableness="50%"
      conscientiousness="70%"
      openness="78%"
    elif(y)=='7':
      extroversion="70%"
      neuroticism="99%"
      agreeableness="13%"
      conscientiousness="99%"
      openness="97%"
    elif(y)=='8':
      extroversion="27%"
      neuroticism="70%"
      agreeableness="64%"
      conscientiousness="28%"
      openness="45%"
    elif(y)=='9':
      extroversion="21%"
      neuroticism="64%"
      agreeableness="74%"
      conscientiousness="21%"
      openness="41%"
    elif(y)=='10':
      extroversion="51%"
      neuroticism="75%"
      agreeableness="74%"
      conscientiousness="54%"
      openness="63%"
    
    to_send={"Groupe":y,"openness":openness,"neuroticism":neuroticism,"extroversion":extroversion,"agreeableness":agreeableness,"conscientiousness":conscientiousness}

    return render_template("result.html",to_send=to_send)


if __name__=="__main__":
  app.run(port=8080,debug=True)