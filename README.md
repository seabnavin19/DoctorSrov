# Rice Disease Classification
## Table Content
1. [Inspiration](#ov)
2. [What it does](#to)
3. [How we built it](#pro)
4. [Final Product](#fin)
5. [Demo](#demo)
<a name="ov"></a>
## 1. Inspiration

Agriculture is one of the most importance sector in cambodia, because we have a potential weather, geography, etc.Base on research around 80% of people in cambodia they are farmers but they are not expert in planting and do farming yet that's why farmer can not make profit as they want. Another thing disease, natural disaster cause a lot of lost for cambodian farmers. 
Alot of disease in agriculture product especially rice, most of the rice disease was started from a small spot in the leaf that's why it is very difficult for farmer to tackle this in the early stage. That's why we built a system that allow farmers to tackle the rice disease from the early stage that will be prevent lost of the rice production.
<a name="to"></a>
## 2. What it Does
Our system we combine backend AI technology with Android and Web application which mean with a mobile app farmers can scan the specific area of rice leaf then our Deep learning model will classify the diesease of the rice and it will provide the solution in khmer language also video explaination of each diesease.
### Customer Journey
![Image](https://raw.githubusercontent.com/seabnavin19/Rice_Disease_Detection/main/Screenshot%20from%202021-09-02%2008-05-08.png)

<a name="pro"></a>
## 3. How We built That
Our application is not a stand alone application but it build that combine with many components include :
- Rice Disease classification model
- Rice Disease classification API and Server
- Rice Disease classification mobile app
- Rice disease classification Webapp

So I will give you a brief detail on how we build its components and how we integrate those components to get our final system.

#### Rice Disease Classification model
 Normally to build a AI model we have some importance steps in Data science life cycle:
 - Data collection : In the first phase we get the data from online platforms like Kaggle that have the image of each rice disease. So it will be easy for us when we first start the project, But the near future we want to improve our product. We want our app to really fit the disease in Cambodia and we want our app to be more customized so we will collect our own datasets from the Cambodia rice field.
 
Link for Kaggle dataset:  https://www.kaggle.com/shayanriyaz/riceleafs

 - Data cleaning and feature engineering:  As we have limited datasets for training so data cleaning and feature engineering is very important in feature engineering we did some importance things like data augmentation, which mean we generate new data set from our existing images by adding some noise, rotation,zoom, etc so it not just give us more datasets but it also make our model more generalize and avoid overfitting.

![image](https://raw.githubusercontent.com/seabnavin19/Rice_Disease_Detection/main/images%20(2).jpeg) | ![image](https://raw.githubusercontent.com/seabnavin19/Rice_Disease_Detection/main/images%20(2).jpeg)



<a name="fin"></a>
## 4. Final Product
![](/pic.png)
