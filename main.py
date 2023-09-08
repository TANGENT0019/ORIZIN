import os.path
import uuid

import requests
from flask import Flask, render_template, request, session, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import random
import datetime
from sqlalchemy import func
from web3 import Web3
from werkzeug.utils import secure_filename

with open("config.json", "r") as c:
    params = json.load(c)["Params"]

app = Flask(__name__)
app.secret_key = "Re"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Rectifier'
app.config["ThumbnailStorage"] = params["ThumbnailStorage"]
app.config["VideoStorage"] = params["VideoStorage"]
app.config["TrailerStorage"] = params["TrailerStorage"]
app.config["ProfilePic"] = params["ProfilePic"]
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/61a4bd94e1964fc5a7f07df852d94b0a"))
receiving_address = params["AccountNumboffund"]  # Account_name
P_Key = params["Privet_Key"]  # private key
db = SQLAlchemy(app)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['GmailAddress'],
    MAIL_PASSWORD=params['GmailPassword']
)
mail = Mail(app)


class Userinfo(db.Model):
    UNAME = db.Column(db.String(80), nullable=False)
    Gmail = db.Column(db.String(20), nullable=False, primary_key=True)


class Aboutofuser(db.Model):
    About = db.Column(db.String(50), nullable=False)
    Gmail = db.Column(db.String(50), primary_key=True)


class Profilepic(db.Model):
    PPic = db.Column(db.String(50), nullable=False)
    UGmail = db.Column(db.String(50), primary_key=True)


class Productnameentery(db.Model):
    Product_Name = db.Column(db.String(50), nullable=False, primary_key=True)
    Parameters = db.Column(db.String(700), nullable=False)


class Indivisualentry(db.Model):
    Product_Name = db.Column(db.String(50), nullable=False)
    User_name = db.Column(db.String(50), nullable=False)
    Points = db.Column(db.String(700), nullable=False)
    Video = db.Column(db.String(50), nullable=False)
    UserEmail = db.Column(db.String(20), nullable=False)
    DateTime = db.Column(db.String(6), nullable=False, primary_key=True, default=db.func.current_timestamp())


class Purchase(db.Model):
    Product_Name = db.Column(db.String(50), nullable=False)
    Client = db.Column(db.String(50), nullable=False)
    Client_email = db.Column(db.String(50), nullable=False)
    Total_Rectifier = db.Column(db.String(750), nullable=False)
    Total_Value = db.Column(db.String(250), nullable=False)
    DateTime = db.Column(db.String(6), nullable=False, primary_key=True, default=db.func.current_timestamp())


class Commentpleace(db.Model):
    UserName = db.Column(db.String(50), nullable=False)
    UEmail = db.Column(db.String(50), nullable=False)
    Comment = db.Column(db.String(50), nullable=False)
    Date = db.Column(db.String(6), nullable=False, primary_key=True, default=db.func.current_timestamp())
    Authority = db.Column(db.Boolean, default=False)
    PPic = db.Column(db.String(50), nullable=True)


class Notification(db.Model):
    Heading = db.Column(db.String(700), nullable=False)
    Content = db.Column(db.String(700), nullable=False)
    ReacherEmail = db.Column(db.String(50), nullable=False)
    UniqueName = db.Column(db.String(700), nullable=False, primary_key=True)
    Product_Name = db.Column(db.String(50), nullable=True,)


Authorised_Email = ['ts2290352@gmail.com']
Otp = random.randrange(100000, 999999)

print(Otp)


def generate_unique_filename(filename):
    ext = ''
    if '.' in filename:
        ext = filename.rsplit('.', 1)[1]  # Get the file extension
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    return new_filename


def mathingWordsR(sentence1, sentence2):
    words1 = sentence1.strip().split("/")
    sentenc2 = sentence2.Catagory
    words2 = sentenc2.strip().split("/")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


def mathingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    sentenc2 = sentence2.Product_Name
    words2 = sentenc2.strip().split(" ")
    # scoreing
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


def duplicate_remover(ErroedList):
    DuplicateRemovedList = []
    for Errored in ErroedList:
        if not any(wc.Product_Name.split(".")[0] == Errored.Product_Name.split(".")[0] for wc in DuplicateRemovedList):
            DuplicateRemovedList.append(Errored)
    return DuplicateRemovedList


