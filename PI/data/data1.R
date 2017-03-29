# plot a scatter 2D graph
# This will produce a Rplot.pdf file after the running the Rscript, without opening the Rplot.pdf.

# collect the values together, and assign them to a variable called x
c(1,2,4,8,16,32,64,16,128,256,512,1024,2048,4096,8192) ->batch
# do the same for the corresponding y-values
c(3.3e-07,3.1e-07,2.8e-07,2.7e-07,2.6e-072.6e-07,2.5e-07,2.6e-07,0.062,0.062,0.71,0.94,1,1.1,1.1) -> rel_rms_err
plot(batch , rel_rms_err) # do a scatterplot of y on x

myString <- "Scatter ploted"
print ( myString)
