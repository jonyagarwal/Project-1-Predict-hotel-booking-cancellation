'''PROBLEM STATEMENT:-
                    1.WHERE DO THE GUEST COME FROM
                    2.HOW MUCH DO GUEST PAY FOR A NIGHT.
                    
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("hotel_bookings.csv")

df.head()

df.shape#gives rows and columns in a dataset.
df.isna().sum()#find null values or missing values in a dataset.

def data_clean(df):
    df.fillna(0,inplace=True)
    print(df.isnull().sum())#replace all null values with 0.

data_clean(df)#call a function

df.columns#return all the columns from a dataset.

list=['adults', 'children', 'babies']#we want to find the unique values from these three columns.
for i in list:
    print('{} has unique values as {}'.format(i,df[i].unique()))
    
filter=(df['children']==0)&(df['adults']==0)&(df['babies']==0)#here we applied filter ie. adults,babies,children =0.
df[filter]

pd.set_option('display.max_columns',32)#this is used to display the columns as we want.
filter=(df['children']==0)&(df['adults']==0)&(df['babies']==0)
df[filter]

#we can see that babies,children and adults cant be 0 simuntaneously it means there is a problem so we remove our filter.

data=df[~filter]#remove filter from  dataset.
data.head()

country_wise_data=data[data['is_canceled']==0]['country'].value_counts().reset_index()#it will give the country data where booking is confirmed and cancelation chance is 0.
country_wise_data.columns=['country','no. of guests']#we can change the column name.
country_wise_data

import folium
from folium.plugins import HeatMap
folium.Map()
import plotly.express as px 
map_guest=px.choropleth(country_wise_data,
                        locations=country_wise_data['country'],
                         color=country_wise_data['no. of guests'],
                         hover_name=country_wise_data['country'],
                        title='Home Country of guests'
                        )
map_guest.show()
data.head()

plt.figure(figsize=(12,8))
sns.boxplot(x='reserved_room_type',y='adr',hue='hotel',data=data2)#hue is nothing but will do distribution according to hotel as well as resort.
plt.title('price of room types per night and per person')
plt.xlabel('Room type')
plt.ylabel('price(Euro)')
plt.legend()#legend is nothing but margin or difference we specify on the top right of the map with respect to x-axis and y-axis.for  in this legend is given to resort and hotel.
plt.show()

####HOW DOES THE PRICE PER NOIGHT VARY OVER THE YEAR.

data_resort=data[(data['hotel']=='Resort Hotel') & (data['is_canceled']==0)]#filter our data set.
data_city=data[(data['hotel']=='City Hotel') & (data['is_canceled']==0)]
data_resort.head()
data_resort.groupby(['arrival_date_month'])['adr'].mean()#it will give the mean of price of arrival  date month in group.
resort_hotel=data_resort.groupby(['arrival_date_month'])['adr'].mean().reset_index()#reset_index will reset the data in good looking data frame or data set.
city_hotel=data_city.groupby(['arrival_date_month'])['adr'].mean().reset_index()
city_hotel

final=resort_hotel.merge(city_hotel,on='arrival_date_month')
final.columns=['month','price_for _resort','priice_for_city_hotel']
final

import sort_dataframeby_monthorweek as sd#this is special package in python that sorts the months.
def sort_data(df,colname):
    return sd.Sort_Dataframeby_Month(df,colname)
final=sort_data(final,'month')
final
final.columns
px.line(final,x='month',y=['price_for _resort', 'priice_for_city_hotel'],title='room price per night over the month')

######WHICH ARE THE MOST BUSY MONTH OR IN WHICH MONTH THE GUEST ARE HIGH.
#####HOW LONG DO PEOPLE STAY IN HOTEL.

rush_resort=data_resort['arrival_date_month'].value_counts().reset_index()
rush_resort.columns=['month','no. of guests']
rush_resort

rush_city=data_city['arrival_date_month'].value_counts().reset_index()
rush_city.columns=['month','no. of guests']
rush_city

final_rush=rush_resort.merge(rush_city,on='month')

final_rush=rush_resort.merge(rush_city,on='month')
final_rush.columns=['month','no. of guests in resort','no. of guests in city']
final_rush

final_rush=sort_data(final_rush,'month')

final_rush.columns

px.line(final_rush,x='month',y=['no. of guests in resort', 'no. of guests in city'],title='total no. of guests per month')

####SELECT IMPORTANT FEATURES USING CORELATION FOR MACHINE LEARNING.

data.head()
data.corr()##it will give corelation .corelation is nothing but it tells about the effect of another feature or columns of data when will we do change in one feature of column.
co_relation=data.corr()['is_canceled']#it will give all corelation of is_canceled olumn or feature.
co_relation
co_relation.abs().sort_values(ascending=False)

list_not=data.groupby('is_canceled')['reservation_status'].value_counts()

cols=[]
for col in data.columns:
    if data[col].dtype!='O' and col not in list_not:
        cols.append(col)
cols

num_features=[col for col in data.columns if data[col].dtype!='O' and col not in list_not]#one line code of above.
num_features

data.columns
cat_not=['arrival_date_year','assigned_room_type','booking_changes', 'reservation_status','country','days_in_waiting_list']
cat_not#cat=catorigal 
cat_features=[col for col in data.columns if data[col].dtype!='O' and col not in cat_not]
cat_features

####EXTRACT DERIVED FEATURES FROM DATA

data_cat=data[cat_features]
data_cat.head()
data_cat.dtypes

import warnings
from warnings import filterwarnings#it remove warnings if any occur in jupyter notebook.
filterwarnings('ignore')

data_cat['reservation_status_date']=pd.to_datetime(data_cat['reservation_status_date'])

data_cat['year']=data_cat['reservation_status_date'].dt.year
data_cat['month']=data_cat['reservation_status_date'].dt.month #the date was given in mm/dd//yy so now it will give year ,month and day separetely.
data_cat['day']=data_cat['reservation_status_date'].dt.day
data_cat.head()

data_cat.drop('reservation_status_date',axis=1,inplace=True)#it will dropp reservation_status_date beacuse beacuse date we fetch separately by year month and day.

data_cat['cancellation']=data['is_canceled']#it will add new columnn.
data_cat

##APPLY FEATURE ENCODING ON DATA BEACUSE MACHINE LEARNING DOESNT UNDERSTAND THE STRING DATA SO WE ENCODE THE STRING DATA INTO INTEGER DATA
data_cat['market_segment'].unique()
cols=data_cat.columns[0:8] 
data_cat.groupby(['hotel'])['cancellation'].mean()
for col in cols:
    print(data_cat.groupby([col])['cancellation'].mean())
for col in cols:
    print(data_cat.groupby([col])['cancellation'].mean().to_dict())#dictionary maps the data easily.
    
for col in cols:
    dict=data_cat.groupby([col])['cancellation'].mean().to_dict()
    data_cat[col]=data_cat[col].map(dict)

data_cat.head()

dataframe=pd.concat([data_cat,data[num_features]],axis=1)    

dataframe.head()

dataframe.drop('cancellation',axis=1,inplace=True)
dataframe.shape

###HOW TO HANDLE OUTLIERS:-the data which is too much far away from real world for eg there is 100 person age and my 100th person age is 700 then 100th person  is outlier beacuse
                                               ### the age=700 cant possible
    
dataframe.head()
sns.distplot(dataframe['lead_time'])#we can see that most values between 0 to 200 and less values between 600 to 800 so this is outlier and we need to handle this outlier.

import numpy as np
def handle_outlier(col):#handle the outlier
    dataframe[col]=np.log1p(dataframe[col])
 
handle_outlier('lead_time')
sns.distplot(dataframe['lead_time'])
sns.distplot(dataframe['adr'])
handle_outlier('adr')
sns.distplot(dataframe['adr'].dropna())

###APPLY TECHNIQUES OF FEATURES IMPORTANCE ON DATA TO SELECT MOST IMPORTANT FEATURES.

dataframe.isnull().sum()
dataframe.dropna(inplace=True)
y=dataframe['is_canceled']
x=dataframe.drop('is_canceled',axis=1)

from sklearn.linear_model import Lasso
from sklearn .feature_selection import SelectFromModel 

feature_sel_model=SelectFromModel(Lasso(alpha=0.005,random_state=0))

feature_sel_model.fit(x,y)
feature_sel_model.get_support()

cols=x.columns
selected_feat=cols[feature_sel_model.get_support()]
print('total_features {}'.format(x.shape[1]))
print('selected_features {}'.format(len(selected_feat)))
selected_feat
x=x[selected_feat]
'''
###Logistic regrssion:-classification algorithm.In our poject password will be 3 classes ie.0,1,2 
###Linear Regression:-we draw a straight line in such a way that the actual distance between my original point and predicted point will be minimum.
##notation of Lineaer regression:- y=mx+c 
                                   y=theta 0+theta 1.x
                                   y=beta 0+beta 1.x
                                   y=w transpose.x+b
                                   
