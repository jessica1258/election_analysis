# Election Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has requested the following analysis to complete an election autid of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Create an inventory of the counties where votes were cast.
3. Calculate the number of votes cast in each county
4. Calculate the percent of votes cast in each county relative to all votes cast.
5. Determine the county with the highest voter turnout (i.e., the largest number and percentage of votes cast).
6. Create an inventory of the candidates who received votes.
7. Calculate the number of votes each candidate received.
8. Calculate the percent of votes each candidate received.
9. Determine the winner of the election based on the popular vote.

## Election Audit Results
Analysis showed the following:
- During the election, there were 369,711 votes cast.
- The candidates who received votes were Charles Casper Stockham, Diane DeGette and Raymon Anthony Doane.
- The voter turnout of the election by county was:
  - There were 38,855 votes cast in Jefferson county, which was 10.5% of the total votes cast.
  - There were 306,055 votes cast in Denver county, which was 82.8% of the total votes cast.
  - There were 24,801 votes cast in Arapahoe county, which was 6.7%
  - The largest number of votes were cast in Denver county.
- The results of the election for each candidate were:
  - Charles Casper Stockham recieved 85,213 votes, which was 23.0% of the total votes cast.
  - Diane DeGette recieved 272,892 votes, which was 73.8% of the total votes cast.
  - Raymon Anthony Doane recieved 11.606 votes, which was 3.1% of the total votes cast.
  - The winner of the election was Diane DeGette based on having received 73.8% of the vote, or 272,892 votes.

## Election Audit Summary
The election analysis performed can be used for any election regardless of location or number of candidates as long as it is a single role being elected. The only requirements to use the query unchanged is that an input file have a format consistent with the election_results.csv file, specifically with each row of data representing a single vote and with the county displayed in the second field (or column) and the candidate that the vote was cast for in the third filed (or column). 

First, with minor modifications the analysis could be expanded to handle elections with multiple roles on the ballot rather than a single role at a time. In order to handle mulitple elections at once, this would be dependent on an additional data element indicating the role being elected and muliple records for each role or by adding additional columns for each role in the election. With that information, additional criteria could be added to for loops and conditional (if) statements to count votes for distinct roles. In this case, output formating and information would also need to be changed, resulting in modification to print and write logic to clearly communicate the specific role being elected.

Second, with minor modifications the analysis could be expanded to handle national and more locally scaled elections where state or zip code level results are more relevant for reporting than counties. This would require naming conventions in the code to be changed to better explain the geographic level and to generate output language that is appropriate to the varying geographies.  
