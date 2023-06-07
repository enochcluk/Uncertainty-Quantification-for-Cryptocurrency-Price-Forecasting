# Uncertainty Quantification for Cryptocurrency Price Forecasting 
 Applied UQ to obtain robust confidence intervals for short-term cryptocurrency price forecasts by comparing the prediction and confidence interval (CI) of AutoRegressive Integrated Moving Average (ARIMA) with Bayesian Neural Networks (BNN), calibrated using conformal prediction.
## Introduction
- UQ helps quantify and manage inherent uncertainties in financial models and data
- Cryptocurrency markets are highly volatile 
- Predicting price movements and managing risk is particularly challenging for short-term cryptocurrency data
- Many ML/UQ studies on stock markets, but few studies on cryptocurrency markets 
- Goal: Apply UQ to highly volatile cryptocurrency price forecasts to obtain robust confidence intervals 
- Idea: Compare the prediction and CI of ARIMA with BNN after calibrating CI using conformal prediction

## Methods
- **Dataset:** Bitcoin tether order book data (millisecond bid/ask prices and volumes) collected from June to September 2021
- Compute open, close, low, and high prices for ten-minute intervals
- Train-test split: 70% train, 30% test 
- Predictive models used to predict next time step open price
- Traditional statistical method: ARIMA (AutoRegressive Integrated Moving Average)
- Newer ML based method: Bayesian Neural Networks (BNNs)
- Conformal Prediction using α = 0.1 
- Calibrate using first 1000 points of the test set
- Allows for comparison of model CI

## Evaluation
- Comparison of CI for both models after CP using various metrics
- **BNN**
  - Architecture
    - 14 neurons, two hidden layers (20 neurons), 1 neuron output layers
  - AutoDiagonalNormal guide
  - Adam optimizer with learning rate of 1e-3
  - Coverage
    - Before CP: 0.998
    - After CP: 0.847
- **ARIMA**
  - Best model found with auto ARIMA
  - ARIMA(0, 1, 0) (random walk), where ŷt = μ + yt - 1
  - Coverage
    - Before CP: 0.935 
    - After CP: 0.896

## Conclusion/Future Directions
- After CP, ARIMA model gives better confidence interval compared to BNN model under evaluation metrics
- Future directions
  - Investigate different ML models for price prediction
  - Incorporate price variance as one of the calibration parameters of the confidence interval