DRAWBECKS OF LINEAR REGRESSION:-
                                    1.deviated by outliers.
                                    2.most of the time i am getting probability>1&<0 ,here my linear regression get stuck.
                                    
So logistic regression comes in picture.It uses sigmoid function that means convert best fit straight line into s shape curve.

Logistic regression is used to classify those data points whose classes are linearly separable.

Linearly separable:- when we do separation by using straight line the difference between data points and plane is lineary separable
 which is y=w transpose.x+b and if our line starts from origin then b=0 according to linear algebra the distance is nothing but w transpose.x+b/|W| and if w is unit vector and
 line is coming from origin ie b=0 then distance between datapoints and plane ie(y)=w transpose.x
 
 w transpose x is nothing but the distance between datapoints and specific plane.
 
 If there is multiple data points then distance = summation from i=1 to n wi transpose.xi
 
 if the all datapoints are above the specific plane then distance will always +ve. and gives -ve below the plane.
 
 CASES INN LOGISTIC REGRESSION:-
                                +ve data points,y=+1 and -ve data points,y=-1 if data point is above lineary separable line thn +ve otherwise -ve.
                                case1:-y>0 and w transpose.x>0 and product of these two is also +ve then correct classification.
                                case2:-y<0(-ve) and w transpose.x<0(-ve) but product of these two is +ve then correct classification.
                                case3:-y<0(-ve) and w transpose.x>0(+ve) so product of these two is -ve then incorrect classification.
                                case4:-> y=+1 and   w transpose.x<(-ve) and product of these two is -ve then incorrect classification.

