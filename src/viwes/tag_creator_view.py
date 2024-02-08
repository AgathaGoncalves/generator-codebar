from src.viwes.http_types.http_request import  HttpRequest
from src.viwes.http_types.http_response import  HttpResponse


class  TagCreatorView:

    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        print('To no arquivo tag_creator_view')

        return HttpResponse(status_code=200,
                            body={"message": f"Tag created for the product {product_code}"})
