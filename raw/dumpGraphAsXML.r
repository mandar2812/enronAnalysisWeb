#! /usr/bin/Rscript
#load("../enVar.Rdata")
library(rgexf, lib.loc = "/usr/local/lib/R/site-library")
args <- commandArgs(trailingOnly = TRUE)


lim = args[1]
fileName1 = args[2]
setwd("../../data/proc")

if(!file.exists(fileName1)) {
    cat("\n... File Doesnt Exist ...\n")
    q()
}


df <- read.csv(fileName1, sep = "|", quote = "\'",
               header = TRUE, stringsAsFactors = FALSE)
dt <- as.POSIXct(Sys.time())

dumpFileName <- paste("graph-sample-", lim, "-",
                      format("%Y-%m-%d-%H-%i-%s", dt), ".gexf", sep = "")
summary(df)


edgeList <- edge.list(df[,c("From", "To")])
gexfObj <- write.gexf(edgeList$nodes, edgeList$edges,
                      edgesWeight = df[, "EdgeStrength"], output = dumpFileName)
