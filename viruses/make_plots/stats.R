normalised=read.csv("~/alldata.normalised.csv", header=TRUE)
mytab= with(normalised,table(normalised$normalised_count,normalised$type))
chisq.test(mytab, simulate.p.value = TRUE)
# Explanation: We used Pearson's Chi-squared test to verify the difference in distributions of normalized counts between control and experimental groups. This results in a p-value = 0.0004998, supporting our initial findings that the two distributions are significantly different.