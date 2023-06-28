class MasterData:
    def __init__(self):
        self.original = {
            'original_ids': [],
            'dataframe': pd.DataFrame,
            'history': []
        }

        self.correlation = {
            'correlation_ids': [],
            'dataframe': pd.DataFrame,
            'history': []
        }

        self.current = {
            'current_ids': [],
            'dataframe': pd.DataFrame,
            'history': []
        }

        self.all = {
            'all_ids': [],
            'dataframe': pd.DataFrame,
            'history': []
        }

    def set_master_data(self, data, ids, type):
        if type == 'original':
            self.original['dataframe'] = data
            self.original['original_ids'] = ids
        elif type == 'correlation':
            self.correlation['dataframe'] = data
            self.correlation['correlation_ids'] = ids
        elif type == 'current':
            self.current['dataframe'] = data
            self.current['current_ids'] = ids
        elif type == 'all':
            self.all['dataframe'] = data
            self.all['all_ids'] = ids

    def get_master_data(self, type):
        if type == 'original':
            return self.original['dataframe']
        elif type == 'correlation':
            return self.correlation['dataframe']
        elif type == 'current':
            return self.current['dataframe']
        elif type == 'all':
            return self.all['dataframe']