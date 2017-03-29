# plot a scatter 2D graph
# This will produce a Rplot.pdf file after the running the Rscript, without opening the Rplot.pdf.

# collect the values together, and assign them to a variable called x
c(44, 7, 9, 16, 7) -> x
# do the same for the corresponding y-values
c(13, 2, 71, 4, 9) -> y
plot(x , y) # do a scatterplot of y on x
myString <- "Hello, World!"
print ( myString)
