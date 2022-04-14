class RL(object):
    def __init__(self, metrics_api, agg_stat, action_space):
        '''
            metrics_api: similar to cloudwatch boto3
            agg_stat: mean, max, and other statistical functions
            action_space: list of all action points such as memory size
        '''
        self.metrics_api = metrics_api
        self.agg_stat = agg_stat
        self.action_space = action_space
        

    def policy(self, time_interval, threshold, current_action, action_delta):
        '''
            time_interval: time interval for metric compilation
            threshold: critical value for compliance
            current_action: current value for action point
            action_delta: change unit for action point (learnable parameter)
            
        '''
        current_metrics = self.metric_api(time_interval)
        if self.agg_stat(current_metrics) < threshold:
            return current_action
        else:
            current_action -= action_delta
            current_metrics = self.metric_api(time_interval)
