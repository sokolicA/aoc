library(here)

file_path <- here::here("2025", "d6", "p1.txt")


tbl <- read.table(file_path, header=FALSE)


p1 <- sapply(tbl, function(x) {eval(parse(text=paste(head(x, -1), collapse=tail(x, 1))))}) |> sum()
print(as.character(p1))


read_file <- function(path) {
    tryCatch(
        {
            con <- file(path, "r")
            lines <- readLines(con, warn=FALSE)
            print(lines)
        },
        error=function(e) print(e),
        finally=close(con)
    )
}
lines <- read_file(file_path)

split <- sapply(lines, function(x) strsplit(x, split="", fixed=TRUE), USE.NAMES = FALSE)

ncols <- length(split[[1]])
nrows <- length(split)

r <- vector(mode="character")
res <- vector(mode="numeric")
op <- ""
for (i in ncols:1) {
    if(split[[nrows]][i] != " ") {
        op <- split[[nrows]][[i]]
    }
    v <- sapply(split[-nrows], function(x) {trimws(x[i])})
    str <- paste(v, collapse ="")
    if (i==1) {r <- c(r, str)}
    if(trimws(str) == "" || i ==1) {
        suma <- eval(parse(text=paste(r, collapse=op)))
        r <- character()
        op <- ""
        res <- c(res, suma)
    } else {
        r <- c(r, str)
    }
}

options(scipen=999)
print(sum(res))