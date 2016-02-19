import punch


app = punch.App()


@app.view('/')
def index(request):
   return {
      'hello': 'world',
   }


if __name__ == '__main__':
    app.serve()
