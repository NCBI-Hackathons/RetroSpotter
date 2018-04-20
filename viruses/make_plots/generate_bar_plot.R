<- read.csv("~/aml.normalised.pivot.zeroes.csv")

f1 <- colMeans(f[sapply(f, is.numeric)])

g1 <- colMeans(g[sapply(g, is.numeric)])

h <- as.data.frame(cbind(f1, g1))

colnames(h) <- c("Control", "AML")

h2 <- data.table::setDT(h, keep.rownames = TRUE)[]

fm <- melt(h2[,c('rn','Control','AML')],id.vars = 1)

ggplot(fm,aes(x = rn, y = value)) + geom_bar(aes(fill = variable), stat = "identity", position = "dodge") + scale_fill_manual(values=c("#619CFF", "#F8766D")) + labs(title = "Endogenous Retroviral RNA Expression", x = "Retroviral Sequence", y = "Average Expression") + theme(axis.text.x = element_blank())


