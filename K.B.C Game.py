question_list=["how many continents are there","what is the capital of india","ng na kon course pandey"]
option_list=[['four','nine','seven','eight'],
            ['chatishgarh','bhopal','chennai','delhi'],
            ['softwareengineer','counseling','tourism','agriculture',]]
fiftyfifty=[['four','seven'],['delhi','bhopal'],['softwareengineer','tourism']]
solutions=[2,1,2]
solution_list=[3,4,1]
li_c=0
def lifeline(ind):
    global li_c
    j=0
    if li_c==0:
        while j<len(fiftyfifty[ind]):
            print(j+1,fiftyfifty[ind][j])
            j+=1
        user=int(input("enter answer"))
        li_c+=1
        if user==solution_list[ind]:
            return True
        else:
            return False
    else:
        print("u already use 5050")
def option(ind):
    j=0
    while j<len(option_list):
        print(j+1,option_list[ind][j])
        j+=1
    user=int(input("enter number"))
    if user==solution_list[ind]:
        return True
    if user==5050:
        return False
def que():
    ind=0
    while ind<len(question_list):
        print(question_list[ind])
        result=option(ind)
        if result=="no":
            ind+=1
        elif result==True:
            print("congratulation")
        else:
            print("u loose")
        break
    ind=ind+1
def main():
    que()
main()