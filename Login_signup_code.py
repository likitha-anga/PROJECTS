import json,os
def my():
    user=(input("enter login or signup :  "))
    if user=="signup":
        u_name=input("enter the user_name :  ")
        password=input("enter the Password:")
        if len(password)>=1 and len(password)<=10:
            if "@" in password or "#" in password or "$" in password:
                if "A" or "Z" in password:
                    if "0" or "9" in password:
                        if "a" or "z" in password:
                            print("strong password")
            password1=((input("re_enter  the password :  ")))
            if password==password1 :
                print("your password is match")
                if(os.path.isfile('Signup.json')):
                    op=open("Signup.json","r")
                    a=json.load(op)
                    for i in a["user"]:
                        if i["username"]==u_name:
                            print("Already Exists")
                        else:
                            dic={}
                            d={}
                            dic["username"]=u_name
                            dic["password"]=password1
                            d["Description"]=input("enter description : ")
                            d["D.O.B"]=input("enter D.O.B : ")
                            d["Gender"]=input("enter your gender : ")
                            d["Hobbies"]=input("enter your hobbies : ")
                            dic["Profile"]=d
                            v=a["user"]
                            v.append(dic)
                            f=open("Signup.json","w+")
                            json.dump(a,f,indent=4)  
                            f.close()
                            print("Signup Succesfully")
                            break  
                else:
                    print("does't match")
            else:
                print("invalid")     
    elif user=="login":
        a=open("Signup.json","r")                 
        f=json.load(a)
        d=input("Enter your user name for login:")
        v=input("Enter your password for login:")
        for i in f["user"]:
            if d==i['username']:
                if v==i['password']:
                    print("Login successful")
                    print(i)
                else:
                    print("Check your password")
                    break
            else:
                print("Check your user_name")
                break
    else:
        print("Your enter worng input ")       
my()