def most_liked_content(table_name):
    # Get the table class dynamically based on the provided table name
    table_class = globals()[table_name]

    # Query to get the most liked content and their like counts
    query = db.session.query(
        table_class.Content,
        table_class.Thumbnail,
        table_class.Gmail,
        table_class.Title,
        table_class.Profilepic,
        table_class.CreatorsName,
        db.func.count(table_class.Content).label('LikesCount')
    ).group_by(table_class.Content).order_by(db.desc('LikesCount'))

    # Execute the query and fetch the results
    result = query.all()

    # Retrieve the content with the highest count
    if result:
        most_liked_content = result[0][0]
    else:
        most_liked_content = None  # or any other default value you want to assign

    # Retrieve all rows associated with the most liked content
    rows = table_class.query.filter_by(Content=most_liked_content).all()

    # Retrieve the remaining liked content and their counts
    remaining_contents = result[1:]

    # Sort the remaining contents based on their like counts in descending order
    sorted_contents = sorted(remaining_contents, key=lambda x: x[1], reverse=True)

    # Use a set to store unique content names
    unique_content = {most_liked_content}

    # Retrieve all rows associated with the remaining liked content and add them to the unique_content set
    for content in sorted_contents:
        rows += table_class.query.filter_by(Content=content[0]).all()
        unique_content.add(content[0])

    # Remove duplicates based on the Content column
    rows = list({row.Content: row for row in rows}.values())

    return rows


@app.route("/registration", methods=["GET", "POST"])  # Registration BAr
def Log_in_bar():
    if request.method == "POST":
        name = request.form.get("Name")
        email = request.form.get("Email")
        DbEmail = Userinfo.query.filter_by(Gmail=email).order_by(Userinfo.UNAME).all()
        G = ""
        for i in DbEmail:
            G += i.Gmail
        if name == G:
            mg = "This email id is already existing"
            return render_template("registration.html", Msg=mg)
        try:
            mail.send_message('New message for ' + name,
                              sender=[params['GmailName'], params['GmailAddress']],
                              recipients=[email],
                              body='your OTP ' + str(Otp)
                              )
        except Exception as e:
            return render_template("registration.html", Msg="Opps, internet is not available")

        return render_template('OtpVerification.html', Uname=name, email=email)
    return render_template('registration.html')


@app.route("/OtpVerification", methods=["POST", "GET"])  # Verification
def Verification():
    name = request.form.get("Uname")
    email = request.form.get("U_Email")
    OTP = request.form.get("Verification")
    otpe = int(OTP)
    if Otp == otpe:
        LocalEmail = Userinfo.query.filter_by(Gmail=email).order_by(Userinfo.Gmail).all()
        if LocalEmail == []:
            mail.send_message('We have got a new user named ' + name,
                              sender=[params['GmailName'], params['GmailAddress']],
                              recipients=[params["ParthibAccount"]],
                              body='I have made a new user ' + name
                              )
            entry = Userinfo(UNAME=name, Gmail=email)
            db.session.add(entry)
            db.session.commit()
            session["E-user"] = email
            print(email)
            session["user"] = name
            return render_template("SucceedMassage.html", Sm="Verification Succeed")
        else:
            session["E-user"] = email
            session["user"] = name
            return render_template("SucceedMassage.html", Sm="Verification Succeed")
    else:
        return render_template("failed attempt.html", Sm="Verification failed")


@app.route("/logInBar", methods=["GET", "POST"])  # LOginBar
def LBAr():
    if 'user' in session and 'E-user' in session:
        UId = session['user']
        PP = UId[0]
        email = session['E-user']
        print(email)
        Comment = Profilepic.query.filter_by(UGmail=email).first()
        return render_template("Profile.html", PP=PP, Uname=UId, Email=email, Comment=Comment)
    elif request.method == "POST":
        name = request.form.get("Name")
        email = request.form.get("Email")
        G = ""
        y = ""
        DbEmail = Userinfo.query.filter_by(Gmail=email).order_by(Userinfo.Gmail).all()
        DbUName = Userinfo.query.filter_by(Gmail=email).order_by(Userinfo.UNAME).all()
        for i in DbUName:
            y += i.UNAME
        for i in DbEmail:
            G += i.Gmail
        if G == email and y == name:
            try:
                mail.send_message('New message for ' + name,
                                  sender=[params['GmailName'], params['GmailAddress']],
                                  recipients=[email],
                                  body='your OTP ' + str(Otp)
                                  )
                user_agent = request.headers.get('User-Agent')
                if 'Macintosh' in user_agent:
                    return render_template("OtpVerification.html", Uname=name, email=G)
                elif 'Windows' in user_agent:
                    return render_template("OtpVerification.html", Uname=name, email=G)
                else:
                    return render_template("OtpVerificationforTabs.html", Uname=name, email=G)
            except Exception as e:
                return render_template("LogIn.html", Msg="Opps, internet is not available")
        elif G == email or y == name:
            msge = "may be you have entered wrong User name or email id"
            return render_template('LogIn.html', Msg=msge)
        else:
            msge = "you have no Account sign in at first,please"
            return render_template('registration.html', Msg=msge)
    else:
        user_agent = request.headers.get('User-Agent')
        if 'Macintosh' in user_agent:
            return render_template("LogIn.html")
        elif 'Windows' in user_agent:
            return render_template("LogIn.html")
        else:
            return render_template("LoginforTabs.html")


