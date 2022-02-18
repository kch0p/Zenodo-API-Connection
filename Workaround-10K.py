import requests
import flatten_json
import pandas as pd



def get_zenodo_search_output(search_term):
    """Return the outputs for a Zenodo output query 
    
    Parameters
    ----------
    search_term: str
    
    Returns
    -------
    output_df = pd.DataFrame
    """
    
    assert isinstance(search_term, str)

    search_url = 'https://zenodo.org/api/records'
    search_params = {'q': search_term, 'size': 100}
    
    r = requests.get(search_url, params = search_params)
    output = r.json()
    
    if not (r.status_code == 200 and output.get('hits').get('hits')):
        return output
        
    cumulative_df = pd.DataFrame()
    
    while r.status_code == 200 and output['links'].get('next'):
        hits_df = pd.DataFrame(output['hits']['hits'])
        
        cumulative_df = pd.concat([cumulative_df, hits_df]).reset_index(drop=True)
        
        r = requests.get(output['links']['next'])
        output = r.json()
    
    hits_df = pd.DataFrame(output['hits']['hits'])
    cumulative_df = pd.concat([cumulative_df, hits_df]).reset_index(drop=True)
        
    
    return cumulative_df