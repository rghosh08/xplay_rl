# xplay_rl

```
python3 app.py

request: 

    curl -X POST -H "Content-type: application/json" -d <input_json> "localhost:<port>/rl_input"

    fields in input_json:
        data: metrics data
        agg_stat: mean, max, 95th percentile, and other statistical functions
        max_threshold: upper limit for the critical compliance value
        min_threshold: lower limit for the critical compliance value
        current_action: current value for action point
        action_delta: change unit for action point (learnable parameter)
        

response: 
    output json: 
        json.dump({'ouput_action': output_action, 'flag': flag})
            rec_action: recommended action (float: should be converted to the right datatype.)
            flag: a boolean value which indicates whether theshold is already satified. 
                The default flag value is equal 1 which indicates non-compliance.


```


