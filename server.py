from flask import Flask,render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import pandas as pd
from io import StringIO
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import json

ml=" "
with open('config.json', 'r') as c:
    params=json.load(c)['params']

local_server = True
app = Flask(__name__)
app.secret_key = 'secret message key'
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Users(db.Model):
    uid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(12), nullable=False)
    pwd = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    tele = db.Column(db.String(12), nullable=False)
    city = db.Column(db.String(12), nullable=False)
    zip = db.Column(db.String(12), nullable=False)
    gen = db.Column(db.String(12), nullable=False)
    addr = db.Column(db.String(12), nullable=False)
    profilepic = db.Column(db.String(12), nullable=True)

class Frequest(db.Model):
    sno = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ufrom = db.Column(db.String(80), nullable=False)
    uto = db.Column(db.String(80), nullable=False)
    requ = db.Column(db.String(12), nullable=False)

class Queries(db.Model):
    qid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    queri = db.Column(db.String(80), nullable=False)
    uemail = db.Column(db.String(80), nullable=False)
    uname = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(12), nullable=False)

class Interaction(db.Model):
    qid = db.Column(db.Integer, nullable=False, primary_key=True)
    asker = db.Column(db.String(80), nullable=False)
    user = db.Column(db.String(80), nullable=False, primary_key=True)
    ans = db.Column(db.String(80), nullable=False)

class Calc(db.Model):
    email = db.Column(db.String(80), nullable=True, primary_key=True)
    weight = db.Column(db.Float, nullable=True)
    ps = db.Column(db.Float, nullable=False)
    pa = db.Column(db.Float, nullable=True)
    pc = db.Column(db.Float, nullable=True)
    closeness = db.Column(db.Float, nullable=True)
    metric = db.Column(db.Float, nullable=True)

class Friends(db.Model):
    user1 = db.Column(db.String(100), nullable=False, primary_key=True)
    user2 = db.Column(db.String(100), nullable=False, primary_key=True)

class Weight(db.Model):
    Users = db.Column(db.String(100), nullable=False, primary_key=True)
    Business = db.Column(db.Integer, nullable=False, primary_key=True)
    Food = db.Column(db.Integer, nullable=False, primary_key=True)
    Education = db.Column(db.Integer, nullable=True,primary_key=True)
    Politics = db.Column(db.Integer, nullable=True,primary_key=True)
    Computer = db.Column(db.Integer, nullable=True,primary_key=True)

#class Weight(db.Model):
 #   user = db.Column(db.String(80), nullable=True,primary_key=True)
 #   music = db.Column(db.Integer, nullable=True)
  #  movies = db.Column(db.Integer, nullable=True)
  #  television = db.Column(db.Integer, nullable=True)
 #   books = db.Column(db.Integer, nullable=True)

@app.route("/")
def hello():
    quer = Queries.query.filter_by(status='new')
    return render_template('index.html', params=params, quer=quer)
    # return render_template('index.html', params=params)

@app.route("/yourqueries")
def yourqueries():
    x=[]
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    queries = Queries.query.filter_by(uemail=session['email'])
    for i in queries:
        inter=Interaction.query.filter(Interaction.qid== i.qid,Interaction.ans.isnot(None))
        #inter = Interaction.query.filter(ans!=None,qid=i.qid).all()
        #inter = db.engine.execute("select * from interaction where qid='" + str(i.qid)+ "' and ans !='non'").scalar()
        for j in inter:
            x.append(j.ans)
            x.append(j.user)
            print(j.ans)
            print(j.user)
    length=len(x)
    return render_template('yourqueries.html', params=params, queries=queries, f_len=f_len, x=x, length=length)


'''
@app.route("/freq")
def freq():
    return render_template('index.html', params=params)
'''

@app.route("/search2", methods = ['GET', 'POST'])
def search2():
    id = "fail"
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    if request.method=='POST':
        x=0
        mail = request.form.get('mail')
        p_fr = Frequest.query.filter_by(ufrom=session['email'], uto=mail)
        if p_fr.count()>0:
            x=x+1
        else:
            entry = Frequest(ufrom=session['email'], uto =mail , requ='req')
            db.session.add(entry)
            db.session.commit()
        id = "succ"
    return render_template('search2.html', params=params, username=session['username'], email=session['email'], f_len=f_len, id=id, x=x)

@app.route("/usearch", methods = ['GET', 'POST'])
def usearch():
    id = "fail"
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    if request.method=='POST':
        query = request.form.get('friend')
        u_s = Users.query.filter_by(name=query)
        u_f = Friends.query.filter_by(user1 = session['email'])
        id = "succ"
    return render_template('usearch.html', params=params, u_f=u_f, username=session['username'], email=session['email'], f_len=f_len, id=id, u_s=u_s)


@app.route("/postquery", methods = ['GET', 'POST'])
def postquery():
    id = "fail"
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    if request.method=='POST':
        query = request.form.get('query')
        print(query)
        entry = Queries(queri=query, uemail = session['email'], uname = session['username'], status = 'new')
        db.session.add(entry)
        db.session.commit()
        id = "succ"
    return render_template('postquery.html', params=params, username=session['username'], email=session['email'], f_len=f_len, id=id)


