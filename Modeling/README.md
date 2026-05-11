# Bone Age Prediction Model
Building a Deep Learning Regression model which predicts the age of a person for the X-ray scan of his hand.


### Preprocessing
* rescaling the image values to [0, 1]
* converting the images into gray scale since colors doesn't have significant meaning in X-ray images.
* resizing the images to 256x256

### Model
* developed a model similar to VGGnet model, loss function was MSE, tried different optimizers and altered the architecture of the model multiple times.
![First Trials](model_development/first_trials.png)
* tried a pre-trained model and compared it with the custome one
![Xception vs Custom](model_development/xception_vs_costum.png)
* this was the best model I reached before the deadline
![Best Model](model_development/best.png)

### Evaluation
* Best MSE: 30.419 and Validation MSE: 36.53
![Loss](model_development/mse.png)
* Best MAE: 4.316 and Validation MAE: 4.864
![MAE](model_development/mae.png)
* Variance
![Variance](model_development/variance.png)
