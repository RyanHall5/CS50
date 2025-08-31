#getting intended route from user
input <- readline("Route: ")


#reading both CSVs
rail_csv <- read.csv("rail.csv")
bus_csv <- read.csv("bus.csv")



#validating input
while(!(input %in% rail_csv$route || input %in% bus_csv$route)){
  print("Invalid Input!")
  input <- readline("Route: ")
}



#reading correct dataset based on input
ifelse(input %in% rail_csv$route, data <- rail_csv, data <- bus_csv)


#creating reliability vector
data$reliability <- data$numerator / data$denominator


#creating new vectors with only relevant data
peak_vector <- data$reliability[data$route == input & data$peak == "PEAK"]
off_peak_vector <- data$reliability[data$route == input & data$peak == "OFF_PEAK"]


#calculating percentage on time for both scenarios
peak_percent <- sum(peak_vector) / length(peak_vector) * 100
off_peak_percent <- sum(off_peak_vector) / length(off_peak_vector) * 100


#rounding percentages
peak_percent <- round(peak_percent, digits = 0)
off_peak_percent <- round(off_peak_percent, digits = 0)

print(paste("On time ",  peak_percent, "% of the time during peak hours.", sep = ""))
print(paste("On time ", off_peak_percent, "% of the time during off-peak hours.", sep = ""))