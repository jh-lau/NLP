## end-to-end story 1
* greet: hello
    - utter_ask_howcanhelp   <!-- predicted: utter_greet -->
* inform: show me [chinese](cuisine) restaurants   <!-- predicted: affirm: show me chinese restaurants -->
    - utter_ask_location   <!-- predicted: utter_happy -->
* inform: in [Paris](location)   <!-- predicted: mood_unhappy: in Paris -->
    - utter_ask_price   <!-- predicted: utter_cheer_up -->


