Build a front end application using statcast data that answers a specific and unique question. 

**Decided**

1) Simple UI that selects pitch, location, rotation, (and maybe others) and gives the most likely outputs
2) Simple UI to select the type of pitch and count and determine who would be the best and worse hitter to have hit it (Filter by team, position, etc)
* Drag and drop the location of the ball in virtual strike zone
* Velocity meter
* Pitch type selection

# ML

## Steps
* [ ] Understand the Nietche example
* [ ] Use keras to predict the pitch type
* [ ] Use keras to predict the swing and miss potential of a pitch
* [ ] Use keras to predict the result of given pitch
* [ ] Generate the best hitter for every single given variable 

## Setting up Data
* [ ] Filter out all data except hitterid, velocity, final location, rotation
 
## Resources
* https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py
* http://karpathy.github.io/neuralnets/

--------------------------------
### Future Ideas
* Hit probability UI
  * Looks at all pitches that are 'similar' to a thrown pitch and result from the data. If it matches indicate what the likely outcome of that result is
  * https://baseballsavant.mlb.com/statcast_hit_probability
  * https://baseballsavant.mlb.com/statcast_search?hfPT=FF%7C&hfAB=&hfBBT=&hfPR=hit%5C.%5C.into%5C.%5C.play%7Chit%5C.%5C.into%5C.%5C.play%5C.%5C.no%5C.%5C.out%7Chit%5C.%5C.into%5C.%5C.play%5C.%5C.score%7C&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7C&hfC=&hfSea=2018%7C&hfSit=&player_type=pitcher&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&hfInfield=&team=&position=&hfOutfield=&hfRO=&home_road=&hfFlag=&hfPull=&metric_1=&hfInn=&min_pitches=0&min_results=0&group_by=name&sort_col=pitches&player_event_sort=h_launch_speed&sort_order=desc&min_pas=0#results
* 
* https://statsapi.mlb.com/api/v1/game/531060/playByPlay?timecode=20180803_182458
* Application that determines which is the best pitch pitcher is the best to throw against a given batter and count. 
   * Even of pitches that don't exist (put rails on this though)
* Daily Unusual Stats 
* Deep dive into a specific stat (Ball rotation, catcher pop time)

## Similar Projects
* https://medium.com/tensorflow/predicting-balls-and-strikes-using-tensorflow-js-2acf1d7a447c
* https://github.com/tensorflow/tfjs-examples/tree/master/baseball-node

### Data
* https://github.com/baseballhackday/data-and-resources/wiki/Resources-and-ideas
* http://gd2.mlb.com/components/game/mlb/year_2018

### Resources
* https://aws.amazon.com/statcastai/

### Implementation
* Use AWS/Google to run the table rollups to answer questions from the front end