there can be more than one best fit line for linearly separable then only that line will consider which has maximum optimizer and it can be calculated as 
summation of i=1 to n .yi* wiT(wi transpose).xi


                                   y=mx+c 
                                   y=theta 0+theta 1.x
                                   y=beta 0+beta 1.x
                                   y=w transpose.x+b and if our line starts from origin then b=0.
                                   
If any fluctuation is coming by the outlier(datapoint which is far from the other one) then sigmoid function is used sigmoid function convert the large value between 0 and 1.
 sigmoid function f=1/1+e^z  
 
 CROSS VALIDATION:- if there is any usecase like regression,classification then first split the data by using function teain_test_split(independent variable(x),dependent variable(y)),random_state)
 train_test_split will give the four parameters as (x_train,x_test),(y_train,y_test) and my data points in this 4 parameters always varies when random_state will also vary.
 for eg training data is 75% and testing data is 25% when random_state is 0.and it will vary when random_state vary.
 And when training data,testing data willm change then my accuraacy of ml will also change.So to get rid of these or overcome these problem we have cross validation.
                                                                                                    |        |       |       |       |
 for eg when cv=5 then in first iteration 80% data is traing and 20%data is testing                     20        20     20      20   |  20  find accuraacy a1
                  then in 2nd iteration 60% data goes for traing and 20% data goes for testing          20         20    20   | 20            find accuraacy a2
                  then in 3rd iteration 40% data goes for traing and 20% data goes for testing           20        20  | 20                   find accuraacy a3
                  then in 4th iteration 20% data goes for traing and 20% data goes for testing           20      | 20                          find accuraacy a4
                  hen in 5th iteration 20% data goes for traing                                          20                                       find accuraacy a5
                  then we find the mean of all accuracy and that willl our final accuracy.
                  
