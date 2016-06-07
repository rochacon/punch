import punch


app = punch.App()


@app.after
def api_version(request, response):
    response.headers['X-Api-Version'] = '1'


@app.before
def authenticate(request):
   if request.authorization != ('Bearer', 'token'):
      response = punch.Response()
      response.status_int = 401
      response.json = {"status": "Unauthorized"}
      return response


@app.view('/')
def index(request):
   return {
      'hello': 'world',
   }


if __name__ == '__main__':
   app.serve()
