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
            obj = RL(rl_input["data"], rl_input["agg_stat"]);
            rec_action, flag = obj.policy(rl_input["max_threshold"], rl_input["min_threshold"], rl_input["current_action"], rl_input["action_delta"])
            return json.dump({
                'rec_action': rec_action, 
                'flag': flag
            });
        except:
            print('an error has occured')
    else:
        print("content type not support")

if __name__ == "__main__":
    app.run()

    