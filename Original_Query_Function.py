import requests
import flatten_json
import pandas as pd

def get_zenodo_search_output(search_term, page, size):
    """Return the outputs for a Zenodo output query 
    
    Parameters
    ----------
    search_term: str
    page: int
    size: int 
    
    Returns
    -------
    output_df = pd.DataFrame
    """
    
    assert isinstance(search_term, str)
    assert isinstance(page, int)
    assert isinstance(size, int)
    
    search_url = 'https://zenodo.org/api/records'
    search_params = {'q': search_term, 'page': page, 'size': size}
    
    r = requests.get(search_url, params = search_params)
    output = r.json()
    
    if r.status_code == 200 and output.get('hits').get('hits'):
        output_df = pd.DataFrame(output['hits']['hits'])
    else:
        return r
    
    return output_df