CROSS VALIDATION APPROACHES:-
HYPER PARAMETER OPTIMIZATION HYPERTUNIC:-for eg. i implemented random forest ml algorith for my data or dataframe so for this there will be class available in our sklearn module
like random forest regression class or random forest classifier class so if we want to train our module then our module will train by default parameter which is present in these class 
but there is acase that values for this default parameter cannot fit in ml module  so to achive the best fit values of default parameters (hyper parameters) we have grid search cv and randomise 
search cv.
GRID SEARCH CV:-In this we take a duictionary and in that,we take a group of vslues for every default parameter  for eg.
dict={'n_estimators'=[100,200,300,1000]
       'max_features=['auto','logo2','sqrt']
       'max_depth'=[2,4,10]
 then we will appply functons gridSearchCV(....,dict,cv=5)   then we will take  all permutation and combinations. and find the best one which has highest accuracy like (100,logo2,4) is giving 
 90% which is highest accuracy and this default parameter combination is given to our ml module.
 so the purpose of gridSearchCV is to find best model and best default parameters.
 
 RANDOMSEARCHCV:-in this we pick up the random values of default parameters and find accuracy and which accuracy is highjest we consider that group or combination of parameters.

RANDOMSEARCHCV is greater then GRIDSEARCHCV  beacuse if dictionary has large group of values then its permutation and combination is difficult. and less time consuming.

'''
#APPLYING MACHINE LEARNING ALGORITHM 
#CROSS VALIDATE YOUR MODEL.
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)
y_pred
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)
from sklearn.model_selection import cross_val_score
score=cross_val_score(logreg,x,y,cv=10)
score.mean()
'''
DECISION TREE ALGORITHM:- Decision tree is extinsively used in classification where data are present in classes.it is little bit use in regression also.
it is a base algorithm which is used in every assemble technology like randm forest,xgboost in which collection of decision tree algo or it is used in bunch
this algorithm is nothing but just take decision like if time<9 then i will not go for a party otherwise will check for money if money ==yes then will go for a party.
 will go and enjoy. time and money are my data beacuse i am taking decision on 
the basis of it.
we can take usecase like:-
                        time    money   decision  for going party
                        12      y       y
                        10      n       n
                        9       n       n
                        8       y       n
In decision tree we make the tree of our data in above case time<9 is my root node like this    time<9
                                                                                                   /  \
                                                                                                   no  yes
                                                                                                   /    \
                                                                                               money    dont money
                                                                                               /           \
                                                                                               yes          no
                                                                                               
TERMINOLOGIES IN DECISION TREE:-
PRE-PRUNING & POST-PRUNING:-WHEN there is overfitting situation in decision tree then we use this term. for eg. when traing our data and and accuracy is 90% but while
doing testing or prediction our accuracy goes down to60%.it is overfitting condition.

ENTROPY/INFORMATION GAIN:-Randomness in your data or how random your data is or probability of occurence of data in a certain or give impurity insiide data.
 impurity is nothing but we take one basket and this basket all fruits are apple then impurity is 0.and if we have different different fruits like orange apple bananas then
 impurity=3.
 Entropy e=-pi log2 pi =[-p log2 p + q log2 q ] where q=1-p

HOW TO FIND ROOT NODE:-
                        if there are 3 independent variable our use case ie x,y,z then we willl find entropy Ex,Ey,Ez.After that we will find information gain igx,igy,igz
                        and whosoever feature or variable has maximum information gain that variable is my root node. for eg. z is my root node.
                        
 Let us we take one example.                            X 
        x   y   z   class       x   class              / \                  >1 probability of occurence of class one when value of x is 1 ie. 2/3 beaacuse 2 times x=1 when class=1 and total no. of x=3.
        1   1   1   1           1   1                 1   0              X>1>2 probability of occurence of class 2  when value of x is 1  ie.1/3
        1   1   0   1           1   1                / \  / \             >0>1 probability of occurence of class one when value of x is 0 ie.0/1.
        0   0   1   2           0   2               1  2  1  2              >2  probability of occurence of class 2 when value of x is 0  ie.1/1.
        1   0   0   2           1   2
Total entropy ie.Ex=[-2/3 log2/3+-1/3 log1/3] when x=1 for both the classes. ie.0.28
                 entropy =0 when x=0 for both the classes.
                 Like this we will find entropy of y and z also.
                 
Information gain:-it is nothing but which entropy feature has highest value or gain that feature will comsider as a parent node.
                Info gain(g)=1-(E Sn/S. Ei)   E=summation  Ei=Entropy of x=1 and entropy of x=0.    S=total datapoints in X.   Sn=Out of total data points,how many of all 1's or all 0's.

igx=1-[(3/4*0.28)+(1/4*0)   3/4=no. of 1's/total data points.* entropy when x=1 + no.of 0's /entropy whn x=0. ie.0.79
igy=1-[(2/4*0)+(2/4*0)]=1    igz=1-[(2/4*1)+(2/4*1)=0.

Decision tree =   y
                /  \
                1   0
        x  z  c     x z c 
        1  1 1      0 1 2
        1  0 1      1 0 2     #now we again perform entropy and information gain to find next parent node and further again and again.

BUILDING A DECISION TREE USING GINI INDEX(GI):-
for eg we have use case in which columns are class gender stay in hostel in which class are 8,9,10,11 and gender m,f stay in hostel yes or no.

class   stay in hostel  count   p(yes)  p(no)
8       yes=2,no=1      3       2/3     1/3
9       yes=2,no=1      3       2/3     1/3
10      yes=1,no=3      4       1/4     3/4
11      yes=3,no=1      4       3/4     1/4

GINI INDEX(GI)=class=8=1-[p(yes)^2 + p(no)^2]=4/9
                class=9=    4/9
                cllass=10   6/16
                class=11    6/16
                
 Gini of entire class =(no. of instance of class8/total instances )*G(class=8)+(no. of instance of class9/total instances )*G(class=9)+for class 10 and 11 also
 3/14*4/9+3/14*4/9+4/14*6/16+4/14*6/16=0.404
 now we apply whole procedure for gender as well as stay in hostel.also.
 For gender:-create table>>then find gini of every gender>>find ini of entire gender.=0.4822
 we can observe that gini of class is smaller then gender so our root node is class.
 
 POST PRUNING /Backward pruni:-if we want to get rid from overfitting situation then we use this.
 In this decision tree is generated first and after that they check for overfitting situation (testing accuracy is decreasing with respect to testing ) then
 removes the usless braches by experimenting some cross validation approach like randomise search cv or grid cv.Basically it take care of depth and height of tree.
 
Pre-pruning/forward pruning:-In this before building decision tree first we do cv >>random/grid>>best parameters>>best model>>best decision tree>>training/testing.
 
Different algorithms for decision tree:-
****ITERATIVE DIGTOMISER3(ID3):-It is basically for classification type of usecases. it uses the concept of info gain to make decision tree.it always works on the term of catorigal attributes..

****C 4.5 :- extension of ID3  which works on continuous as well as discrete data. or numerical or categorigal data.It uses gini index to find our root node.

****CART(CLASSIFICATION AND REGRESSION TREES):-In this we use gini index to find root node and we can modify data also and can use entropy also.

**C 5.0:-It is much better than C 4.5.it works with catorigal target variable use label like yes and no.

MARS:-MULVARIANT ADAPTIVE REGRESSIVE SPLINE.it always create series of peer wise linear model.which is used to modulate irregularity and interaction among variable.

DECISION STUMP:-It is used to create a single level decision tree.

**M5:- when we have small dataset or noise or outlier is present in our dataset then we use it.
CIT(CONDITION INFLUENCE TREE.)
CHAD(chai square automatic interaction detection):-it works on statistical data like ch-square.

ADVANTAGES:-it is used in classification as weell as regression.
            easy to learn and use beacuse we need to learn only entropy and gini index in this.
            we dont have to deal with outlier beacuse it works on rule based things.
            no need to perform scaling and normalization.
            
Disadvantages:-if we want to make small changes in training data then unstability occur beacuse node will shift from one place to anotheer.
                probability of overfitting is very high so we need pruning.
                it take more time to train decision model.
                
HOW DECISION TREE WORKS IN CASE OF REGRESSION :-

x1      x2      x3      target
4       100     70      0.1
5       10      80      0.2     
6       40      90      0.9
my new data is 5 200 21 and we have to  predict this target feature by using decision tree using regression.
5       200     21      0.8

#so we can assume x1 data is within rangge of 4-10 x2 is range in 1-500 x3 is range in 1-100. so we will split our data.        x2--300-500                                                                                                                            /|  
 X1 :-(1-5),(6-10)  X2:-(1-100,100-300,300-500)  X3:-(1-30,30-60,60-100)                                                       1-100 100-300
i have to predict when x1=5 x2=200 x3=21 so x1 in range of (1-5) so we will find average of it and give name y1 x2 is in range of (100-300) so find average of it y2 and y3= avg of (1-30)
then we will find the mean ie. y1+y2+y3/3 and this is my final prediction.
how to select a region like 1-5,100-300,1-30 so we have select region in such a way that sum of squares of errors or residuals is less or minimum.. error=predicted-actual value.

So to minimize this error we use gradient descent approach in linear regression.

RANDOM FOREST ALGORITHM:-this algorithm is used in classification as well as in regression.In sklearn library there is randomforest classifier and random forest regressor class is used.
RANDOM FOREST is nothing but follow ensemble learning approach. and it is collection of multiple decision  trees.

ENSEMBLE LEARNING APPROACH:-it is nothing but learns from multiple models and at the end it will combine all the learning.

Random forest is a collection of multiple decision tree and the and decision tree built in this is known as bagging or bootstrap aggregation.

bagging or bootstrap aggregation is nothing but create a multiple bags or desion tree and give prediction as 0 or 1 fo eg. bag1 give prediction 0 bag2 give 1 bag3 give 0 then
and which has majority for eg.0 then it will consider simply will do aggregation and and return majority.
 for eg there is a dataset of 600 rows and 9 columns then in random forest we take out random sample like 200 rows and 3 columns by using row sampling and column sampling and
 perform decision tree on it by using classification or regression for eg. if use regression then discrete prediction will give as 0/1 amd in classification conntinuous prediction 
 will give like 10.11. then this random sample again goes to the datta set and again random sample will pick out and perform decision tree. and we will do multiple times.

Desion tree has high variance which means prediction data is and actual data has very high difference. so we use random forest to convert high variance into the low variance.but how:-
beacuse in random forest we use multiple decision tree and every decision tree works or trained on specific data of dataset so it become expert. so atlast random forest have low variance. 

So if we use regression in random forest then we take mean of all decision tree. and in case of classification random forest we take majority of 0's or 1's.

KNN(K-NEAREST NEIGHBOUR) ALGORITHM:-it is also used for classification as well as for regression.it is not used for huge data beacuse it take more time in computaton.

k=no. of nearest neighbours of particular datapoints. and we can find this k by using cross validaion techniques like randomise search cv and grid search cv.

For eg.if we have two type of data points ie.data points of class 1 and class 2 and now we have new data point and wants to find out that new data point belongs to class 1 or 2
then we will take random value of k ie3 k=3 means now we have to take 3 nearest neighbour datapoints of new data point but how will we find that which 3 datapoints are nearest
datapoints of new datapoints. then we will apply concept of distance to find 3 nearest data points. we will find the distance of every data points from new data points
lest us assume that new data point has coordinates as (x1,y1) and other data point as (x2,y2) then we will apply distance formula of euclidian distance==root of[(x2-x1)^2 + (y2-y1)^2]
and which datapoint has minimum distance from new data point that data point will consider as nearest data point to new datapoint. 

Sometime we can use manhattan distance instead of euclidian distance to find nearest neighbour which is nothing but absolute distance. and use when we have not the distance is straight 
 and distance is in curve line or my distance is passing from multiple corordinate like X1,X2,X3 
 
 X-------------------y :-euclidian distance will find to get distance from X to y.
 \          /
  \      /
  \    /               :-we will find manhatan distance to find distance between x to y beacuse is not going directly from x to y it is going X-->a && a-->>y-axis
  \  /                      manhattan distance  is nothing but summation of all vector. 
  \
   a

We applied k nearest neighbour and found that 2 datapoints of class 1 and 1 datapoints of class 2 is nearest to new datapoint then we will find the probability of new data points with respect to both classes 

So the probability of class 1=2/3 and class 2= 1/3. 

so we can observe with the probability that new datapoint belong to class 1.

KNN is also known as lazy learner algo beacue like other algo it doesnt give relationship among data until or unless first it dont have testing data.
knn never try to bulit model,it only find out the distance of new data and on the basis of new data it give prediction like this new data belongs to which class.
So we can say that in knn,our whole dataset is model and and when huge dataset then huge model and take more time so dont use in huge dataset.

HOW TO COMPUTE DISTANCE BETWEEN CATEGORICAL DATA :-BY USING HAMMING DISTANCE.:-summation of all 1's and x is not equal to y.

        (a  b   c   d) 
        (a  e   d   f)
        (0  1   1   1) so hamming distance= summation of all 1's ie.3
        
We take one example of knn using hamming distance:-

class 1                 class2
a b c d                 x y z a    Now we want to find that xacd belongs to which class whwn k=3.Beacuse we have catorigal data so we will find hamming distance.
x a c d                 x a c d
1 1 0 0                 0 1 1 1 

a b c e                 x y b a    then we simply do hamming of every catorigal data of class 1 and class 2 with find catorigal data xacd.
x a c d                 x a c d
1 1 0 1                 0 1 1 1
 
a b d e                 x y c a
x a c d                 x a c d
1 1 1 1                 0 1 0 1

a b c e                 x y z a 
x a c d                 x a c d
1 1 0 1                 0 1 1 1 

class1 1's are=2,3,4,3 and class2= 3,3,2,2 and we can see that xacd has 2 nearest neighbour of class 2 so xacd belong to class 2.

KNN system is highly used in recommended system.

Advantagges of knn:- it is used as classification as well as regression. so when we used regression then we take mean.
mathematics behind this algorithm is easy. and easy to use and implement. not take more time in training time.

Disadvantages.:-huge data not used.take more time in prediction or testing data. 
'''
#APPLYING MULTIPLE ALGORITHM ON DATA AND CHECK IT ACCURACY.

from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

models=[]

models.append(('LogisticRegression',LogisticRegression()))
models.append(('NaiveBayes',GaussianNB()))
models.append(('RandomForest',RandomForestClassifier()))
models.append(('DecisionTree',DecisionTreeClassifier()))
models.append(('KNN',KNeighborsClassifier()))

for name,model in models:
    print(name)
    model.fit(X_train,y_train)
    
    predictions=model.predict(X_test)
    
    from sklearn.metrics import confusion_matrix
    print(confusion_matrix(predictions,y_test))
    print('\n')
    
    print(accuracy_score(predictions,y_test))
    print('\n')






 
















































































