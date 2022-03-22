import pandas as pd

class PostalCode:
    
    def __init__(self, prefix_url, suffix_range, suffix_leading_zero_len):
        self.prefix_url = prefix_url
        self.suffix_range = suffix_range
        self.suffix_leading_zero_len = suffix_leading_zero_len

    def get_valid_postal_code_prefix_from_url(self):
        df = pd.read_html(self.prefix_url, skiprows=1)    
        postal_df = df[0]
        postal_prefix_lst = postal_df[1].tolist()
        postal_prefix = ','.join(postal_prefix_lst).replace(' ', '')
        self.postal_prefix_lst = postal_prefix.split(',')

    def get_postal_code(self):
        postal_code = []
        for suffix in self.suffix_range:
            for prefix in self.postal_prefix_lst:            
                current_postal_code = f"{prefix}{str(suffix).zfill(self.suffix_leading_zero_len)}"
                postal_code.append(current_postal_code)

        return postal_code
    