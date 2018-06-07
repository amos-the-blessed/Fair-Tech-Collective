library(anytime)
library(tidyverse)
library(psych)
library("xlsx")
library(reshape2)
hello= list()
fileNames <- Sys.glob("/Users/amos/Google Drive/FairTech/Esdr_data_Location_monthly/4914/2017/*.csv")
for (fileName in fileNames) {
  
  Loc_4910 <-read.csv(fileName,stringsAsFactors = TRUE)
  
  for(col in 1:length(names(Loc_4910))){
    Loc_4910[,col] = as.numeric(as.character(Loc_4910[,col]))
  }
  pmfix<-Loc_4910[!is.na(Loc_4910$X3.feed_4912.PM_2_5),]
  bcfix<-Loc_4910[!is.na(Loc_4910$X3.feed_4912.Black_Carbon),];
  #print(head(pmfix))
  columns_to_change=grep("PM_2_5", names(Loc_4910))
  columns_to_change=c(columns_to_change, grep("Black_Carbon", names(Loc_4910)))
  print(fileName)
  #print(head(Loc_4910))
  pm25<-describe(Loc_4910[,columns_to_change[1]])
  bcstuff<-describe(Loc_4910[,columns_to_change[2]])
  print(pm25)
  print(bcstuff)
  # Write the first data set in a new workbook
  #write.xlsx(fileName,pm25,bcstuff, file = "datastuff", sheetName = "4910_2016", append = FALSE)
  
  #print("This is working")
  #print(head (Loc_4910))
  #print(describe(pmfix))
  #print(describe(bcfix))
  
}
