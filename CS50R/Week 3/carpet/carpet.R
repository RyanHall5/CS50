calculate_growth_rate <- function(years, visitors) {
  (visitors[length(visitors)] - visitors[1]) / (years[length(years)] - years[1])
}

predict_visitors <- function(years, visitors, year) {
  growth <- calculate_growth_rate(years, visitors)
  visitors[length(visitors)] + (year - years[length(years)]) * growth
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
