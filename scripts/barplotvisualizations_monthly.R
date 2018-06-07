setwd("~/Documents/myFairTech")
library(anytime)
library(tidyverse)
library(ggplot2)

fileNames <- Sys.glob("/Users/amos/Google Drive/FairTech/Esdr_data_Location_monthly/4910/2016/*.csv")
i<-0
pdf("4910_vsuals.pdf")
for (fileName in fileNames) {
  #print("This is working")
  Loc_4910 <- read.csv(fileName, na.strings = c("foo", "bar"), stringsAsFactors=FALSE)
  Loc_4910$Realdate <- anytime(Loc_4910$EpochTime)
  Loc_4910$Counts <- rowSums (Loc_4910[2:17] > 0 )
  head (Loc_4910)
  freq <- table (Loc_4910$Counts)
  rel_freq <- (freq / NROW(Loc_4910$Counts)*100)
  old = options(digits=2) 
  #print (fileName)
  counts <- rel_freq
  i<-i+1
  #print("I worked")
  month= list("April","August","December","February","January","July","June","March","May","November","October","September")
  barplot(counts, width = 1, main= paste("Atchinson Village Community, ",month[i]," 2016"),
          col = NULL, border = par("fg"),
          xlab = "Number of Pollutants" , ylab = "Percent of Time",
          axes = TRUE, axisnames = TRUE, ylim = c( 0 , 50))
  plot(Loc_4910$Realdate,Loc_4910$Counts, xlab="Date", ylab="Counts",main= paste("2016 Counts of Pollutants in the air for the Month of ",month[i]))

  
  
  #hello[fileName]= list(cbind(rel_freq))
  ##write.csv(hello, file = "test4.csv")
}
dev.off()

