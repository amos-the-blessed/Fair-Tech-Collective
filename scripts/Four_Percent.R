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


pollutants<-names(Loc_4910)
plot(Loc_4910$Realdate,Loc_4910[,pollutants[2]], xlab="Date", ylab="Reading PPB", main= paste("2016 Readings of Pollutants in the air for the Month of ",month[i]))
for(col in 2:length(pollutants)){
  points(Loc_4910$Realdate,Loc_4910[,pollutants[col]], col=3:length(pollutants), pch=1)
  
}


















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











library(anytime)
library(tidyverse)
#hello= list()
fileNames <- Sys.glob("/Users/amos/Google Drive/FairTech/Esdr_data_Location_monthly/4914/2017/*.csv")
for (fileName in fileNames) {
  #print("This is working")
  Loc_4910 <- read.csv(fileName, na.strings = c("foo", "bar"), stringsAsFactors=FALSE)
  Loc_4910$Realdate <- anytime(Loc_4910$EpochTime)
  Loc_4910$Counts <- rowSums (Loc_4910[1:16] == 0 )
  head (Loc_4910)
  freq <- table (Loc_4910$Counts)
  rel_freq <- (freq / NROW(Loc_4910$Counts)*100)
  old = options(digits=2) 
  print (fileName)
  print (cbind(rel_freq))
  #hello[fileName]= list(cbind(rel_freq))
  ##write.csv(hello, file = "test4.csv")
}





#Loc_4910$X3.feed_4910.Hydrogen_Sulfide = cleanFacts(Loc_4910$X3.feed_4910.Hydrogen_Sulfide) # simple
# do for many:
# ?apply
#apply(Loc_4910, 2, is.factor)

Loc_4910$Realdate <- anytime(Loc_4910$EpochTime)

Loc_4910$Counts <- rowSums (Loc_4910[1:6] > 0 )
head (Loc_4910)


freq <- table (Loc_4910$Counts)

rel_freq <- (freq / NROW(Loc_4910$Counts)*100)

old = options(digits=2) 

cbind(rel_freq) 

###############################################################################

Loc_4910$Ammonia_Counts <- rowSums (Loc_4910[2] > 0 )
Loc_4910$Black_Carbon_Counts <- rowSums (Loc_4910[3] > 0 )
Loc_4910$Ethylbenzene_Counts <- rowSums (Loc_4910[4] > 0 )
Loc_4910$Hydrogen_Sulfide_Counts <- rowSums (Loc_4910[5] > 0 )
Loc_4910$Methylpentane_Counts <- rowSums (Loc_4910[6] > 0 )
Loc_4910$N_Heptane_Counts <- rowSums (Loc_4910[7] > 0 )
Loc_4910$N_Hexane_Counts <- rowSums (Loc_4910[8] > 0 )
Loc_4910$N_Octane_Counts <- rowSums (Loc_4910[9] > 0 )
Loc_4910$PM_2_5_Counts <- rowSums (Loc_4910[10] > 0 )
Loc_4910$Toluene_Counts <- rowSums (Loc_4910[11] > 0 )
Loc_4910$a_Trimethylbenzene_Counts <- rowSums (Loc_4910[12] > 0 )
Loc_4910$b_Trimethylbenzene_Counts <- rowSums (Loc_4910[13] > 0 )
Loc_4910$c_Trimethylbenzene_Counts <- rowSums (Loc_4910[14] > 0 )
Loc_4910$d_Trimethylpentane_Counts <- rowSums (Loc_4910[15] > 0 )
Loc_4910$m_p_Xylene_Counts <- rowSums (Loc_4910[16] > 0 )
Loc_4910$o_Xylene_Counts <- rowSums (Loc_4910[17] > 0 )

################################################################################


#plot(x='Realdate', y='Ammonia_Counts' ,figsize=(12,8), grid=True, label="Action", color="red") 
#plot(x='Realdate', y='Black_Carbon_Counts' ,figsize=(12,8), grid=True, label="Action", color="red") 

Loc_4910$test.melt <- melt(Loc_4910$Realdate, measure.vars=c('Ammonia_Counts','Black_Carbon_Counts','Ethylbenzene_Counts','Hydrogen_Sulfide_Counts','Methylpentane_Counts','N_Heptane_Counts','N_Hexane_Counts','PM_2_5_Counts','Toluene_Counts','a_Trimethylbenzene_Counts','b_Trimethylbenzene_Counts','c_Trimethylbenzene_Counts','d_Trimethylpentane_Counts','m_p_Xylene_Counts','o_Xylene_Counts'))

Loc_4910$test.melt <- na.omit(Loc_4910$test.melt)
Loc_4910$test.melt.ggplot<-ggplot(Loc_4910$test.melt)

Loc_4910$test.melt.ggplot + geom_line(aes(colour = variable)) 
+ scale_colour_discrete("Pattern") 
+geom_point(aes(x,y), size=1,shape="o") 
+ xlab("Date")
+ ylab("Counts")


################################################################################

png("C:/Users/aoa53/Downloads/October_2016.png")
qplot (Realdate, Counts, data = Loc_4910)+ scale_y_continuous(breaks=c(1,2,3,4,5,6,7,8,9,10,11, 12,13,14,15,16,17))
print(October_2016)
dev.off()

ggplot(Loc_4910, aes(x = Counts)) +
  geom_dotplot()
############################################################################################







# full_data = NULL

# for(x in 1:length(list.files())){ --> iterate through an integer from 1 to the number of files
# ... some functions here:

## temp = read.csv(list.files()[x]) --> select the specific file number x

## full_data = rbind(full_data , temp) 

## }
#cleanData = function(column){
  
 # if(is.factor(column) == FALSE){
    
#    print("Isn't a factor")
 #   return(column)
  #} else {
    
   # print("factor found, processing")
    #column = as.character(column)
    #olumn = as.numeric(column)
    #return(column)
  #}
  
#}

