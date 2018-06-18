# Fair-Tech-Collective
The code in this repositry are the scripts I wrote to do data analysis on Fair Tech's project on air pollution data in specific locations in the bay area: 

This README will list all the scripts and a short summary of what they do. The data used in this analysis can be acquired from the following places: 

Python Files 
Counts_of_pollutants_plot_4910, 4911, 4912, 4913, 4914.py:  These scripts were used to generate the following plots. One of the early plots we looked into during the project. 

Plotting_individual_pollutants_richmond.py: This script was used in creating plots for individual pollutants in Richmond. 

four_possibilities_richmond.py: This script was used to make counts for 4 possible scenarios explained in our report where a pollutant is detected at both refinery and community OR either one or the other or either nothing detected at all. 

R files 
Four_or_More_Pollutants.R: This script  written in R basically  helps calculate a relative frequency for when there is 1, 2, 3, 4.. up to the maximum 16 pollutants that are in the air at any point in time. After getting these frequencies, I basically put them into an excel sheet (available here: https://drive.google.com/open?id=1tW7MZxibUMo-RtLiLGyY013mnHTMpFM0bqE0CPkUXXI)- And I added up the 4 to the maximum amount of pollutants detected. 

barplotvisualizations_monthly.R: This script written in R was used to make bar plots showing monthly pollutant detects. 

Piechart_detections_monthly.R: This script was used to make piechart showing a breakdown of  pollutants detected at a particular  location monthly from 2016-2017

pm_25_black_carbon.R: This script was written to get the relative frequency of pm2.5 and black carbon in the air. 

For the analysis. All data used can be acquired here: 
https://drive.google.com/drive/folders/11vHLS1kqlDe7ocpaI3ClLc14Rz1CKtYc?usp=sharing

If you would like to pull your own data you can use the following links: 
1. Go to https://esdr.cmucreatelab.org/browse/ and select the data you want to view and right click and download as csv or json format.
2. Use curl from your terminal to pull the data. The script titled "" helps to pull data monthly OR You can go to https://github.com/CMU-CREATE-Lab/esdr/blob/master/HOW_TO.md to learn more about ESDR and how to use it. 
