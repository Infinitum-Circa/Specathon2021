# TeamInfinitum_Circa-Krishi
# Specathon2021
## Problem Id - PSAR003 	
## Theme - Smart Agriculture & Rural Development 	
### Problem Statement- Apps for Climate monitoring and crop sowing. 	
#### Description 
Smart Apps that could give insights on Climate changes and helps monitoring yield minimizing losses to the maximum extent possible.
**Software requirements**: Python, Kivy, Turicreate, Scipy, tensorflow, scikit-learn
![Alt Text](https://github.com/Specathon2k21/TeamInfinitum_Circa-Krishi/blob/main/methodology.jpeg)
##### Working model and optimization​ :
All climate estimates will be made with data from the meteorological department of India
and the price estimate will be modelled as a simple linear regression problem and calculated.
The algorithm for prediction will be designed such that it balances the trade off between crops
that will endure better and crops that will sell more in that particular season. We take the six
indian seasons into consideration and will have a list of crops that are grown prelevantly in that
particular area and also subdivide them into sub categories based on temperature, water
requirement and soil health. The farmer is also provided with an option to choose a safety point
wherein he can safeguard his investment in both time and money.
Another important factor besides the climate would be the money invested by the farmer
in his crops. Based on the above factors such as temperature, water requirement, soil health,region etc the crops are chosen and n crops are assumed to be x1, x2....xn. The factors that
need to be estimated are money and space. We assume the farmer has S square feet of land,
then s1x1 + s2x2 + ... + snxn = S, and assuming selling prices to p1,p2,....,pn the function
p1x1+p2x2+...+pnxn = P will be maximized. Also, certain crops will have higher sustainability in
that particular season, and some may have low sustainability and to compensate for that, a
modified selling price is taken to be Probxp1, where Prob is the probability that the crop is
produced. The probability function here compasses the effect of climate, possible pest attack,
Soil nutrient values, chances of crop failure.
##### User Interface
![Alt Text](https://github.com/Specathon2k21/TeamInfinitum_Circa-Krishi/blob/main/Screenshot%20from%202021-01-29%2013-43-25.png)
