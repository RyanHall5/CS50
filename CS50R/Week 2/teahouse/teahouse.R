
#creating tea data table
tea_recs <- data.frame(
  Light = c("Green", "Chamomile"),
  Bold = c("Black", "Rooibos")
)


#setting empty initial values
flavor <- ""
caffeine <- ""


#getting flavor preference
while (flavor != "Light" && flavor != "Bold"){
  flavor <- readline("Enter your flavor preference: (Light or Bold)")
}


#getting caffeine preference
while (caffeine != "Yes" && caffeine != "No"){
  caffeine <- readline("Enter your caffeine preference: (Yes or No)")
}


#converting caffeine from string to index
caffeine <- ifelse(caffeine == "Yes", 1, 2)


#displaying recommendation
print(paste("You should try", tea_recs[caffeine,flavor], "tea"))