@app.route("/LogOut")  # LOg out
def logOut():
    session.pop('user', None)
    session.pop('E-user', None)
    return render_template("Login.html")


@app.route("/Watched")  # Backend Pop up
def backed():
    if "user" in session:
        Comment = Profilepic.query.filter_by(UGmail=session['E-user']).first()
        return render_template('WatchedPopUp.html', Comment=Comment)

    massage = "Please, Login at first"
    user_agent = request.headers.get('User-Agent')
    if 'Macintosh' in user_agent:
        return render_template("LogIn.html", Msg=massage)
    elif 'Windows' in user_agent:
        return render_template("LogIn.html", Msg=massage)
    else:
        return render_template("LoginforTabs.html", Msg=massage)


@app.route("/Community", methods=["GET", "POST"])
def Community():
    if request.method == "POST":
        if 'user' in session:
            comment = request.form.get("Comment")
            UEamil = session['E-user']
            P = Profilepic.query.filter_by(UGmail=session['E-user']).first().PPic
            if UEamil in Authorised_Email:
                entry = Commentpleace(UserName=session['user'], UEmail=UEamil, Comment=comment, Authority=True, PPic=P)
                #notification
                all_Emails = Userinfo.query.all()
                for i in all_Emails:
                    if i.Gmail == session['E-user']:
                        continue
                    notify_saving = Notification(Heading="Helpful for you some new massages in chat box", Content=comment, ReacherEmail=i.Gmail, UniqueName=comment + i.Gmail +str(datetime.datetime.now()))
                    db.session.add(notify_saving)
                    db.session.commit()
            else:
                entry = Commentpleace(UserName=session['user'], UEmail=UEamil, Comment=comment, Authority=False, PPic=P)
            db.session.add(entry)
            db.session.commit()
            return redirect("/Community")
        else:
            massage = "Please, Login at first"
            return render_template('Login.html', Msg=massage)
    OverAllComment = Commentpleace.query.all()
    return render_template("Comment.html", Comments=OverAllComment)


@app.route("/Notification", methods=["GET", "POST"])
def notification():
    if 'user' in session:
        Notify = Notification.query.filter_by(ReacherEmail=session['E-user']).all()
        return render_template("Notification.html", notifications=Notify)
    else:
        massage = "Please, Login at first"
        return render_template('Login.html', Msg=massage)


