import punch


app = punch.App()


@app.after
def api_version(request, response):
    response.headers['X-Api-Version'] = '1'


@app.before
def authenticate(request):
    if request.authorization != ('Bearer', 'token'):
        return punch.Response(json={
            'status': 'Unauthorized',
        }, status=401)


@app.view('/')
def index(request):
   return {
      'hello': 'world',
   }


if __name__ == '__main__':
   app.serve()
