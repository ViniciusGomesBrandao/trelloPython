class client():
    import requests;
    def __init__(this, key, token):
        this.key = key
        this.token = token
        this.uri = "https://api.trello.com/1"
        pass
    
    def get(this, url, params = {}, body = {},):
        params['token'] = this.token
        params['key'] = this.key
        response = this.requests.request("GET", this.uri+url, params=params, data=body)
        return response.json()