@app.route("/Analytics")
def Analytics():
    if 'E-user' in session:
        ProductName = request.args.get("productName")
        if ProductName is None:
            Purchesed_Feedback = Purchase.query.filter_by(Client=session['user']).all()
            No_Repeat = duplicate_remover(Purchesed_Feedback)
            Comment = Profilepic.query.filter_by(UGmail=session['E-user']).first()
            return render_template("PlayerTrailer.html", content="", total_Purchesed=No_Repeat, Comment=Comment)
        else:
            # cheaking if the feedback is purchased by the client or not
            Client_email = session['E-user']
            Client = session['user']
            Client_Purchase = Purchase.query.filter_by(Product_Name=ProductName, Client=Client,
                                                       Client_email=Client_email).all()
            print(Client_Purchase)
            if len(Client_Purchase) == 0:
                return redirect("/Transaction?Product=" + ProductName)
            else:
                parameter_String = Productnameentery.query.filter_by(Product_Name=ProductName).first()
                induvisual_E = Indivisualentry.query.filter_by(Product_Name=ProductName).all()
                Parameter_List = parameter_String.Parameters.strip().split("~")
                Parameter_List.pop(0)
                Actual_List = []
                total_len = len(Parameter_List)
                for i in range(total_len):
                    dictionary = {'P_Name': Parameter_List[i], "data": [0, 0, 0, 0, 0, 0]}
                    Actual_List.append(dictionary)

                for item in induvisual_E:
                    Value_List = item.Points.strip().split("~")
                    Value_List.pop(0)
                    New_Value = [int(x) for x in Value_List]
                    try:
                        for i in range(5):
                            The_Value = New_Value[i]
                            Actual_List[i]['data'][The_Value] = Actual_List[i]['data'][The_Value] + 1
                    except Exception as e:
                        pass
                print(total_len)
                Purchesed_Feedback = Purchase.query.filter_by(Client=session['user']).all()
                No_Repeat = duplicate_remover(Purchesed_Feedback)
                Comment = Profilepic.query.filter_by(UGmail=session['E-user']).first()
                return render_template("PlayerTrailer.html", content=parameter_String, Actual_List=Actual_List,
                                       L=len(Actual_List), total_Purchesed=No_Repeat, Comment=Comment,
                                       PName=ProductName)
    else:
        massage = "Please, Login at first"
        return render_template('Login.html', Msg=massage)


@app.route("/AboutInput", methods=["Get", "POST"])
def AboutInput():
    if 'user' in session:
        if request.method == "POST":
            About = request.form.get("About_Write")
            Gmail = session["E-user"]
            Uinfo = Aboutofuser.query.filter_by(Gmail=Gmail).all()
            if len(Uinfo) == 0:
                entry = Aboutofuser(About=About, Gmail=Gmail)
                db.session.add(entry)
                db.session.commit()
                return redirect('/studios')
            else:
                Uinfo = Aboutofuser.query.filter_by(Gmail=Gmail).first()
                Uinfo.About = About
                db.session.commit()
                return redirect('/studios')
        MyName = session['user']
        MYEmail = session['E-user']
        About = Aboutofuser.query.filter_by(Gmail=MYEmail).all()
        PP = Profilepic.query.filter_by(Gmail=MYEmail).all()
        return render_template('StudioUpload.html', name=MyName, Abouts=About, PPs=PP)
    else:
        massage = "Please, Login at first"
        return render_template('Login.html', Msg=massage)


@app.route("/ProfilePic", methods=["Get", "POST"])
def ProfilePic():
    if 'user' in session:
        if request.method == "POST":
            Profilepi = request.files["ProfilePic"]
            Filen = secure_filename(Profilepi.filename)
            Gmail = session["E-user"]
            Uinfo = Profilepic.query.filter_by(UGmail=Gmail).all()
            NewProfilePic = generate_unique_filename(Filen)
            if len(Uinfo) == 0:
                Profilepi.save(os.path.join(app.config["ProfilePic"], NewProfilePic))
                entry = Profilepic(PPic=NewProfilePic, UGmail=Gmail)
                db.session.add(entry)
                db.session.commit()
                return redirect('/studios')
            else:
                Uinfo = Profilepic.query.filter_by(Gmail=Gmail).first()
                Uinfo.PPic = NewProfilePic
                db.session.commit()
                return redirect('/studios')

        MyName = session['user']
        MYEmail = session['E-user']
        About = Aboutofuser.query.filter_by(Gmail=MYEmail).all()
        PP = Profilepic.query.filter_by(Gmail=MYEmail).all()
        return render_template('StudioUpload.html', name=MyName, Abouts=About, PPs=PP)
    else:
        massage = "Please, Login at first"
        return render_template('Login.html', Msg=massage)


