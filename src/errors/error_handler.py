from src.viwes.http_types.http_response import HttpResponse

def handle_errors(error: Exception) ->HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
