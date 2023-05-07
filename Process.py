import whois 
import uvicorn
import joblib,os
from Database import Data

def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)


def domain_info(domain_name):
    if is_registered(domain_name):
        whois_info = whois.whois(domain_name)
        dic={}
        dic["domain_name"]=whois_info["domain_name"][0]
        dic["registration"]=whois_info["registrar"]
        dic["org"]=whois_info["org"]
        dic["state"]=whois_info["state"]
        dic["country"]=whois_info["country"]
        return dic

#print(domain_info("https://www.w3schools.com/"))
def sign_up(name,phone_number,email,password):
    db=Data('Phising_site')
    data={"Name":name,"Phone_number":phone_number,"Email":email,"Password":password}
    db.Insert_data('User_details',data)
    return True

def user_login(email,password):
    db=Data('Phising_site')
    tup=list(db.Read_data('User_details','*','Email=\''+email+"\'"))
    if tup:
        tup=tup[0]
        if tup[3]==email and tup[4]==password:
            return tup[0]
        else:
            return False
    else:
        return False

def admin_login(email,password):
    db=Data('Phising_site')
    tup=list(db.Read_data('Admin_details','*','Email=\''+email+"\'"))
    if tup:
        tup=tup[0]
        if tup[3]==email and tup[4]==password:
            return True
        else:
            return False
    else:
        return False
    

def store(user_id,url,result):
    db=Data('Phising_site')
    data={"User_id":user_id,"Url":url,"Result":result}
    db.Insert_data('Phising_result',data)
    return True

def predict(features):
    phish_model = open('phishing.pkl','rb')
    phish_model_ls = joblib.load(phish_model)
    X_predict = []
    X_predict.append(str(features))
    y_Predict = phish_model_ls.predict(X_predict)
    if y_Predict == 'bad':
        result = "This is a Phishing Site"
    else:
        result = "This is not a Phishing Site"
    return (features, result)

def get_data():
    db=Data('Phising_site')
    data=db.Read_data("Phising_result","*")
    result=[]
    for i in data:
        result.append(list(i))
    return result

#k=get_data()
#for i in k:
#    print(i[0])

#store("1","https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_style_visibility","yes")
"""
A function that returns a boolean indicating 
whether a `domain_name` is registered
"""
# pip install python-whois
#print(domain_info("facebook.com"))
#print(domain_name)
#print(registration)
#print(org)
#print(state)
#print(country)
#print(creation_date)
#print(expiration_date)
#print(whois_info)
#print(predict("google.com"))
#pkl
