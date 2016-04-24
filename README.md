# Making residents happy again
Goals
-----
This project aims to characterize the livability of San Francisco neighborhoods, and does so in 2 ways:
- Giving meaningful features for each neighborhood -- crime, transportation, access to restaurants etc... --
  and tools to visualize them.
- Uncovering the relation between those features and the satisfaction of neighborhood inhabitants. 

Data and Methodology
--------------------
The satisfaction of inhabitants is inferred from surveys and the features are inferred from census data, notably from <a href="http://datasf.org">datasf.org</a>.

The neighborhood features include:
- a <b>crime</b> index, calculated from the crime density of the area.
- access to <b>schools</b>, both public and private.
- access to <b>restauration</b> services, i.e. number of close restaurants and their respective ratings.
- <b>transportation</b>, <b>affordability</b>, <b>poverty</b>, <b>ethnicity</b> indices taken directly from census data.

Tools
-----
Analysis:
- pandas, numpy, matplotlib
- jupyter
- geopy

Visualization:
- bqplot
- ipyleaflet
- jupyter widgets