@app.route('/u_check')
def u_check():
    if 'username' in session:
       return redirect(url_for('u_home'))
    else:
       return "You are not logged in <br><a href = '/user'></b>" + "click here to log in</b></a>"

@app.route("/u_home")
def u_home():
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    return render_template('u_home.html', params=params, username=session['username'], email=session['email'], f_len=f_len)


@app.route("/uqueries2", methods=['GET', 'POST'])
def uqueries2():
    if request.method=='POST':
        qid_s = request.form.get("qid_s")
        ans = request.form.get("ans")
        upd = Interaction.query.filter_by(qid=qid_s, user=session['email']).first()
        upd.ans= ans
        #x = db.engine.execute("update interaction set ans='" +request.form.get("ans")+ "' where qid = '" +qid+ "' && user=' " +session['email']+ "' ").scalar()
        db.session.commit()
    return redirect(url_for('uqueries'))





@app.route("/uqueries")
def uqueries():
    qid_list=[]
    qname_list=[]
    question=[]
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    uquer = Interaction.query.filter_by(user=session['email'], ans=None)
    for i in uquer:
        qid_list.append(i.qid)
        qname_list.append(i.asker)
    print(qname_list)
    for id in qid_list:
        ques = Queries.query.filter_by(qid=id)
        question.append(ques[0].queri)
    print(qid_list)
    print(type(question))

    return render_template('uqueries.html', params=params, username=session['username'], email=session['email'], f_len=f_len, uquer=uquer, question=question, qname_list=qname_list, qid_list=qid_list)

@app.route("/freq")
def freq():
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    return render_template('freq.html', params=params, freqt=freqt, f_len=f_len)

@app.route("/viewf")
def viewf():
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    frie = Friends.query.filter_by(user1=session['email'])
    return render_template('viewf.html', params=params, f_len=f_len, frie=frie)

@app.route("/viewint")
def viewint():
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    wei = Weight.query.filter_by(Users=session['email'])
    return render_template('viewint.html', params=params, f_len=f_len, wei=wei)


@app.route("/accept", methods = ['GET', 'POST'])
def accept():
    freqt = Frequest.query.filter_by(uto=session['email'], requ='req')
    f_len = freqt.count()
    try:
        if request.method=='POST':
            mail = request.form.get('mail')
            entry = Friends(user1= session['email'], user2 = mail)
            db.session.add(entry)
            entry1 = Friends(user1=mail , user2 =session['email'])
            db.session.add(entry1)
            Frequest.query.filter_by(uto=session['email'], ufrom=mail).delete()
            db.session.commit()
            f=1
    except:
        f=0
    return render_template("accept.html", f=f, f_len=f_len)

@app.route("/user", methods = ['GET', 'POST'])
def user():
    session.pop('username', None)
    session.pop('email', None)
    if request.method=='POST':
        uid = request.form.get('uid')
        pwd = request.form.get('pwd')
        post = Users.query.filter_by(email=uid, pwd=pwd).first()
        if post:
            session['username'] = post.name
            session['email'] = post.email
        return redirect(url_for('u_check'))
    return render_template('user.html', params=params)

@app.route("/tags", methods=['GET', 'POST'])
def tags():
    if request.method=='POST':
        print(request.form)
        a = request.form.get('1',0)
        b = request.form.get('2',0)
        c = request.form.get('3',0)
        d = request.form.get('4',0)
        e = request.form.get('5',0)
        print('line274')
        print(a,b,c,d,e)
        entry = Weight(Users =session['email'],Business = a, Food = b, Education = c, Politics = d, Computer = e)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('user'))

    return render_template('tags.html', params=params)

@app.route("/tags2",methods=['GET','POST'])
def tags2():
    if(request.method=='POST'):
        name = request.form
        print(name)
        for n in name:
            print(n)

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if(request.method=='POST'):
        global ml
        '''Add entry to the database'''
        name = request.form.get('name')
        lname = request.form.get('lname')
        pwd = request.form.get('pwd')
        email = request.form.get('email')
        tele = request.form.get('tele')
        city = request.form.get('city')
        zip = request.form.get('zip')
        gen = request.form.get('gen')
        addr = request.form.get('addr')
        session['email']=email
        entry = Users(name=name, lname = lname, pwd = pwd, email= email, tele = tele, city = city, zip = zip, gen = gen, addr = addr)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('tags'))

    return render_template('signup.html', params=params)

@app.route("/admin_home")
def admin_home():
    return render_template("admin_home.html", params=params)

@app.route("/queries")
def queries():
    quer = Queries.query.filter_by(status='new')
    return render_template("queries.html", params=params, quer=quer)

