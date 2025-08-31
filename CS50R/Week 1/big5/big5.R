
data <- read.table("tests.tsv", header = TRUE, sep = "\t")


data$gender

data$gender <- factor(
  data$gender,
  labels = c("Unanswered", "Male", "Female", "Other")
)


data$extroversion <- round((data$E1 + data$E2 + data$E2) / 15, digits = 2)
data$neuroticism <- round((data$N1 + data$N2 + data$N3) / 15, digits = 2)
data$agreeableness <- round((data$A1 + data$A2 + data$A3) / 15, digits = 2)
data$conscientiousness <- round((data$C1 + data$C2 + data$C3) / 15, digits = 2)
data$openness <- round((data$O1 + data$O2 + data$O3) / 15, digits = 2)



write.csv(data, "analysis.csv")


