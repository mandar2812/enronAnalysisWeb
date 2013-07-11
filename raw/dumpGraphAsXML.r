#! /usr/bin/Rscript
library(rgexf)
args <- commandArgs(trailingOnly = FALSE)


lim = args[0]
fileName = args[1]
setwd("../../data/proc")

if(!file.exists(fileName)) {
    cat("\n... File Doesnt Exist ...\n")
    q()
}


df <- read.csv(fileName, sep = '|', quote = "\'",
               header = TRUE, stringsAsFactors = FALSE)
dt <- as.POSIXct(Sys.time())

dumpFileName <- paste("graph-sample-", lim, "-",
                      format("%Y-%m-%d-%H-%i-%s"), ".gexf", sep = "")
str(df)
edgeList <- egde.list(df[,c("From", "To")])
gexfObj <- write.gexf(edgeList$nodes, edgeList$edges,
                      edgesWeight = df[, "EdgeStrength"], output = dumpFileName)