@app.route("/uploading", methods=['GET', 'POST'])  # UPloading Video
def uploading():
    if 'user' in session and 'E-user' in session:
        if request.method == "POST":
            try:
                # Get the data from the POST request
                Fparameters_json = request.form.get('Fparameters')
                RespectedRating_json = request.form.get('RespectedRating')
                Productname = request.form.get('ProductName')
                VideoClip = request.files.get("VideoFile")

                # Convert the JSON strings to Python lists
                Fparameters = json.loads(Fparameters_json)
                RespectedRating = json.loads(RespectedRating_json)
                # Processing for database entry
                Parametersentry = ""
                Points = ""
                for i in Fparameters:
                    Parametersentry = Parametersentry + "~" + i
                for m in RespectedRating:
                    Points = Points + "~" + m

                # notification
                New_Parametres = Parametersentry
                old_Parameters = Productnameentery.query.filter_by(Product_Name=Productname).first().Parameters
                print(New_Parametres, old_Parameters)
                Timeing = str(datetime.datetime.now())
                if len(New_Parametres) > len(old_Parameters):
                    old_Rectifiers = Indivisualentry.query.filter_by(Product_Name=Productname).all()
                    print(old_Rectifiers)
                    for IEntry in old_Rectifiers:
                        print(IEntry.UserEmail)
                        if IEntry.UserEmail == session['E-user']:
                            continue
                        heading = "Some new parameters Arrived for " + Productname
                        content = "Previously, you have uploaded feedback of " + Productname + " some new parameters " \
                                                                                               "are added, please " \
                                                                                               "edit you feedback for " \
                                                                                               "better services"
                        eeentry = Notification(Heading=heading, Content=content, ReacherEmail=IEntry.UserEmail,
                                               UniqueName=heading + IEntry.UserEmail + Timeing, Product_Name=Productname)
                        db.session.add(eeentry)
                        db.session.commit()

                # final database entry
                # especially for product parameters
                productCheaking = Productnameentery.query.filter_by(Product_Name=Productname).first()
                if type(productCheaking) is None:
                    ListOfParameters = Productnameentery(Product_Name=Productname, Parameters=Parametersentry)
                    db.session.add(ListOfParameters)
                    db.session.commit()
                else:
                    productCheaking = Productnameentery.query.filter_by(Product_Name=Productname).first()
                    productCheaking.Product_Name = Productname
                    productCheaking.Parameters = Parametersentry
                    db.session.commit()

                # identification if the uploading processor is edit or new
                Privious_Record = Indivisualentry.query.filter_by(UserEmail=session['E-user'], Product_Name=Productname).first()
                if type(Privious_Record) is None:                           # new entry
                    Unique_name = generate_unique_filename(VideoClip.filename)
                    VideoClip.save(os.path.join(app.config["VideoStorage"], Unique_name))
                    entry = Indivisualentry(Product_Name=Productname, User_name=session['user'], Points=Points,
                                            Video=Unique_name, UserEmail=session['E-user'])
                    db.session.add(entry)
                    db.session.commit()
                else:                                                       #edit content
                    #cheaking new uploaded video is available
                    if VideoClip is None:                             # user not trying to change the video
                        VideoName = Privious_Record.Video
                        Privious_Record.Product_Name = Productname
                        Privious_Record.User_name = session['user']
                        Privious_Record.UserEmail = session['E-user']
                        Privious_Record.Points = Points
                        Privious_Record.Video = VideoName
                        db.session.commit()
                    else:
                        Unique_name = generate_unique_filename(VideoClip.filename)
                        VideoClip.save(os.path.join(app.config["VideoStorage"], Unique_name))
                        Privious_Record.Product_Name = Productname
                        Privious_Record.User_name = session['user']
                        Privious_Record.UserEmail = session['E-user']
                        Privious_Record.Points = Points
                        Privious_Record.Video = Unique_name
                        db.session.commit()

                # Return a response (optional)
                # In this example, we'll just return a success message, but you can customize the response as needed.
                response_data = {'message': 'Data received successfully'}
                return jsonify(response_data), 200

            except Exception as e:
                # Handle any errors that might occur during processing
                error_message = {'error': str(e)}
                return jsonify(error_message), 400
        forTap = request.args.get("fortapping")
        PP = Profilepic.query.filter_by(UGmail=session['E-user']).first()
        About = Aboutofuser.query.filter_by(Gmail=session['E-user']).first()
        return render_template('FeedBackUpload.html', ProfilePic=PP, Abouts=About, fortapping=forTap)
    massage = "Please, Login at first"
    return render_template('Login.html', Msg=massage)


