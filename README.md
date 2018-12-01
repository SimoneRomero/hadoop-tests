# Practicing with Hadoop 

Hadoop implementations made in order to attend the Data Scientist Nanodegree Program from Udacity - module Big Data and Hadoop.


### Optional Project from Hadoop and Big Data module

#### Part I

Now it's time for you to have a go at this. For starters you will have to work with the same data set - sales data, that we discussed in lessons. You will have to write some Mappers and Reducers yourself and then answer the questions about data that follow. You will have to do the data processing on your local pseudo-distributed cluster, but you will be able to see if your solution was correct by submitting your results to our system.

The three questions that you have to answer about this data set are:

1. Find the sales by product category across all of our stores. 
	* sales-per-category folder.
	* The result file has the format: "category" "total-sales"
2. Find the monetary value for the highest individual sale for each separate store. 
	* highest-value folder.
	* The result file has the format: "store" "total-sales"
3. Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.
	* total-sales folder
	* The result file has the format: "number-sales" "total-sales"
4. Find the mean (average) of sales for each weekday. 
	* average-sales folder
	* The result file has the format: "weekday" "total-sales" "number-sales" "average"


Format of each line from "purchases.txt" is:
"date" "time" "store-name" "item-description" "cost" "method-of-payment"

#### Part II

We've talked about how Hadoop works, you've seen Hadoop code, and you've written some code of your own using our store sales data. Now we'd like you to solve some problems using a different dataset on your own. You'll have to write your Mappers and Reducers from scratch; please use Python. You will have to do the data processing on your local pseudo-distributed cluster, but you will be able to see if your solution was correct by submitting your results to our system.

The data set we're using is an anonymized Web server log file from a public relations company whose clients were DVD distributors. The log file is in the udacity_training/data directory, and it's currently compressed using GnuZip. So you'll need to decompress it and then put it in HDFS. If you take a look at the file, you'll see that each line represents a hit to the Web server. It includes the IP address which accessed the site, the date and time of the access, and the name of the page which was visited.

The questions that you have to answer about this data set are:
1. Find the number of hits for each different file on the Web site
	* hits-to-page folder
	* The result file has the format: "total access"
2. Find the number of hits to the site made by each different ip address
	* hits-from-ip folder
	* The result file has the format: "ip" "total access"

Format of each line from "access-log" is:

%h %l %u %t \"%r\" %>s %b

Where:

- %h is the IP address of the client
- %l is identity of the client, or "-" if it's unavailable
- %u is username of the client, or "-" if it's unavailable
- %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
- %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
- %>s is the status code that the server sends back to the client.
- %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
