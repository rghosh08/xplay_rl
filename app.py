from rl import RL
from flask import Flask
app = Flask(__name__)

@app.route('/rl', methods=['GET', 'POST'])
def rl(metrics_api, agg_stat, action_space, threshold, current_action, action_delta, time_interval):
    obj = RL(metrics_api, agg_stat, action_space);
    return obj.policy(time_interval, threshold, current_action, action_delta)

if __name__ == "__main__":
    app.run()