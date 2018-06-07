#PIE CHART MAKING 
library(anytime)
library(tidyverse)
library(ggplot2)

fileNames <- Sys.glob("/Users/amos/Google Drive/FairTech/Esdr_data_Location_monthly/4910/2017/*.csv")
i<-0

for (fileName in fileNames) {
  i<-i+1
  Loc_4910 <- read.csv(fileName, na.strings = c("foo", "bar"), stringsAsFactors=FALSE)
  columnNames <- names(Loc_4910)
  slices<- colSums(Loc_4910[2:17] > 0)
  #print ("yes")
  month= list("April","August","December","February","January","July","June","March","May","November","October","September")
  colors = c("red4", "yellow", "green", "violet", "orange", "blue", "pink", "cyan", "antiquewhite3","burlywood4","coral1","gold","firebrick4","darkorchid","darkolivegreen1","gray")
  png(paste("491_",month[i],"_2017",".png",sep=""))
  pie(slices, main ="", labels= "", edges = 100, radius = 0.6,
      density = NULL, angle = 45, col = colors, border = NULL)
  dev.off()
  
}

