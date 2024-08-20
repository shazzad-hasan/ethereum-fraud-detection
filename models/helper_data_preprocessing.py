from sklearn.base import BaseEstimator, TransformerMixin
from typing import List, Optional, Union

class DataPrep(BaseEstimator, TransformerMixin):
    ''' Preprocess dataset.'''

    def __init__(self, features: List[str],
                 features_to_drop: Optional[List[str]] = None,
                 fill_strategy: Union[int, str] = 0,
                 upper_clip_quantile: Optional[float] = None,
                 lower_clip_quantile: Optional[float] = None):
        '''
        Parameters:
            - `features`: List of feature names to be processed.
            - `features_to_drop`: List of feature names to be dropped.
            - `fill_strategy`: Strategy to fill NaNs (0, 'mean', 'median').
            - `upper_clip_quantile`: Upper quantile for clipping outliers.
            - `lower_clip_quantile`: Lower quantile for clipping outliers.
        '''
        self.features = features
        self.features_to_drop = features_to_drop
        self.fill_strategy = fill_strategy
        self.upper_clip_quantile = upper_clip_quantile
        self.lower_clip_quantile = lower_clip_quantile

    def fit(self, df):
        self.fill_values = {}
        self.upper_clip_values = {}
        self.lower_clip_values = {}

        fill_function = {
            'median': lambda feature: df[feature].median(),  
            'mean': lambda feature: df[feature].mean(),    
            0: lambda feature: 0
        }.get(self.fill_strategy)

        for feature in self.features:
            if fill_function:
                self.fill_values[feature] = fill_function(feature)  
            else:
                self.fill_values[feature] = None

            if self.upper_clip_quantile:
                self.upper_clip_values[feature] = df[feature].quantile(self.upper_clip_quantile)

            if self.lower_clip_quantile:
                self.lower_clip_values[feature] = df[feature].quantile(self.lower_clip_quantile)

        if self.features_to_drop:
            self.features = [feature for feature in self.features if feature not in self.features_to_drop]

        return self

    def transform(self, df):

        # Drop specified features
        if self.features_to_drop:
            df = df.drop(columns=self.features_to_drop)

        # Fill NaN values
        for feature in self.features:
            df[feature] = df[feature].fillna(self.fill_values.get(feature))

        # Clip outliers
        if self.upper_clip_quantile:
            for feature in self.features:
                df[feature] = df[feature].clip(upper=self.upper_clip_values[feature])

        if self.lower_clip_quantile:
            for feature in self.features:
                df[feature] = df[feature].clip(lower=self.lower_clip_values[feature])

        return df