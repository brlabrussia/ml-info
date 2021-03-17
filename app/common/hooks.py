def preprocess_exclude_non_api(endpoints, **kwargs):
    return [
        (path, path_regex, method, callback)
        for path, path_regex, method, callback in endpoints
        if path.startswith('/api')
    ]
