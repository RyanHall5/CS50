url <- readline("Enter your csv: ")

csv <- read.csv(url)

numStops <- nrow(csv)

shortest <- min(csv$time)

longest <- max(csv$time)

totalTime <- sum(csv$time)

print(numStops)
print(shortest)
print(longest)
print(totalTime)



