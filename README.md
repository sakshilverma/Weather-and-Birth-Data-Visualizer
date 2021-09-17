# Weather-and-Birth-Data-Visualizer
Visualizing data is used by virtually every discipline these days. It is used for analyzing web traffic to determine peak server load, growth and death rate of populations for biological analysis, analyzing weather patterns over time, stock market trends, and so on. Simply put, Data Visualization brings meaning to numbers that help people understand it. Seeing the data change can draw attention to trends and spikes that may otherwise go unnoticed. Python is an open-source (free) programming language which has libraries that can be used to read and make useful graphics to present the data.

This application reads data from CSV files and visualize the data using various techniques using existing Python libraries like pandas, matplotlib and seaborn. 
In this application I have used three data sets -
1. Contains yearly temperature and rainfall data.
2. Contains yearly and monthly birth data.
3. Contains monthly rainfall and temperature data.

In PandasDfGraph Program -
* A Table using Pandas dataframe would be created and printed.
* Statistics based on the table values would be created.
* A Line graph with an X-axis and Y-axis using Pandas would be created.
* A window showing the graph using Matplotlib’s pyplot would be displayed for visualization.   

In MatPlotLib_PyPlot Program -
* A Pyplot plot using Temperature and Month would be created and displayed for visualization.  
* A Pyplot using Rainfall and Month would be created and displayed for visualization.  
* A Pyplot plot using Month on the X-axis, Temperature and Rainfall together on the Y-axis would be created and displayed for visualization by creating a Legend for the graph.

In SeabornScatter-RegressionplotGraph Program -
* A Scatter plot using Year and Temperature would be created and displayed for visualization showing individual data points scattered.
* A Scatter plot using Rainfall and Temperature would be created and displayed for visualization showing individual data points scattered.
* A Regression Plot using Year and Temperature would be created and displayed for visualization showing possible correlation.
* A Regression Plot using Rainfall and Temperature would be created and displayed for visualization showing possible correlation.

In SeabornHeatmap Program -
* Data is reorganized into a Matrix using pivots. 
* A colourful Graph is created and displayed which is good for spotting large and small values quickly and it has a color key on the side.

In SeabornJointPlot Program -
* A Graph good for looking at distribution and data points at the same time would be created and displayed for visualization.
* A Graph of hex kind would be created and displayed for visualization.
* A Graph good to see scatter with regression line, as well as distribution would be created and displayed for visualization.
