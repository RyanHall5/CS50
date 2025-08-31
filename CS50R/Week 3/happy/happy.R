#creating function to get score for any specific year and country
get_score <- function(year, country){
  data <- read.csv(paste(year, ".csv", sep = ""))
  if(!(country %in% data$country)){
    return ("data unavailable")
  }
  filter <- data["country"] == country
  countryData <- data[filter]
  round(sum(as.double(countryData[2:8])), digits = 2)
}

name <- readline("Country: ")
for(i in 2020:2024){
  cat(name, "(", i, "): ", get_score(i, name), "\n", sep="")
}