@app.route("/EditFeedback", methods=["GET", "POST"])
def EditFeedback():
    if 'user' in session and 'E-user' in session:
        Product_Name = request.args.get("Product_Name")
        parameters = Productnameentery.query.filter_by(Product_Name=Product_Name).first()
        RectifiersValue = Indivisualentry.query.filter_by(Product_Name=Product_Name,
                                                          UserEmail=session['E-user']).first()
        listParams = parameters.Parameters.strip().split("~")
        valuelist = RectifiersValue.Points.strip().split("~")
        valuelist.pop(0)
        listParams.pop(0)
        PP = Profilepic.query.filter_by(UGmail=session['E-user']).first()
        About = Aboutofuser.query.filter_by(Gmail=session['E-user']).first()
        return render_template("FeedbackUploadedEdit.html", ProfilePic=PP, Abouts=About, Parameters=listParams,
                               RectifiersValue=valuelist, ProductName=Product_Name)
    massage = "Please, Login at first"
    return render_template('Login.html', Msg=massage)


@app.route("/ProvidedParameters", methods=["GET", "POST"])
def ProvidedParameters():
    productName = request.args.get("productName")
    Parameters = Productnameentery.query.filter_by(Product_Name=productName).first()
    Par = Parameters.Parameters
    Params = Par.strip().split("~")
    Params.pop(0)

    for i in Params:
        print(i)
    # Returning the list of parameters as a JSON response
    return jsonify(parameters=Params)


@app.route("/studios", methods=["GET", "POST"])  # STudios
def studios():
    if 'user' in session and 'E-user' in session:
        MyName = session['user']
        MYEmail = session['E-user']
        About = Aboutofuser.query.filter_by(Gmail=MYEmail).first()
        PP = Profilepic.query.filter_by(UGmail=MYEmail).first()
        feedbacks = Indivisualentry.query.filter_by(UserEmail=session['E-user']).all()
        return render_template('StudioUpload.html', name=MyName, Abouts=About, ProfilePic=PP, Contents=feedbacks)
    else:
        massage = "Please, Login at first"
        return render_template('Login.html', Msg=massage)


@app.route("/")  # Main Home page
def hello():
    # Check if the user is in the session
    if "E-user" in session:
        # Fetch the user's liked and watched content based on their email ID
        user_email = session["E-user"]
        user_agent = request.headers.get('User-Agent')
        Comment = Profilepic.query.filter_by(UGmail=user_email).first()
        contents = Productnameentery.query.all()

        if 'Macintosh' in user_agent:
            return render_template("index.html", Comment=Comment, Liked=contents)
        elif 'Windows' in user_agent:
            return render_template("index.html", Comment=Comment, Liked=contents)
        else:
            return render_template("indexfortabs.html", Comment=Comment, Liked=contents)
    else:
        user_agent = request.headers.get('User-Agent')
        contents = Productnameentery.query.all()
        if 'Macintosh' in user_agent:
            return render_template("index.html", Liked=contents)
        elif 'Windows' in user_agent:
            return render_template("index.html", Liked=contents)
        else:
            return render_template("indexfortabs.html", Liked=contents)


@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    incomplete_data = request.form.get('IncompleteData')
    SearchableItems = Productnameentery.query.all()
    scores = [mathingWords(incomplete_data, sentence) for sentence in SearchableItems]
    sortedSentScore = sorted(zip(scores, SearchableItems), reverse=True, key=lambda x: x[0])
    sortedSentScore = [(score, sentence) for score, sentence in sortedSentScore if score != 0]
    print(f"{len(sortedSentScore)} results found!")

    # Convert Productnameentery objects to dictionaries
    suggestions = [{'score': score, 'Product_Name': sentence.Product_Name} for score, sentence in sortedSentScore]

    # Return the suggestions as JSON
    return jsonify(suggestions)


@app.route("/Search", methods=['POST', 'GET'])
def search():
    SearchItem = request.form.get("Search")
    SearchableItems = Productnameentery.query.all()

    scores = [(mathingWords(SearchItem, sentence), sentence) for sentence in SearchableItems]
    sortedSentScore = sorted(scores, reverse=True, key=lambda x: x[0])
    sortedSentScore = [(score, sentence) for score, sentence in sortedSentScore if score != 0]

    # Remove elements from SearchableItems that are present in sortedSentScore
    S = [item for item in SearchableItems if item not in [entry for score, entry in sortedSentScore]]

    print(f"{len(sortedSentScore)} results found!")

    if "E-user" in session:  # Check if the key is present in the session
        Comment = Profilepic.query.filter_by(UGmail=session["E-user"]).first()
    else:
        Comment = None  # Handle the case when "E-user" key is not found

    return render_template("Searched.html", ASearch=sortedSentScore, Comment=Comment, searchedItem=SearchItem,
                           OSearch=S)


