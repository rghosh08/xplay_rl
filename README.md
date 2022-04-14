# xplay_rl

```
python3 app.py

curl -X POST -H "Content-type: application/json" -d <input_json> "localhost:<port>/rl_input"

fields in input_json:
    metrics_api: similar to cloudwatch boto3
    agg_stat: mean, max, and other statistical functions
    action_space: list of all action points such as memory size
    time_interval: time interval for metric compilation
    threshold: critical value for compliance
    current_action: current value for action point
    --
    action_delta: change unit for action point (learnable parameter)
```

