import sniffio
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import syncopate

sniffio.current_async_library_cvar.set("asyncio")


async def homepage(request):
    return JSONResponse({"hello": "world"})


routes = [Route("/", endpoint=homepage)]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    syncopate.run(app)
