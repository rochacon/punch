import punch


app = punch.App()


@app.view('/', methods=('POST',))
def post(request):
   return request.json_body


if __name__ == '__main__':
   app.serve()
