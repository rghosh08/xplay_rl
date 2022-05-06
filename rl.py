class RL(object):
    def __init__(self, data, agg_stat):
        '''
            data: metrics data
            agg_stat: mean, max, 95th percentile, and other statistical functions
        '''
        self.data = data
        self.agg_stat = agg_stat
        
    def policy(self, max_threshold, min_threshold, current_action, action_delta):
        '''
            Input: 
                max_threshold: upper limit for the critical compliance value
                min_threshold: lower limit for the critical compliance value
                current_action: current value for action point
                action_delta: change unit for action point (learnable parameter)
            Output:
                rec_action: recommended action
                flag: a boolean value which indicates whether theshold is already satified. 
                      The default flag value is equal 1 which indicates non-compliance.
            
        '''
        current_metrics = self.data
        flag=1
        if (self.agg_stat(current_metrics) < max_threshold) and (self.agg_stat(current_metrics) > min_threshold):
            rec_action, flag = current_action, 0
            
            return rec_action, flag
        else:
            if self.agg_stat(current_metrics) >= max_threshold:
                current_action -= action_delta
            else:
                current_action+=action_delta

            rec_action=current_action;

            return rec_action, flag

            

            
