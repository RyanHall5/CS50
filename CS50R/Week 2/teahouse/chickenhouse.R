
#creating chicken data table
chicken_recs <- data.frame(
  Mild = c("Honey Mustard", "BBQ"),
  Very = c("Buffalo", "Hot Sauce")
)


#setting empty initial values
spice <- ""
bold <- ""


#getting spiceyness preference
while (spice != "Mild" && spice != "Very"){
  spice <- readline("Enter your spice preference: (Mild or Very)")
}


#getting boldness preference
while (bold != "Yes" && bold != "No"){
  bold <- readline("Enter your boldness preference: (Yes or No)")
}


#converting spice from string to index
bold <- ifelse(bold == "Yes", 1, 2)


#displaying recommendation
print(paste("You should try", chicken_recs[bold,spice], "chicken"))

