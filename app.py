import json
import logging
from rl import RL
from flask import Flask, request
app = Flask(__name__)

@app.route('/rl_input', methods=['GET', 'POST'])
def rl(rl_input):
    content_type = request.headers.get('Content-Type')
    if (content_type=='application/json'):
        try:
            rl_input = request.json
            obj = RL(rl_input["metrics_api"], rl_input["agg_stat"], rl_input["action_space"]);
            output_action = obj.policy(rl_input["time_interval"], rl_input["threshold"], rl_input["current_action"], rl_input["action_delta"])
            return json.dump({'ouput_action': output_action});
        except:
            print('an error has occured')
    else:
        print("content type not support")



if __name__ == "__main__":
    app.run()

    