@app.route("/process",methods = ['POST', 'GET'])
def process():
    qid = request.args.get('id')
    session['qid']=qid
    query_ad = Queries.query.filter_by(qid=qid)
    df = pd.read_csv('C:/Users/adity/Downloads/Final Year Final-20220513T065420Z-001/Final Year Final/questions - questions.csv')
    col = ['query', 'category']
    df = df[col]
    df = df[pd.notnull(df['query'])]
    df.columns = ['query', 'category']
    df['category_id'] = df['category'].factorize()[0]
    category_id_df = df[['category', 'category_id']].drop_duplicates().sort_values('category_id')
    category_to_id = dict(category_id_df.values)
    id_to_category = dict(category_id_df[['category_id', 'category']].values)
    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=1, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
#features = tfidf.fit_transform(df.).toarray()\n",
    labels = df.category_id
#features.shape\n",
    X_train, X_test, y_train, y_test = train_test_split(df['query'], df['category'], random_state = 0, test_size=20)
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = MultinomialNB().fit(X_train_tfidf, y_train)
    session['qemail']=query_ad[0].uemail
    session['que']=query_ad[0].queri
    session['qname']=query_ad[0].uname
    cat = clf.predict(count_vect.transform([query_ad[0].queri]))
    session['cat']=str(cat)
    return render_template("process.html", params=params, query_ad=query_ad, cat=session['cat'], que=session['que'], qemail=session['qemail'], qname=session['qname'])

@app.route("/process2", methods = ['GET', 'POST'])
def process2():
    wei=[]
    cat1=session['cat']
    end=cat1.rfind(']')
    end=end-1
    cat=cat1[2:end]
    cat=cat.lower()
    Calc.query.delete()
    frie = Friends.query.filter_by(user1=session['qemail'])
#    max1= db.engine.execute("select count(user1) from Friends where user1= '"+session['qemail']+"' ").scalar()
    for i in frie:
        weigh = db.engine.execute("select " +cat+ " from weight where users= '" +i.user2+ "' ").scalar()
        wei.append(weigh)
        entry = Calc(email=i.user2, weight = weigh)
        db.session.add(entry)
        db.session.commit()
    print(wei)
    return render_template("process2.html", params=params, cat=cat, frie=frie, wei=wei)

@app.route("/forwardque", methods=['GET', 'POST'])
def forwardque():
    wei=[]
    cat1=session['cat']
    end=cat1.rfind(']')
    end=end-1
    cat=cat1[2:end]
    cat=cat.lower()
    # frie = Friends.query.filter_by(user1=session['qemail'])
    frie=db.engine.execute("select user2 from Friends where user1='" +session['qemail'] +"'").all()
    print('/')
    print(session['qemail'])
    print('/')
    print(frie)
#    max1= db.engine.execute("select count(user1) from Friends where user1= '"+session['qemail']+"' ").scalar()
    for i in frie:
        weigh = db.engine.execute("select " +cat+ " from Weight where users= '" +i[0]+ "' ").scalar()
        print(type(weigh))
        print(weigh)
        wei.append(weigh)
    j=0
    print(wei)
    for i in wei:
        if i>0:
            print('====')
            print(frie[j][0])
            print(session['qemail'])
            entry = Interaction(qid=session['qid'], asker = session['qemail'], user=frie[j][0], ans=None)
            db.session.add(entry)
        j=j+1    
    print("------------")
    print(session['qid'])        
    qd = Queries.query.filter_by(qid=session['qid']).first()
    print(qd)
    qd.status="old"
    db.session.commit()
    return redirect(url_for("admin_home"))
    


@app.route("/process3", methods = ['GET', 'POST'])
def process3():
    frie = Friends.query.filter_by(user1=session['qemail'])
    inter = Interests.query.filter_by(email=session['qemail'])

@app.route("/process4", methods = ['GET', 'POST'])
def process4():
    x=0.0
    int_count = db.engine.execute("select count(*) from interaction where asker='"+session['qemail']+"' group by qid").scalar()
    x=int_count
    fri_all = Friends.query.filter_by(user1=session['qemail'])
#    fri_all = db.engine.execute("select * from friends where user1='"+ session['qemail'] +"' ").scalar()
    for j in fri_all:
        d=0.0
        target=j.user2
        int_count_2 = db.engine.execute("select count(*) from interaction where asker='" +session['qemail']+ "' and user='" +target+ "' group by qid").scalar()
        if int_count_2:
            d = int_count_2
            #Calc.query.filter_by(email=j.user2).update(dict(pa=d/x))
            db.engine.execute("update calc set pa='" +str(d/x)+ "' where email = '" +j.user2+ "' ").scalar()
        else:
            db.engine.execute("update calc set pa='0.0' where email='" +j.user2+ "' ").scalar()
    return render_template('process4.htl')



@app.route("/admin", methods = ['GET', 'POST'])
def admin():
    if (request.method=='POST'):
        uid = request.form.get('uid')
        pwd = request.form.get('pwd')
        if uid=='system' and pwd=='system':
            return redirect(url_for('admin_home'))
    return render_template("admin.html", params=params)
@app.route("/trial")
def trial():
    return render_template('index1.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
