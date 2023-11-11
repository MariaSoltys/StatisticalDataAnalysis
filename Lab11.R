library(Hmisc)

#data forming
data <- read.csv("C:/Users/Ciri/Desktop/Навчання/Economy_Indicators.csv", sep=",")
View(data)
#Graphical view
plot(data$Inflation.Rate, data$GDP, type = "p")
summary(data)
#Histogram
hist(data$Jobless.Rate)
# Просте ковзане середнє
require(smooth) 
sma(data$Jobless.Rate, h=3, silent=FALSE)
sma(data$Jobless.Rate, h=5, silent=FALSE)
sma(data$Jobless.Rate, h=7, silent=FALSE)
sma(data$Jobless.Rate, h=9, silent=FALSE)
sma(data$Jobless.Rate, h=11, silent=FALSE)

plot(data$Inflation.Rate, data$Jobless.Rate, type = "p")

#коефіцієнти кореляції
cor(data$Inflation.Rate, data$Jobless.Rate, method = 'kendall')
cor(data$Inflation.Rate, data$Jobless.Rate, method = 'pearson')
cor(data$Inflation.Rate, data$Jobless.Rate, method = 'spearman')

#кластерний аналіз
library(ggplot2)
library(dplyr)
Mdist <- dist(data$Inflation.Rate) 
hc <- hclust(Mdist, method = "single") 
hc
plot(hc) 
#2 кластери
plot(hc, cex = 0.6, main = "2 clusters") 
rect.hclust(hc, k = 2, border="red")
#4 кластери
plot(hc, cex = 0.6, main = "4 clusters")
rect.hclust(hc, k = 4, border="red")
#5 кластерів
plot(hc, cex = 0.6, main = "5 clusters") 
rect.hclust(hc, k = 5, border="red")