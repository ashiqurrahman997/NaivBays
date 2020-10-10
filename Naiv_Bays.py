import csv

def probability(data,arg,arg1):
  
        prm=arg.split(' = ')
        prm1=arg1.split(' = ')
        key=prm[0].strip()
        key1=prm1[0].strip()
        valu=prm[1].strip()
        valu1=prm1[1].strip()
        count=0
        c=0
        for i in range(len(data[key1])):
            if(data[key1][i]==valu1):
                count=count+1
               
        for i in range(len(data[key])):
            
            if((data[key][i])==valu and data[key1][i]==valu1):
                c=c+1
                #print('index:',i+1,' ',data[key][i],' : ',data[key1][i])

        print('P(',arg,'|',arg1,')=',c/count)
        return (c/count)
 

def main():

    infile=open('data.csv', 'r')
    
    reader = csv.DictReader(infile)
    
    data = {}
    for row in reader:
        for header, value in row.items():
            
             try:
                data[header].append(value)
             except KeyError:
                data[header] = [value]
                
             
    print('DATA:')
    print('  ',end=' ')
    for i in data.keys():
        print(i, end='  ')
        clm=i
    print()
  
    for i in range(len(data[clm])):
        print(i+1,end='  ')
        for j in data.values():
            print(j[i],end='   ')
        print()
            
    print()
    while(1):
        print('Enter the Class :')
        
        C1=input()
        C2=input()
        C3=C1.split(' = ')
        C4=C2.split(' = ')
        
        
        bk=0
        for i in data.keys():
            if(i.strip()==C3[0] and i.strip()==C4[0]):
                 bk=1
                 break
                
        if(bk==1):
            break
        else:
             print('Class error.Give a space in both side of \'=\' or check input. ')
                 
                 
    count_yes=0
    count_no=0
    total_elmnt=len(data[C3[0]])
    
    for i in range(len(data[C3[0]])):
        if(data[C3[0]][i]==C3[1]):
                count_yes=count_yes+1

    for i in range(len(data[C4[0]])):
        if(data[C4[0]][i]==C4[1]):
                count_no=count_no+1
            
        
    try:
        #X =' age = <=30,income = medium,student = yes,credit_rating = fair '
        #X= ' outlook = sunny,temp = hot,humidity = normal,windy = false '
        X=input('Data to be Classified X :')
        print('X -> ',X)
    
        prm=X.split(',')

        s_y=1
        s_n=1
    
        print() 
        for atr in prm:
              s_y=s_y*probability(data,atr,C1)
           
        print()
        for atr in prm:
              s_n=s_n*(probability(data,atr,C2))
        print()
 
        print('P(X|YES)=',s_y)
        print('P(X|NO)=',s_n)
        print()
        print('P(YES)=',count_yes/total_elmnt)
        print('P(NO)=',count_no/total_elmnt)
        print()
        f_yes=s_y*(count_yes/total_elmnt)
        f_no=s_n*(count_no/total_elmnt)
        print('P(YES|X)=P(X|YES)*P(YES)')
        print('        = ',f_yes)
        print()
        print('P(NO|X)=P(X|NO)*P(NO)')
        print('        = ',f_no)
        print()
        if(f_yes>f_no):
                print('P(YES|X) > P(NO|X). So X  belongs to YES.')
                print()
           
        else:
                 print('P(NO|X) > P(YES|X). So X  belongs to NO.')
                 print()

    except :
            print()
            print('Error in your Input (X) .Give a space in both side of \'=\' or Check  Attribute.')
           
    
main()


