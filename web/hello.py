def app(environ, start_response):
    # bm
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]