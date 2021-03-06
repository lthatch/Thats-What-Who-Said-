# That's What Who Said?

![image](./flask_app/static/images/Dunder_Mifflin,_Inc_Long.jpg)


## The inspiration for this project- The Office TV Show

I am an Office fanatic! I love all the characters and the crazy situations they find themselves in. I would be embarrassed to say how many hours I have watched, but with that time, I feel as if I can quote just about any character from any noteworthy scene.

## Project Goal

The goal of this project is to build a model that would take input text from a user and identify a character from The Office who would most likely say those words.

![foxdemo](https://www.sunyocc.edu/sites/default/files/styles/full_width_1228_/public/images/migrated/2018/12/top-of-story-michael-scott-image.jpg)

## EDA

![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-12%20at%2011.54.34%20AM.png)
![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-12%20at%2011.54.54%20AM.png)
![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-12%20at%2011.55.15%20AM.png)
![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-12%20at%2011.56.02%20AM.png)
Words used leading up to a "That's what she said" joke.



## Preparing the Data

- I limited the amount of classes/characters down to the top 20 speakers
- Using a TfidfVectorizor, I removed stop words and transformed the text into a weighted matrix of numbers
- Once in numeric form, I performed a train, test split and my data was ready to be fed into a model

## Selecting and Training a Model

I decided to use scikit learn’s ComplementNB model because of the imbalances in my data.

Hold out data accuracy: .24

Random guessing expected 
accuracy: .05

![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-12%20at%202.47.15%20PM.png)
![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-13%20at%2012.21.56%20PM.png)


## Limiting the Number of Classes

In an effort to improve my accuracy I decided to limit the number of classes the model needed to predict. I chose the top 4 speakers

Hold out data accuracy: .41

Random guessing expected 
accuracy: .25

![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-13%20at%2012.20.46%20PM.png)
![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-13%20at%2012.21.10%20PM.png)

## Fine-tuning the model

After seeing my accuracy increase I decided to add in 3 more characters. In addition to increasing the number of classifications, I tuned the model using sklearn’s Randomized SearchCV

Hold out data accuracy: .33

Random guessing expected 
accuracy: .14

![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-12%20at%203.04.10%20PM.png)
![foxdemo](https://github.com/lthatch/Thats-What-Who-Said-/blob/main/images/Screen%20Shot%202021-01-13%20at%2012.22.25%20PM.png)

## Conclusion

The results were mostly as expected.

Next steps: Expanding this project into creating a chat bot in order to chat with your favorite characters!


