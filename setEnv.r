#! /usr/bin/R

#"We define constants needed throughout the code base here
#'run this script only from the directory it is stored in

wd <- getwd()
spl <- strsplit(wd, "/")

ln <- length(spl[[1]])
tmp = paste(spl[[1]][1:ln-1], collapse = "/")
#'The data directories
dataDir <- list(raw = paste(tmp, "data", "raw", sep = "/"),
                processed = paste(tmp, "data", "proc", sep = "/"))
#'The code directories
codeDir <- list(raw = paste(wd, "raw", sep="/"),
                final = paste(wd, "final", sep="/"))
#'Figures
figDir <- list(raw = paste(tmp, "figures", "raw", sep = "/"),
                final = paste(tmp, "figures", "final", sep = "/"))

#'Reports
reportDir <-  paste(tmp, "reports", sep = "/")

#'Saving it so it is accesible for the other scripts via .RData File
save(dataDir, codeDir, figDir, reportDir, file = paste(wd, "envVar.RData", sep = "/"))


    
