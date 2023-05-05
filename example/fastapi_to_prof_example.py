"""
This example shows how to output the profile
to a .prof file.
"""
import os
import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi_profiler import PyInstrumentProfilerMiddleware


app = FastAPI()
app.add_middleware(
    PyInstrumentProfilerMiddleware,
    server_app=app,  # Required to output the profile on server shutdown
    profiler_output_type="prof",
    is_print_each_request=False,  # Set to True to show request profile on
    # stdout on each request
    prof_file_name="example_profile.prof",  # Filename for output
)


@app.get("/test")
async def normal_request():
    return JSONResponse({"retMsg": "Hello World!"})


# Or you can use the console with command "uvicorn" to run this example.
# Command: uvicorn fastapi_example:app --host="0.0.0.0" --port=8080
if __name__ == "__main__":
    app_name = os.path.basename(__file__).replace(".py", "")
    uvicorn.run(app=f"{app_name}:app", host="0.0.0.0", port=8080, workers=1)
