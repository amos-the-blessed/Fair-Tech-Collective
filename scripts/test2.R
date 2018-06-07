#PIE CHART MAKING 
library(anytime)
library(tidyverse)
library(ggplot2)
library(ggrepel)

fileNames <- Sys.glob("/Users/amos/Google Drive/FairTech/Esdr_data_Location_monthly/4910/2016/*.csv")
i<-0
pdf("abcde.pdf")
for (fileName in fileNames) {
  i<-i+1
  Loc_4910 <- read.csv(fileName, na.strings = c("foo", "bar"), stringsAsFactors=FALSE)
  columnNames <- names(Loc_4910)
  slices<- colSums(Loc_4910[2:17] > 0)
  labels<- names(slices)
  myvalues <- as.numeric(slices)
  newdf = tibble(labels, myvalues)
  newdf$labels = as.factor(newdf$labels)
   #print ("yes")
  month= list("April","August","December","February","January","July","June","March","May","November","October","September")
  ggplot(newdf, aes(x = "",  y = myvalues, fill = labels))+
         geom_bar(width = 1, stat = 'identity')+
         coord_polar(theta = "y", start=0)+
         theme(axis.title = element_blank())
  
}

dev.off()


