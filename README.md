# xplay_rl

```
python3 app.py

request: 

    curl -X POST -H "Content-type: application/json" -d <input_json> "localhost:<port>/rl_input"

    fields in input_json:
        data: state data
        agg_stat: mean, max, and other statistical functions
        action_space: list of all action points such as memory size
        time_interval: time interval for metric compilation
        threshold: critical value for compliance (min_threshold)
        current_action: current value for action point
        --
        action_delta: change unit for action point (learnable parameter)

response: 

        json.dump({'ouput_action': output_action})

