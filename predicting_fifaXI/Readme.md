# Best Playing XI Selection for Football team through Data Science Techniques

## Contributors

- Tushar Tanwar - @tushartanwar - tusharta@buffalo.edu
- Dipankar Sharma - @dipankar17 - dsharma8@buffalo.edu
- Kewal Chheda - @kewalchh - kewalchh@buffalo.edu

## Introduction

Data Science could be useful for Football club managers to make decision on biding players or team selection based on players playing skills and position. We have scraped the data for 20k players from sofifa.com and used machine learning algorithm to determine the best players for every position. Our goal is to build a team of 3-4-3 formation out of 20k players based on the selected configuration of attacking, defensive and balanced so that the overall rating of the team comes out to be 84.

## Data Description

sofifa.com maintains the list of players along with their attributes rating and personal information.

Data scraped from sofifa.com using python module Scrapy and it has been divided into the below schema tables:

- player_personal_info
  **Columns:** player_id, name, photo_url, weight, age, height, nationality
  **Description:** Contains personal info of player

- player_club_info
  **Columns:** player_id, club_name, club_flag_url, club_playing_position, club_jersey_number, current_club_joined_dt, current_club_contract_valid_yr
  **Description:** Contains players club information

- player_country_info
  **Columns:** player_id, country, country_flag_url, country_playing_position, country_jersey_number
  **Description:** Contains players Country team information

- player_financial_info
  **Columns:** player_id, value, wage
  **Description:** Contains players financial information

- player_attributes_info
  **Columns:** player_id, weak_foot, international_reputation, weak_foot, skill_moves, overall_rating, potential, Crossing, Finishing, heading_accuracy, short_passing, Volleys, Dribbling, Curve, FK_Accuracy, Long_Passing, Ball_Control, Acceleration, Sprint_Speed, Agility, Reactions, Balance, Shot_Power, Jumping, Stamina, Strength, Long Shots, Aggression, Interceptions, Positioning, Vision, Penalties, Defensive_Awareness, Standing_Tackle, Sliding_Tackle, GK_Diving, GK_Handling, GK_Kicking, GK_Positioning, GK_Reflexes
  **Description:** Contains player's skills rating

- player_positions_info
  **Columns:** player_id, LS, ST, RS, LW, LF, CF, RF, RW, LAM, CAM, RAM, LM, LCM, CM, RCM, RM, LWB, LDM, CDM, RDM, RWB, LB, LCB, CB, RCB, RB
  **Description:** Contains player's playing position rating

  ## Data Analysis

  Data analysis is done to understand the pattern of attributes of players for different positions along with the dependency of these attributes on different player characteristics like age, BMI, wage, etc.
  Data analysis is being done for the following:

  - Top 5 football clubs with players collectively higher overall rating
  - Top 5 football clubs with players collectively higher value
  - Players position and comparison to their values
  - Players Age vs Rating vs Value
  - Correlation of Players attributes

  ## Execution

  - Python Scrapy module to scrape data from sofifa.com in a csv file.
  - Loaded csv file in Pandas to clean, normalize, de-duping and load data in sqlite3 tables.
  - Used matplotlib and seaborn to visualize the data from the sqlite3 tables.
  - Identified key attributes necessary for every position and added weights to those attributes using Pandas.
  - Data segregation as per playing position using Pandas to implement K-Nearest Neighbor for predicting each player’s best position as per the algorithm.
  - Assigned points to every player as per the predicted position on the basis of the rating in the key attributes necessary for that position.
  - Linear programming using python module Pulp to formulate an equation for an attacking,
    defensive and balanced team with an overall rating of 84.
  - Fit the players in the equation as per the assigned points using Pulp.
  - Image processing using python module PIL to visualize the selected players as per their position on a football field.

  ## Player Classification Model

  Using K-nearest neighbor, try to predict the players position in football based on the players playing attributes.
  Took player preferred position as the class and their attributes as the features to feed it into the KNN classifier so that a cluster for player attributes as per their positions can be formed.

  ## Results

  Below are the results after training the model.
  **Nearest Neighbors:** 7
  **Training Error:** 0.09509408602150538
  **Test Error:** 0.11581067472306139
  **CV Error:** 0.120943 +-0.021380

  ## Conclusion

  We formulated a team of 11 players for the formation 3-4-3 by predicting the player position using KNN classifier and formed three teams as attacking, defensive and balanced so that the overall rating of the team comes out to be 84.

  ## Future Research Directions

  Right now, we have only considered the attributes of the player while forming the team but below are the things which can be considered:

  - Wage of the players can also be considered while forming the team as every club has a fixed budget in which they have to accommodate all the players’ wages.
  - Preferred leg of the players can also be considered while selecting the position of the player.
  - Players coordination can also be considered while forming the team.
  - Overall team rating can be parameterized because as of now we have only considered the
    overall team rating to be 84.
  - There are different formations for which the prediction can be made. Right now, we have only considered 3-4-3 formation.

  ## References

  - https://sofifa.com/
  - https://www.fontsquirrel.com/fonts/list/popular
  - https://python-graph-gallery.com/100-calling-a-color-with-seaborn/
  - http://logfact.com/football-soccer-field-player-positions-abbreviations/