@app.route("/DelPPic", methods=['GET'])
def delpic():
    Cname = request.args.get("Cname")
    Doption = Profilepic.query.filter_by(PPic=Cname).first()
    db.session.delete(Doption)
    db.session.commit()
    return redirect("/studios")


@app.route("/DelFeedback", methods=['GET'])
def delFeedback():
    CEamil = request.args.get("CEmail")
    Cvideo = request.args.get("CVideo")
    print(Cvideo)
    print(CEamil)
    Doption = Indivisualentry.query.filter_by(Video=Cvideo, UserEmail=CEamil).first()
    print(Doption)
    db.session.delete(Doption)
    db.session.commit()
    return redirect("/studios")


@app.route("/DelAbout", methods=['GET'])
def delAbout():
    Doption = Aboutofuser.query.filter_by(Gmail=session['E-user']).first()
    print(Doption)
    db.session.delete(Doption)
    db.session.commit()
    return redirect("/studios")


@app.route("/Transaction", methods=["POST", "GET"])
def Transfer():
    if 'user' in session:
        if request.method == "POST":
            # Data collection
            P_Name = request.form.get("Thumbnail")
            Amount = request.form.get("amount")
            print(Amount)
            from_Account = request.form.get("AccountNumber")
            try:
                # currency transfer
                amount_in_dollars = float(Amount)
                eth_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd").json()[
                    "ethereum"]["usd"]
                amount_in_ether = amount_in_dollars / eth_price
                # transaction
                amount = int(amount_in_ether) * 10 ** 18  # Convert to Wei
                sender_address = from_Account

                if not w3.isAddress(sender_address) or not w3.isAddress(receiving_address):
                    Client = session["user"]
                    Client_Email = session["E-user"]
                    ProductName = P_Name
                    feedbacks = Indivisualentry.query.filter_by(Product_Name=ProductName).all()
                    url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
                    response = requests.get(url)
                    print(len(feedbacks) * 12.5)
                    return render_template("Payment.html", Name=ProductName, Purcheser=Client,
                                           PurcheserEmail=Client_Email,contents=feedbacks,
                                           ether=response, alurt="Please, enter a proper account number")

                nonce = w3.eth.getTransactionCount(sender_address)
                gas_price = w3.eth.gasPrice

                transaction = {
                    "to": receiving_address,
                    "value": amount,
                    "gas": 21000,  # Standard gas for Ethereum transfer
                    "gasPrice": gas_price,
                    "nonce": nonce,
                }

                private_key = "SENDER_PRIVATE_KEY"  # Replace with actual private key
                signed_txn = w3.eth.account.signTransaction(transaction, private_key)

                tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
                # Database entry
                Total_Rectifier = ""
                Total_Indivisual_Entry = Indivisualentry.query.filter_by(Product_Name=P_Name).all()
                for i in Total_Indivisual_Entry:
                    Total_Rectifier = Total_Rectifier + "~" + i.User_name
                # Final entry
                entry = Purchase(Product_Name=P_Name, Client=session['user'], Client_email=session['E-user'],
                                 Total_Rectifier=Total_Rectifier, Total_Value=Amount)
                db.session.add(entry)
                db.session.commit()
                return render_template("SucceedMassage.html", sm="complete")  # tx_hash=tx_hash.hex()

            except Exception as e:
                # Log the error or perform any necessary actions
                print(f"Error: {e}")
                Client = session["user"]
                Client_Email = session["E-user"]
                ProductName = P_Name
                feedbacks = Indivisualentry.query.filter_by(Product_Name=ProductName).all()
                url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
                response = requests.get(url)
                print(len(feedbacks) * 12.5)
                return render_template("Payment.html", Name=ProductName, Purcheser=Client,
                                       PurcheserEmail=Client_Email, contents=feedbacks,
                                       ether=response, alurt="some error occurred, try again")
        else:
            Client = session["user"]
            Client_Email = session["E-user"]
            ProductName = request.args.get("Product")
            feedbacks = Indivisualentry.query.filter_by(Product_Name=ProductName).all()
            url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
            response = requests.get(url)
            print(len(feedbacks) * 12.5)
            return render_template("Payment.html", Name=ProductName, Purcheser=Client, PurcheserEmail=Client_Email,
                                   contents=feedbacks, ether=response)
    else:
        massage = "Please, Login at first"
        return render_template('Login.html', Msg=massage)


app.run(debug=True)
