# Analyzer
## Link to the web-app ->
https://analyzer-nlp.herokuapp.com/

## Description ->
##### .> NLP based web-app to help users save time of reading long tedious text movie reviews by converting them to singular sentiment.Moreover it avoids any kind of spoiler. So, movie lovers get your hands over it.
##### .> The model was trained over IMDB dataset available on kaggle.
##### .> After performing all types of data cleaing and pre-processing the clean data was feeded to different models.
##### .> Logistic Regression was found to be the best performer with 89.24% accuracy. The confusion matrix out of 10000 data was as follows :
#####         [[4345    616]
#####            [ 460   4579]]
##### .>
##### .> Another feature is hate speech/text detection. A user can also use this as an API for his/her web/mobile app

### How To Get Started ?
#### .> Go to the site.(Link above)
#### .> Next, route to the movie analysis(https://analyzer-nlp.herokuapp.com/imdb). Click on the input field , enter/paste the movie review and hit analyze. Brovo!! You did it 
#### .> Next, route to the hate analysis(https://analyzer-nlp.herokuapp.com/hate). Click on the input field , enter/paste the hate speech/text and hit analyze. Brovo!! You did it 


## See the NLP Model code ->
#### .> https://github.com/Asutosh-panda/Analyzer/blob/main/imdb_sentiment/app/mlModel/ 

## Checkout the HTML Template ->
#### .> https://github.com/Asutosh-panda/Analyzer/blob/main/imdb_sentiment/app/template/

## Checkout the routes.py ->
#### .> https://github.com/Asutosh-panda/Analyzer/blob/main/imdb_sentiment/app/urls.py

## Checkout the views.py ->
#### .>https://github.com/Asutosh-panda/Analyzer/blob/main/imdb_sentiment/app/views.py

